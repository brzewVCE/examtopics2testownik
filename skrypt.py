from bs4 import BeautifulSoup
import json


# Path to the HTML file
file_path = 'D:/Buena/Cert1/0.html'
# Sample HTML content as a string (substitute this with your actual HTML file content)
with open(file_path, 'r', encoding='utf-8') as file:
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
    
    # Extract the correct answer (from hidden correct-answer span)
    correct_answer_tag = card.find("span", class_="correct-answer")
    if correct_answer_tag:
        question_data['Correct Answer'] = correct_answer_tag.get_text(strip=True)
    
    
    # Add this question's data to the overall list
    extracted_data.append(question_data)

txt_index = 0
# Output extracted data
for question in extracted_data:
    string = question['Text']+'\n'+str(question['Choices'])+'\n\n'
    with open(f'{txt_index}.txt', 'a') as f:
        json.dump(extracted_data, f, indent=4)
    #print(question['Text'])
    print(question['Choices'])
    print()

# Optionally, you can save this data to a JSON file
import json
with open('extracted_questions.json', 'w') as f:
    json.dump(extracted_data, f, indent=4)
