import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The internet was originally called ARPANET and was created in 1969 by the U.S. Department of Defense.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What does "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Machine Language', 'Hyper Text Modeling Language'],
                'answer': 'Hyper Text Markup Language'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The Renaissance was a period of European cultural, artistic, political, and economic "rebirth" that lasted from the 14th to the 17th century.'
        ],
        'quiz': [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1775', '1914'],
                'answer': '1861'
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 'Greeks'
            },
            {
                'question': 'What was the name of the first successful powered flight made by the Wright brothers?',
                'options': ['Flyer I', 'Spirit of St. Louis', 'Kitty Hawk', 'Wright Flyer'],
                'answer': 'Wright Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) in height.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 21,000 kilometers (13,000 miles).'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'India', 'South Korea'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 'Mount Everest'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Fun Fact: {fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge!')
    score = 0
    for question in topics[topic]['quiz']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer)-1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score is {score} out of {len(topics[topic]["quiz"])}.')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()