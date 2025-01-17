import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body contains around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Sharks have been around for over 400 million years, predating the dinosaurs.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Magnetism', 'Centrifugal force', 'Friction'],
                'answer': 'Gravity'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight, water, and carbon dioxide into oxygen and food?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the region of the Earth's atmosphere where the ozone layer is located?',
                'options': ['Troposphere', 'Stratosphere', 'Mesosphere', 'Thermosphere'],
                'answer': 'Stratosphere'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The first digital camera was invented by Kodak engineer Steven Sasson in 1975.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language that was created by Guido van Rossum in the late 1980s?',
                'options': ['Java', 'C++', 'Python', 'JavaScript'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the wireless communication standard that was first introduced in 1997?',
                'options': ['Bluetooth', 'Wi-Fi', 'Zigbee', '3G'],
                'answer': 'Wi-Fi'
            },
            {
                'question': 'What is the name of the company that created the first commercially successful search engine?',
                'options': ['Microsoft', 'Yahoo', 'Google', 'AltaVista'],
                'answer': 'Google'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.',
            'The Roman Empire lasted for over 400 years, from the 1st century BC to the 5th century AD.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the ancient Greek philosopher who is considered the father of western philosophy?',
                'options': ['Socrates', 'Plato', 'Aristotle', 'Pythagoras'],
                'answer': 'Socrates'
            },
            {
                'question': 'What is the name of the historical event that occurred on July 4, 1776?',
                'options': ['The American Revolution', 'The Declaration of Independence', 'The Civil War', 'The Louisiana Purchase'],
                'answer': 'The Declaration of Independence'
            },
            {
                'question': 'What is the name of the ancient Egyptian queen who was the last active ruler of the Ptolemaic Kingdom?',
                'options': ['Nefertiti', 'Hatshepsut', 'Cleopatra', 'Neferkare'],
                'answer': 'Cleopatra'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest ocean on Earth is the Pacific Ocean, which covers an area of about 63 million square miles.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest continent on Earth by land area?',
                'options': ['Asia', 'Africa', 'North America', 'South America'],
                'answer': 'Asia'
            },
            {
                'question': 'What is the name of the unit used to measure the intensity of earthquakes?',
                'options': ['Richter scale', 'Celsius scale', 'Fahrenheit scale', 'Kelvin scale'],
                'answer': 'Richter scale'
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'],
                'answer': 'Nile River'
            }
        ]
    }
}

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'You selected the {selected_topic.capitalize()} topic.')
        print('Here is a random fact:')
        print(random.choice(topics[selected_topic]['facts']))

        print('\nLet\'s test your knowledge with a quiz!')
        quiz_question = random.choice(topics[selected_topic]['quiz_questions'])
        print(quiz_question['question'])
        for i, option in enumerate(quiz_question['options']):
            print(f"{i+1}. {option}")

        user_answer = input('Enter the number of your answer: ')
        if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
            print('Correct! You're doing great.')
        else:
            print('Oops, that's not the right answer. Better luck next time!')
    else:
        print(f'Sorry, "{selected_topic.capitalize()}" is not a valid topic. Please try again.')

if __name__ == '__main__':
    main()