
import random
import requests
import json

# Define the topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define the facts and quizzes for each topic
facts_and_quizzes = {
    'Science': {
        'facts': [
            'The human body has about 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Diamonds are made of carbon and are the hardest known natural material on Earth.'
        ],
        'quizzes': [
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
                'options': ['Respiration', 'Photosynthesis', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'Technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first programmable computer was the ENIAC, which was completed in 1946.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            }
        ]
    },
    'History': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The American Civil War was fought between 1861 and 1865.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 'Greeks'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            }
        ]
    },
    'General Knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest bone in the human body?',
                'options': ['Femur', 'Tibia', 'Humerus', 'Skull'],
                'answer': 'Femur'
            }
        ]
    }
}

def main():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')

    # Display the topic menu
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')

    # Get the user's topic selection
    topic_choice = input('Enter the number of the topic you want to explore: ')

    if topic_choice in topics:
        topic_name = topics[topic_choice]
        print(f'You've selected the {topic_name} topic.')

        # Display a random fact about the chosen topic
        fact = random.choice(facts_and_quizzes[topic_name]['facts'])
        print(f'\nFact: {fact}')

        # Display a quiz about the chosen topic
        quiz = random.choice(facts_and_quizzes[topic_name]['quizzes'])
        print(f'\nQuiz: {quiz["question"]}')
        for option_id, option in enumerate(quiz['options'], start=1):
            print(f'{option_id}. {option}')

        user_answer = input('Enter the number of the correct answer: ')
        if user_answer == quiz['answer']:
            print('Correct! You're a knowledge champion!')
        else:
            print('Oops, that's not the right answer. Better luck next time!')
    else:
        print('Invalid topic choice. Please try again.')

if __name__ == '__main__':
    main()
