import random
import requests
import json

# Define the available topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define the facts and quiz questions for each topic
facts_and_quizzes = {
    'Science': [
        {
            'fact': 'The human body has around 60,000 miles of blood vessels.',
            'quiz': {
                'question': 'What is the approximate length of the human body\'s blood vessels?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '90,000 miles'],
                'answer': '60,000 miles'
            }
        },
        {
            'fact': 'The first product to have a barcode was Wrigley's gum.',
            'quiz': {
                'question': 'What was the first product to have a barcode?',
                'options': ['Coca-Cola', 'Wrigley's gum', 'Bread', 'Milk'],
                'answer': 'Wrigley's gum'
            }
        }
    ],
    'Technology': [
        {
            'fact': 'The first computer mouse was invented in 1964 and cost $15.',
            'quiz': {
                'question': 'When was the first computer mouse invented?',
                'options': ['1950', '1964', '1980', '1990'],
                'answer': '1964'
            }
        },
        {
            'fact': 'The first text message was sent in 1992 and said "Merry Christmas".',
            'quiz': {
                'question': 'What was the first text message sent?',
                'options': ['Hello, world!', 'Merry Christmas', 'How are you?', 'I love you'],
                'answer': 'Merry Christmas'
            }
        }
    ],
    'History': [
        {
            'fact': 'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'quiz': {
                'question': 'What is the approximate length of the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            }
        },
        {
            'fact': 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'quiz': {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['It was the fashion in Renaissance Florence to shave them off', 'The painting was damaged over time', 'The artist forgot to paint them', 'It was a stylistic choice'],
                'answer': 'It was the fashion in Renaissance Florence to shave them off'
            }
        }
    ],
    'General Knowledge': [
        {
            'fact': 'A group of porcupines is called a prickle.',
            'quiz': {
                'question': 'What is a group of porcupines called?',
                'options': ['A quill', 'A prickle', 'A spike', 'A quiver'],
                'answer': 'A prickle'
            }
        },
        {
            'fact': 'The first product to have a barcode was Wrigley's gum.',
            'quiz': {
                'question': 'What was the first product to have a barcode?',
                'options': ['Coca-Cola', 'Wrigley's gum', 'Bread', 'Milk'],
                'answer': 'Wrigley's gum'
            }
        }
    ]
}

def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')

def get_random_fact_and_quiz(topic):
    fact_and_quiz = random.choice(facts_and_quizzes[topic])
    return fact_and_quiz['fact'], fact_and_quiz['quiz']

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options'], start=1):
        print(f'{i}. {option}')

    while True:
        user_answer = input('Enter your answer (1-4): ')
        if user_answer in ['1', '2', '3', '4']:
            if quiz['options'][int(user_answer) - 1] == quiz['answer']:
                print('Correct!')
                return True
            else:
                print('Incorrect. Please try again.')
        else:
            print('Invalid input. Please enter a number from 1 to 4.')

def main():
    display_menu()
    topic_id = input('Enter the topic number: ')
    if topic_id in topics:
        topic = topics[topic_id]
        fact, quiz = get_random_fact_and_quiz(topic)
        print(f'\nFact about {topic}: {fact}')
        if run_quiz(quiz):
            print('Congratulations, you got the answer right!')
        else:
            print(f'The correct answer is: {quiz["answer"]}')
    else:
        print('Invalid topic number. Please try again.')

if __name__ == '__main__':
    main()