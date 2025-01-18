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
            'fact': 'The Earth is the only planet in our solar system with liquid water on its surface.',
            'quiz': {
                'question': 'What percentage of the Earth\'s surface is covered by water?',
                'options': ['50%', '70%', '90%', '97%'],
                'answer': '97%'
            }
        },
        {
            'fact': 'The human body is composed of around 60% water.',
            'quiz': {
                'question': 'Which organ in the human body is responsible for filtering waste and excess water from the blood?',
                'options': ['Liver', 'Kidneys', 'Heart', 'Lungs'],
                'answer': 'Kidneys'
            }
        }
    ],
    'Technology': [
        {
            'fact': 'The first electronic computer, ENIAC, was developed in 1946 and weighed over 30 tons.',
            'quiz': {
                'question': 'What was the name of the first programmable, general-purpose electronic computer?',
                'options': ['UNIVAC', 'ENIAC', 'MARK I', 'COLOSSUS'],
                'answer': 'ENIAC'
            }
        },
        {
            'fact': 'The World Wide Web was invented by Tim Berners-Lee in 1989.',
            'quiz': {
                'question': 'What year was the first web page published?',
                'options': ['1989', '1991', '1993', '1995'],
                'answer': '1991'
            }
        }
    ],
    'History': [
        {
            'fact': 'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'quiz': {
                'question': 'Approximately how many years ago were the Great Pyramids of Giza built?',
                'options': ['2,500 years ago', '4,500 years ago', '6,500 years ago', '8,500 years ago'],
                'answer': '4,500 years ago'
            }
        },
        {
            'fact': 'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'quiz': {
                'question': 'Which Roman emperor is known for his brutal persecution of early Christians?',
                'options': ['Augustus', 'Nero', 'Trajan', 'Hadrian'],
                'answer': 'Nero'
            }
        }
    ],
    'General Knowledge': [
        {
            'fact': 'The largest ocean on Earth is the Pacific Ocean.',
            'quiz': {
                'question': 'What is the name of the smallest ocean on Earth?',
                'options': ['Arctic Ocean', 'Indian Ocean', 'Atlantic Ocean', 'Southern Ocean'],
                'answer': 'Arctic Ocean'
            }
        },
        {
            'fact': 'The tallest mammal on Earth is the giraffe.',
            'quiz': {
                'question': 'What is the largest land animal on Earth?',
                'options': ['African Elephant', 'Hippopotamus', 'White Rhinoceros', 'Giraffe'],
                'answer': 'African Elephant'
            }
        }
    ]
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
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

    user_answer = input('Enter your answer (1-4): ')
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is {quiz["answer"]}.')

def main():
    display_menu()
    topic_choice = input('Enter the number of the topic you want to explore: ')
    topic = topics[topic_choice]
    print(f'You have chosen the topic of {topic}.')

    fact, quiz = get_random_fact_and_quiz(topic)
    print(f'Here is a random fact about {topic.lower()}: {fact}')
    run_quiz(quiz)

if __name__ == '__main__':
    main()