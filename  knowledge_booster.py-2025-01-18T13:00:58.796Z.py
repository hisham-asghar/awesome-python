import random
import requests
from collections import namedtuple

# Define a named tuple to store topic information
Topic = namedtuple('Topic', ['name', 'description', 'questions'])

# Define the topics and their corresponding questions
topics = [
    Topic(
        name='Science',
        description='Explore the fascinating world of science!',
        questions=[
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'options': ['Photosynthesis', 'Respiration', 'Combustion', 'Evaporation'],
                'answer': 0
            },
            {
                'question': 'Which element is the most abundant in the Earth\'s crust?',
                'options': ['Oxygen', 'Silicon', 'Aluminum', 'Iron'],
                'answer': 0
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 0
            }
        ]
    ),
    Topic(
        name='Technology',
        description='Discover the latest advancements in technology!',
        questions=[
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the device that converts digital signals into sound?',
                'options': ['Modem', 'Router', 'Speakers', 'Microphone'],
                'answer': 2
            }
        ]
    ),
    Topic(
        name='History',
        description='Explore the rich tapestry of human history!',
        questions=[
            {
                'question': 'In what year did the United States declare its independence?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 2
            },
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Mesopotamia', 'Aztec', 'Egyptian', 'Greek'],
                'answer': 2
            }
        ]
    ),
    Topic(
        name='General Knowledge',
        description='Test your knowledge on a wide range of topics!',
        questions=[
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            }
        ]
    )
]

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic.name}')
    print('0. Exit')

def display_fact(topic):
    print(f'\n{topic.description}')
    print(f'Random fact: {random.choice(topic.questions)["question"]}')

def quiz(topic):
    print(f'\nTime to test your {topic.name} knowledge!')
    score = 0
    for question in topic.questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer == question['answer'] + 1:
            print('Correct!')
            score += 1
        else:
            print('Incorrect.')
    print(f'Your final score: {score}/{len(topic.questions)}')

def main():
    while True:
        display_menu()
        choice = int(input('Enter your choice (0-4): '))
        if choice == 0:
            print('Goodbye!')
            break
        elif 1 <= choice <= len(topics):
            topic = topics[choice - 1]
            display_fact(topic)
            quiz(topic)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()