import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'The first digital computer, the ENIAC, was completed in 1946 and weighed over 30 tons.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Who is credited with the invention of the telephone?',
                'options': ['Alexander Graham Bell', 'Thomas Edison', 'Nikola Tesla', 'Marie Curie'],
                'answer': 'Alexander Graham Bell'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was stolen from the Louvre museum in Paris in 1911 and was missing for two years.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Egyptians', 'Mayans', 'Incas', 'Aztecs'],
                'answer': 'Egyptians'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight by the Wright brothers?',
                'options': ['Kitty Hawk', 'Spirit of St. Louis', 'Wright Flyer', 'Concorde'],
                'answer': 'Wright Flyer'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The world's largest desert is Antarctica, which is a desert due to its low precipitation.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Did you know? {fact}')

def run_quiz(topic):
    score = 0
    questions = topics[topic]['quiz_questions']
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer) - 1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score: {score}/{len(questions)}')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()