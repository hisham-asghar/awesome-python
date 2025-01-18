
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
    'Science': [
        {
            'fact': 'The human body contains around 60,000 miles of blood vessels.',
            'quiz': {
                'question': 'How many miles of blood vessels are in the human body?',
                'options': ['30,000', '60,000', '90,000', '120,000'],
                'answer': '60,000'
            }
        },
        {
            'fact': 'The Earth is the only planet in our solar system with liquid water on its surface.',
            'quiz': {
                'question': 'Which planet in our solar system is the only one with liquid water on its surface?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Earth'],
                'answer': 'Earth'
            }
        }
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
        {
            'fact': 'The first commercial smartphone, the IBM Simon, was released in 1992.',
            'quiz': {
                'question': 'In what year was the first commercial smartphone, the IBM Simon, released?',
                'options': ['1985', '1992', '1998', '2002'],
                'answer': '1992'
            }
        }
    ],
    'History': [
        {
            'fact': 'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'quiz': {
                'question': 'How long is the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            }
        },
        {
            'fact': 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'quiz': {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['It was the fashion in Renaissance Florence to shave them off', 'She was painted without eyebrows', 'The painting was damaged over time', 'The artist forgot to paint them'],
                'answer': 'It was the fashion in Renaissance Florence to shave them off'
            }
        }
    ],
    'General Knowledge': [
        {
            'fact': 'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands and raises the structure.',
            'quiz': {
                'question': 'How much taller can the Eiffel Tower get during the summer?',
                'options': ['5 cm', '10 cm', '15 cm', '20 cm'],
                'answer': '15 cm'
            }
        },
        {
            'fact': 'A group of porcupines is called a prickle.',
            'quiz': {
                'question': 'What is a group of porcupines called?',
                'options': ['a quill', 'a spike', 'a prickle', 'a quiver'],
                'answer': 'a prickle'
            }
        }
    ]
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    topic_choice = input('Enter the number of the topic you want to explore: ')
    return topic_choice

def display_fact_and_quiz(topic_choice):
    topic = topics[topic_choice]
    fact_and_quiz = random.choice(facts_and_quizzes[topic])
    print(f'Here is a fact about {topic}:')
    print(fact_and_quiz['fact'])
    print()
    print('Now, let\'s test your knowledge with a quiz!')
    quiz = fact_and_quiz['quiz']
    print(quiz['question'])
    for option in quiz['options']:
        print(f'- {option}')
    user_answer = input('Enter your answer: ')
    if user_answer.lower() == quiz['answer'].lower():
        print('Correct! You're doing great.')
    else:
        print(f'Incorrect. The correct answer is {quiz["answer"]}.')

def main():
    topic_choice = display_menu()
    display_fact_and_quiz(topic_choice)

if __name__ == '__main__':
    main()
