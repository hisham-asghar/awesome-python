import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The Earth is the only planet in our solar system with liquid water on its surface.',
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Neptune', 'Mars'],
                'answer': 0
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 0
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Magnetism', 'Friction', 'Electromagnetism'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The world's first programmable computer was the ENIAC, which was completed in 1946.',
            'The internet was originally called ARPANET, which was developed by the U.S. Department of Defense in the 1960s.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the company that developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful personal computer?',
                'options': ['Apple II', 'IBM PC', 'Commodore 64', 'Atari 800'],
                'answer': 1
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz': [
            {
                'question': 'What year did World War II end?',
                'options': ['1945', '1939', '1941', '1943'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'What ancient civilization built the pyramids in Giza, Egypt?',
                'options': ['Aztecs', 'Incas', 'Mayans', 'Ancient Egyptians'],
                'answer': 3
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.',
            'A group of porcupines is called a prickle.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mammal on Earth?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 1
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
    print(f'Here\'s a random fact about {topic.capitalize()}:')
    print(f'- {fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge with a short quiz!')
    score = 0
    for question in topics[topic]['quiz']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['options'][question['answer']])
    print(f'Your final score is {score} out of {len(topics[topic]["quiz"])}.')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()