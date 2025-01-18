import random
import json
import requests

# Define the topics and their respective facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Diamonds are the hardest known natural material on Earth.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'choices': ['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Argon'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'What is the name of the closest planet to the Sun?',
                'choices': ['Venus', 'Mars', 'Mercury', 'Earth'],
                'answer': 'Mercury'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'choices': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first commercial text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'choices': ['Java', 'C++', 'Python', 'JavaScript'],
                'answer': 'Python'
            },
            {
                'question': 'Which company is known for the development of the Android operating system?',
                'choices': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'choices': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.',
            'The first successful powered flight was achieved by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'choices': ['Egyptians', 'Greeks', 'Romans', 'Mayans'],
                'answer': 'Greeks'
            },
            {
                'question': 'What was the name of the first successful European voyage around the world?',
                'choices': ['Christopher Columbus', 'Magellan', 'Vasco da Gama', 'James Cook'],
                'answer': 'Magellan'
            },
            {
                'question': 'Which event marked the end of World War II in Europe?',
                'choices': ['D-Day', 'Normandy Invasion', 'Battle of Stalingrad', 'V-E Day'],
                'answer': 'V-E Day'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest planet in our solar system?',
                'choices': ['Saturn', 'Jupiter', 'Neptune', 'Uranus'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'choices': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the rarest blood type?',
                'choices': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    return random.choice(topics[topic]['quiz_questions'])

def run_interactive_session():
    """
    Runs the interactive knowledge session.
    """
    print('Welcome to the Interactive Knowledge Session!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()
    if selected_topic not in topics:
        print('Invalid topic. Please try again.')
        return

    print(f'\nYour selected topic is: {selected_topic.capitalize()}')
    print(get_random_fact(selected_topic))
    print('\nNow, let\'s test your knowledge with a quiz!')

    quiz_question = get_quiz_question(selected_topic)
    print(quiz_question['question'])
    for i, choice in enumerate(quiz_question['choices']):
        print(f'{i+1}. {choice}')

    user_answer = input('Enter the number of your answer: ')
    if quiz_question['choices'][int(user_answer) - 1] == quiz_question['answer']:
        print('Correct! You've increased your knowledge.')
    else:
        print(f'Incorrect. The correct answer is: {quiz_question["answer"]}')

    print('\nThank you for participating in the Interactive Knowledge Session!')

run_interactive_session()