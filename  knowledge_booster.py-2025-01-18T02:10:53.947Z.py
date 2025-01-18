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
                'question': 'What is the approximate length of the human blood vessels?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '90,000 miles'],
                'answer': '60,000 miles'
            }
        },
        # Add more science facts and quizzes here
    ],
    'Technology': [
        {
            'fact': 'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'quiz': {
                'question': 'What was the weight of the first electronic computer, ENIAC?',
                'options': ['10 tons', '20 tons', '30 tons', '40 tons'],
                'answer': '30 tons'
            }
        },
        # Add more technology facts and quizzes here
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
        # Add more history facts and quizzes here
    ],
    'General Knowledge': [
        {
            'fact': 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'quiz': {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['It was the fashion in Renaissance Florence to shave them off',
                           'She was born without eyebrows',
                           'The painting was damaged over time',
                           'The artist intentionally left them out'],
                'answer': 'It was the fashion in Renaissance Florence to shave them off'
            }
        },
        # Add more general knowledge facts and quizzes here
    ]
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')

def get_random_fact(topic):
    fact_and_quiz = random.choice(facts_and_quizzes[topic])
    return fact_and_quiz['fact']

def run_quiz(topic):
    fact_and_quiz = random.choice(facts_and_quizzes[topic])
    quiz = fact_and_quiz['quiz']
    print(quiz['question'])
    for option in quiz['options']:
        print(f'- {option}')
    user_answer = input('Enter your answer: ')
    if user_answer.lower() == quiz['answer'].lower():
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is: {quiz["answer"]}')

def main():
    display_menu()
    topic_id = input('Enter the topic number: ')
    if topic_id in topics:
        topic = topics[topic_id]
        print(f'You have selected: {topic}')
        print(get_random_fact(topic))
        run_quiz(topic)
    else:
        print('Invalid topic number. Please try again.')

if __name__ == '__main__':
    main()