def answers_to_binary(possible_answers, correct_answers):
    # Initialize a list of zeros with the same length as possible answers
    binary_representation = ['0'] * len(possible_answers)
    
    # Loop through the possible answers
    for idx, answer in enumerate(possible_answers):
        # If the answer is in the correct answers list, set the corresponding index to '1'
        if answer in correct_answers:
            binary_representation[idx] = '1'
    
    # Join the list into a binary string
    return str("X"+''.join(binary_representation))

if __name__ == '__main__':
    # Example usage:
    possible_answers = ['A', 'B', 'C', 'D']
    correct_answers = ['A',"D"]
    result = answers_to_binary(possible_answers, correct_answers)
    print(result)