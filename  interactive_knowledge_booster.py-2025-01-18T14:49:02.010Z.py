import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Bees can fly higher than the tallest building.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Condensation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 'Plasma'
            },
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Friction', 'Centrifugal force', 'Electromagnetic force'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first programmable computer was the ENIAC, which was completed in 1946.',
            'The internet was originally called ARPANET, and was created by the US Department of Defense.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language that was developed by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which of these is not a type of computer memory?',
                'options': ['RAM', 'ROM', 'CPU', 'SSD'],
                'answer': 'CPU'
            },
            {
                'question': 'What is the name of the first commercial web browser?',
                'options': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'Google Chrome'],
                'answer': 'Mosaic'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza were built around 2560-2540 BC, and are the oldest and largest of the three main pyramids.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 'Mayans'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event marked the end of World War II in Europe?',
                'options': ['D-Day', 'The Battle of Stalingrad', 'The bombing of Hiroshima and Nagasaki', 'The fall of Berlin'],
                'answer': 'The fall of Berlin'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters tall.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the largest bone in the human body?',
                'options': ['Femur', 'Tibia', 'Humerus', 'Skull'],
                'answer': 'Femur'
            },
            {
                'question': 'What is the name of the largest river in the world?',
                'options': ['Amazon', 'Nile', 'Mississippi', 'Yangtze'],
                'answer': 'Nile'
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
    print(f'Did you know that {fact}')

def run_quiz(topic):
    score = 0
    for question in topics[topic]['quiz_questions']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer)-1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score is {score} out of {len(topics[topic]["quiz_questions"])}')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()