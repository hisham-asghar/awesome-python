import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Bees can fly higher than Mount Everest.'
        ],
        'quiz': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To digest food', 'To filter toxins'],
                'answer': 0
            },
            {
                'question': 'Which planet has the fastest winds in the solar system?',
                'options': ['Jupiter', 'Saturn', 'Neptune'],
                'answer': 2
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 3
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first self-driving car was developed by Carnegie Mellon University in the 1980s.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first electronic computer?',
                'options': ['ENIAC', 'UNIVAC', 'Apple I'],
                'answer': 0
            },
            {
                'question': 'When was the first commercial computer delivered?',
                'options': ['1951', '1975', '1984'],
                'answer': 0
            },
            {
                'question': 'Which university developed the first self-driving car?',
                'options': ['MIT', 'Stanford', 'Carnegie Mellon'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization built the Great Pyramid of Giza?',
                'options': ['Egyptian', 'Mesopotamian', 'Aztec'],
                'answer': 0
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'options': ['Michelangelo', 'Leonardo da Vinci', 'Vincent van Gogh'],
                'answer': 1
            },
            {
                'question': 'How long did the Roman Empire last?',
                'options': ['200 years', '400 years', '800 years'],
                'answer': 1
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quiz': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Brain', 'Heart', 'Skin'],
                'answer': 2
            },
            {
                'question': 'What is the tallest mammal?',
                'options': ['Elephant', 'Giraffe', 'Moose'],
                'answer': 1
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 2
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here\'s a fact about {topic.capitalize()}:\n{fact}')

def run_quiz(topic):
    score = 0
    for question in topics[topic]['quiz']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-3): ')) - 1
        if user_answer == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['options'][question['answer']])
    print(f'Your final score is {score}/{len(topics[topic]["quiz"])}')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()