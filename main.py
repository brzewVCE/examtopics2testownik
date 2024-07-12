from bs4 import BeautifulSoup
import json


# Sample HTML content as a string (substitute this with your actual HTML file content)
with open('./html/1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all question cards
question_cards = soup.find_all("div", class_="card exam-question-card")

# Initialize a list to hold all extracted data
extracted_data = []

# Process each question card
for card in question_cards:
    question_data = {}
    
    # Extract question number and title
    header = card.find("div", class_="card-header").get_text(strip=True)
    question_data['Question'] = header
    
    # Extract the question text
    question_text = card.find("div", class_="card-body").find("p", class_="card-text").get_text(" ", strip=True)
    question_data['Text'] = question_text.replace('Reveal Solution Hide Solution', '').strip()
    
    # Find all answer choices
    answers = card.find_all("li", class_="multi-choice-item")
    choices = []
    for answer in answers:
        choice_letter = answer.find("span", class_="multi-choice-letter").get_text(strip=True)
        choice_text = answer.get_text(strip=True)
        choices.append(f"{choice_text[2:]}")
    question_data['Choices'] = choices
    
    # Extract the community answer (from the JSON data)
    script_tag = card.find("script", type="application/json")
    if script_tag:
        voted_answers = json.loads(script_tag.string)
        most_voted_answer = max(voted_answers, key=lambda x: x['vote_count'])['voted_answers']
        question_data['Community Answer'] = most_voted_answer
    
    # Add this question's data to the overall list
    extracted_data.append(question_data)

txt_index = 0

answer_map = {
        'A': 'X1000',
        'B': 'X0100',
        'C': 'X0010',
        'D': 'X0001'
    }



for question in extracted_data:
    #Match the correct answer to the answer map
    testownik_header = str(answer_map[question['Community Answer']])
    with open(f'./testo/{txt_index}.txt', 'w', encoding='utf-8') as file:
        file.write(testownik_header + '\n')
        file.write(question['Text'] + '\n')  # Write the question text
        for choice in question['Choices']:
            file.write(choice + '\n')  # Write each choice on a new line
    txt_index += 1
