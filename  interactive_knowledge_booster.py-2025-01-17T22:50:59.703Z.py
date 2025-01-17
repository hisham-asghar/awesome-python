import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 100 trillion cells.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Bees have five eyes: two compound eyes and three simple eyes.'
        ],
        'quizzes': [
            {
                'question': 'What is the primary function of the human heart?',
                'options': ['To pump blood', 'To filter waste', 'To produce insulin', 'To store oxygen'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 3
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.',
            'The first programmable computer was the ENIAC, completed in 1946.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the purpose of a firewall in computer networks?',
                'options': ['To protect against unauthorized access', 'To increase internet speed', 'To store data', 'To connect devices'],
                'answer': 0
            },
            {
                'question': 'What is the full form of the acronym 'CPU'?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Centralized Processing Unit', 'Computer Primary Unit'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560–2540 BC.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Greek', 'Egyptian', 'Mesopotamian', 'Chinese'],
                'answer': 2
            },
            {
                'question': 'Which famous explorer discovered America in 1492?',
                'options': ['Christopher Columbus', 'Vasco da Gama', 'Marco Polo', 'Ferdinand Magellan'],
                'answer': 0
            },
            {
                'question': 'Which event marked the end of World War II in Europe?',
                'options': ['D-Day', 'V-E Day', 'Pearl Harbor', 'Hiroshima'],
                'answer': 1
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our Solar System?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 1
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 3
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 3
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here\'s a random fact about {topic.capitalize()}:')
    print(f'- {fact}')

def display_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    print(f'Let\'s test your {topic.capitalize()} knowledge!')
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f'{i+1}. {option}')
    user_answer = int(input('Enter your answer (1-4): ')) - 1
    if user_answer == quiz['answer']:
        print('Correct! You know your stuff.')
    else:
        print('Oops, that\'s not the right answer. Better luck next time!')

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == '__main__':
    main()