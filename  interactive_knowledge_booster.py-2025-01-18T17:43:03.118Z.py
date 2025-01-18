
import random
import requests
import json

# Define the topics and their respective facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number has over 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To produce oxygen', 'To filter waste', 'To store energy'],
                'answer': 'To pump blood'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial computer, UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first microprocessor, the Intel 4004, was released in 1971.'
        ],
        'quizzes': [
            {
                'question': 'What does "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Central Power Unit', 'Computer Processing Unit'],
                'answer': 'Central Processing Unit'
            },
            {
                'question': 'Which company is known for creating the first personal computer?',
                'options': ['Apple', 'Microsoft', 'IBM', 'Google'],
                'answer': 'IBM'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Silk Road was an ancient network of trade routes that connected the East and West from the 2nd century BCE to the 18th century CE.',
            'The Renaissance was a period of European cultural, artistic, political, and economic "rebirth" from the 14th to the 17th century.'
        ],
        'quizzes': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplane', 'The Monoplane'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'Who wrote the novel "To Kill a Mockingbird"?',
                'options': ['Harper Lee', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Maya Angelou'],
                'answer': 'Harper Lee'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')
    print('- Quit')

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here\'s a random fact about {topic.capitalize()}:\n{fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge!')
    score = 0
    for quiz in topics[topic]['quizzes']:
        print(quiz['question'])
        for i, option in enumerate(quiz['options']):
            print(f'{i+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if quiz['options'][int(user_answer) - 1] == quiz['answer']:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect. The correct answer is {quiz["answer"]}.')
    print(f'Your final score is {score}/{len(topics[topic]["quizzes"])}')

def main():
    while True:
        display_menu()
        choice = input('Enter your choice: ').lower()
        if choice == 'quit':
            print('Goodbye!')
            break
        elif choice in topics:
            display_fact(choice)
            run_quiz(choice)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
