
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the selected topic using a public API or predefined database."""
    # Replace this with your actual API call or database lookup
    facts = {
        'science': ['The human body has around 60,000 miles of blood vessels.', 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'],
        'technology': ['The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.', 'The first commercial microprocessor was the Intel 4004, released in 1971.'],
        'history': ['The Great Wall of China is the only man-made structure visible from space.', 'The Roman Colosseum could hold up to 80,000 spectators.'],
        'general': ['A group of porcupines is called a prickle.', 'The first product to have a barcode was Wrigley's gum.']
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """Generate a multiple-choice quiz question for the selected topic."""
    # Replace this with your actual quiz questions and answers
    quiz_data = {
        'science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 'Jupiter'
            }
        ],
        'technology': [
            {
                'question': 'What does the acronym "CPU" stand for?',
                'options': ['Computer Processing Unit', 'Central Processing Unit', 'Computer Power Unit', 'Central Power Unit'],
                'answer': 'Central Processing Unit'
            },
            {
                'question': 'Which company developed the first commercial microprocessor?',
                'options': ['Intel', 'IBM', 'Apple', 'Microsoft'],
                'answer': 'Intel'
            }
        ],
        'history': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            }
        ],
        'general': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
    return random.choice(quiz_data[topic])

def main():
    """Main function to run the interactive knowledge-building script."""
    print('Welcome to the Interactive Knowledge-Building Script!')
    print('Please select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General Knowledge')

    topic_choice = input('Enter the number of your choice (1-4): ')

    if topic_choice == '1':
        topic = 'science'
    elif topic_choice == '2':
        topic = 'technology'
    elif topic_choice == '3':
        topic = 'history'
    elif topic_choice == '4':
        topic = 'general'
    else:
        print('Invalid choice. Exiting the script.')
        return

    print(f'\nYour chosen topic is: {topic.capitalize()}')
    print(f'Random fact: {get_random_fact(topic)}')

    quiz_info = quiz_question(topic)
    print(f'\nMultiple-choice quiz question:')
    print(quiz_info['question'])
    for i, option in enumerate(quiz_info['options'], start=1):
        print(f'{i}. {option}')

    user_answer = input('Enter the number of your answer (1-4): ')
    if user_answer == str(quiz_info['options'].index(quiz_info['answer']) + 1):
        print('Correct! You've increased your knowledge.')
    else:
        print('Incorrect. The correct answer is:', quiz_info['answer'])

if __name__ == '__main__':
    main()
