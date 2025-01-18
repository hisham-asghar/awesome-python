import random
import requests
import json

# Define topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Bioluminescence is the production and emission of light by a living organism.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            },
            {
                'question': 'Which scientist is famous for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
                'answer': 1
            },
            {
                'question': 'What is the chemical symbol for the element gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Brain\", was created in 1986.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The world's first website was launched in 1991 by Tim Berners-Lee.'
        ],
        'quiz': [
            {
                'question': 'What does the term \"CPU\" stand for?',
                'options': ['Central Processing Unit', 'Computer Processing Unit', 'Compact Processing Unit', 'Central Power Unit'],
                'answer': 0
            },
            {
                'question': 'Which company is known for creating the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Internet Explorer', 'Netscape Navigator', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 1
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramids of Giza were built around 2560-2540 BCE.',
            'The Roman Empire lasted for over 400 years, from 27 BCE to 476 CE.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for their advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 1
            },
            {
                'question': 'What was the name of the first successful American space mission?',
                'options': ['Apollo 11', 'Gemini 3', 'Mercury-Redstone 3', 'Sputnik 1'],
                'answer': 2
            },
            {
                'question': 'Which event is considered the start of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Sinking of the Lusitania', 'Battle of the Somme', 'Zimmermann Telegram'],
                'answer': 0
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).',
            'The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.'
        ],
        'quiz': [
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'Which country is known as the \"Land of the Rising Sun\"?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 1
            },
            {
                'question': 'What is the largest continent in the world by land area?',
                'options': ['Asia', 'Africa', 'North America', 'South America'],
                'answer': 0
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
    print(f'Did you know? {fact}')

def run_quiz(topic):
    score = 0
    for question in topics[topic]['quiz']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): ')) - 1
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