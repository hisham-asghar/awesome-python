import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Bioluminescence is the production and emission of light by a living organism.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was created in 1983 and was called the 'Brain' virus.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The internet was originally called ARPANET and was developed by the US Department of Defense.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company is known for creating the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Mozilla Firefox', 'Google Chrome', 'Internet Explorer', 'Netscape Navigator'],
                'answer': 'Netscape Navigator'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The ancient Egyptians were the first civilization to invent the calendar.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz': [
            {
                'question': 'In what year was the United States of America founded?',
                'options': ['1776', '1789', '1492', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mayan'],
                'answer': 'Egyptian'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Biplane', 'The Glider', 'The Zeppelin'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest mammal in the world is the giraffe.',
            'The largest known snowflake was 15 inches wide, reported in Montana in 1887.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Io'],
                'answer': 'Titan'
            },
            {
                'question': 'What is the name of the largest desert in the world?',
                'options': ['Sahara Desert', 'Antarctic Desert', 'Gobi Desert', 'Arabian Desert'],
                'answer': 'Antarctic Desert'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def main():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'\nHere\'s a random fact about {selected_topic.capitalize()}:')
        print(get_random_fact(selected_topic))

        print('\nLet\'s test your knowledge with a quiz!')
        quiz_question = get_quiz_question(selected_topic)
        print(quiz_question['question'])
        for i, option in enumerate(quiz_question['options']):
            print(f"{i+1}. {option}")

        user_answer = input('Enter the number of your answer: ')
        if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
            print('Correct! You're a knowledge champion!')
        else:
            print('Oops, that\'s not the right answer. Better luck next time!')
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()