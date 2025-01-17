import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            },
            {
                'question': 'What is the chemical symbol for the element gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first iPhone was released in 2007 and had a 3.5-inch screen.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first web browser, created by Tim Berners-Lee?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Google Chrome', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            },
            {
                'question': 'What is the name of the company that created the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa was stolen from the Louvre in 1911 and not recovered for two years.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'What year did the American Revolutionary War begin?',
                'options': ['1776', '1812', '1861', '1917'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful voyage around the world?',
                'options': ['The Mayflower', 'The Santa Maria', 'The Beagle', 'The Magellan Expedition'],
                'answer': 'The Magellan Expedition'
            }
        ]
    },
    'general': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the tallest mammal?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    question_data = random.choice(topics[topic]['quiz_questions'])
    return question_data['question'], question_data['options'], question_data['answer']

def run_quiz(topic):
    score = 0
    for i in range(3):
        question, options, answer = get_quiz_question(topic)
        print(f'Question {i+1}: {question}')
        for j, option in enumerate(options):
            print(f'{j+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if options[int(user_answer)-1] == answer:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect. The correct answer is: {answer}')
    print(f'Your final score is {score}/3.')

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'Here is a random fact about {selected_topic.capitalize()}:')
        print(get_random_fact(selected_topic))
        print('\nNow, let\'s test your knowledge with a quiz!')
        run_quiz(selected_topic)
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()