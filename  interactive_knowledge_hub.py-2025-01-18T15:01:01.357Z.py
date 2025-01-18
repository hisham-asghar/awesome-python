import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest organ in the human body is the skin.',
            'The human brain has around 100 billion neurons.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Magnetism', 'Friction', 'Electromagnetism'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.',
            'The first smartphone was the IBM Simon, released in 1992.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals?',
                'options': ['Modem', 'Router', 'Switch', 'Amplifier'],
                'answer': 'Modem'
            },
            {
                'question': 'What is the name of the process by which a computer executes a series of instructions?',
                'options': ['Compilation', 'Interpretation', 'Execution', 'Debugging'],
                'answer': 'Execution'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient civilization that built the Colosseum in Rome?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mesopotamian'],
                'answer': 'Roman'
            },
            {
                'question': 'What was the name of the war that lasted from 1939 to 1945?',
                'options': ['World War I', 'World War II', 'Vietnam War', 'Korean War'],
                'answer': 'World War II'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest continent in the world is Asia.',
            'The tallest mammal in the world is the giraffe.',
            'The largest ocean in the world is the Pacific Ocean.'
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
                'question': 'What is the name of the musical instrument with strings that is played by plucking?',
                'options': ['Piano', 'Violin', 'Guitar', 'Drums'],
                'answer': 'Guitar'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Hub!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')
    print('- Exit')

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here\'s a random fact about {topic.capitalize()}:')
    print(f'- {fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge with a quiz!')
    score = 0
    for question in topics[topic]['quiz_questions']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer) - 1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score is {score} out of {len(topics[topic]["quiz_questions"])}.')

def main():
    while True:
        display_menu()
        user_input = input('Enter your choice: ').lower()
        if user_input == 'exit':
            print('Goodbye!')
            break
        elif user_input in topics:
            display_fact(user_input)
            run_quiz(user_input)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()