import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'Which of the following is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 'Plasma'
            },
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Friction', 'Centrifugal force', 'Electromagnetic force'],
                'answer': 'Gravity'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real moth trapped in a Harvard Mark II computer.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The word 'byte' was coined in 1956, and originally referred to a group of 2 bits.'
        ],
        'quiz': [
            {
                'question': 'What does "GUI" stand for?',
                'options': ['Graphical User Interface', 'General User Interface', 'Graphic User Interaction', 'Graphical Universal Interface'],
                'answer': 'Graphical User Interface'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight lasted only 12 seconds and covered 120 feet.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Greeks', 'Romans', 'Egyptians', 'Mayans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'What was the name of the first successful powered aircraft?',
                'options': ['Kitty Hawk', 'Wright Flyer', 'Fokker Triplane', 'Sopwith Camel'],
                'answer': 'Wright Flyer'
            },
            {
                'question': 'Which country was the first to grant women the right to vote?',
                'options': ['United States', 'United Kingdom', 'New Zealand', 'France'],
                'answer': 'New Zealand'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The first commercial barcode scanner was installed in a Marsh supermarket in Ohio in 1974.'
        ],
        'quiz': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'South Korea', 'Taiwan'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]['quiz']
    question = random.choice(quiz_questions)
    return question['question'], question['options'], question['answer']

def main():
    """
    The main function that runs the interactive knowledge booster.
    """
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'\nYour selected topic is: {selected_topic.capitalize()}')
        print(f'Here is a random fact about {selected_topic}:')
        print(get_random_fact(selected_topic))

        print('\nLet\'s test your knowledge with a quiz!')
        question, options, answer = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f'{i+1}. {option}')

        user_answer = input('Enter the number of your answer: ')
        if options[int(user_answer) - 1] == answer:
            print('Correct! You're a knowledge master.')
        else:
            print(f'Incorrect. The correct answer is: {answer}')
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()