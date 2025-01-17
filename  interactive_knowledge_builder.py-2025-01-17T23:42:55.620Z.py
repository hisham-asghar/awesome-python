Here is the raw Python code without any additional commentary:

import random
import requests
import json

def get_random_fact(topic):
    facts = {
        'science': ['The human body has around 60,000 miles of blood vessels.', 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'],
        'technology': ['The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.', 'The first commercial microprocessor was the Intel 4004, released in 1971.'],
        'history': ['The Great Wall of China is the only man-made structure visible from space.', 'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.'],
        'general': ['A group of porcupines is called a prickle.', 'The first product to have a barcode was Wrigley's gum.']
    }
    return random.choice(facts[topic])

def display_fact(topic):
    fact = get_random_fact(topic)
    print(f'Did you know that {fact}')

def quiz_question(topic):
    questions = {
        'science': {
            'question': 'What is the chemical symbol for gold?',
            'options': ['Au', 'Ag', 'Cu', 'Fe'],
            'answer': 0
        },
        'technology': {
            'question': 'What is the name of the first commercially successful web browser?',
            'options': ['Mozilla', 'Internet Explorer', 'Netscape Navigator', 'Safari'],
            'answer': 2
        },
        'history': {
            'question': 'Which ancient civilization built the pyramids?',
            'options': ['Romans', 'Greeks', 'Egyptians', 'Mayans'],
            'answer': 2
        },
        'general': {
            'question': 'What is the largest organ in the human body?',
            'options': ['Heart', 'Liver', 'Skin', 'Brain'],
            'answer': 2
        }
    }
    return questions[topic]

def run_quiz(topic):
    quiz = quiz_question(topic)
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f'{i+1}. {option}')
    
    user_answer = int(input('Enter your answer (1-4): '))
    if user_answer - 1 == quiz['answer']:
        print('Correct!')
    else:
        print('Incorrect. Better luck next time!')

def main():
    print('Welcome to the Interactive Knowledge Builder!')
    print('Select a topic:')
    topics = ['Science', 'Technology', 'History', 'General']
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic}')
    
    topic_choice = int(input('Enter your choice (1-4): ')) - 1
    selected_topic = topics[topic_choice].lower()
    
    display_fact(selected_topic)
    run_quiz(selected_topic)

if __name__ == '__main__':
    main()