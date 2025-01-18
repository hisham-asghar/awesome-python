import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2021 has 23 million digits.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The world's first text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the search engine founded by Larry Page and Sergey Brin?',
                'options': ['Bing', 'Yahoo', 'Google', 'DuckDuckGo'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the company that created the first commercially successful personal computer?',
                'options': ['Apple', 'Microsoft', 'IBM', 'Commodore'],
                'answer': 'IBM'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in Olympia, Greece, in 776 BC.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz_questions': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1787', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['Mesopotamian', 'Sumerian', 'Phoenician', 'Egyptian'],
                'answer': 'Egyptian'
            }
        ]
    },
    'general': {
        'facts': [
            'The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A group of porcupines is called a prickle.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Europa'],
                'answer': 'Titan'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Fun fact about {topic.capitalize()}: {fact}')

def quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge!')
    score = 0
    for question in topics[topic]['quiz_questions']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer)-1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score is {score}/{len(topics[topic]["quiz_questions"])}')

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == '__main__':
    main()