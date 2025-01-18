
import random
import requests
import json

# Define topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Function to display a random fact or concept
def display_fact(topic):
    facts = {
        'Science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'A single bolt of lightning can reach temperatures of up to 30,000°C.'
        ],
        'Technology': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first digital camera was developed in 1975 and could only store 0.01 megapixels.',
            'The first commercial internet service provider (ISP) was launched in 1989.'
        ],
        'History': [
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'General Knowledge': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can reach heights of up to 6 meters.',
            'The world's largest desert is Antarctica, which is a desert due to its low precipitation.'
        ]
    }
    
    # Select a random fact from the chosen topic
    fact = random.choice(facts[topic])
    print(f'Did you know that {fact}')

# Function to display a multiple-choice quiz
def quiz(topic):
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 'Au'},
            {'question': 'What is the name of the largest planet in our solar system?', 'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'], 'answer': 'Jupiter'},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'], 'answer': 'Photosynthesis'}
        ],
        'Technology': [
            {'question': 'What is the name of the first programmable computer?', 'options': ['ENIAC', 'UNIVAC', 'IBM 701', 'Apple I'], 'answer': 'ENIAC'},
            {'question': 'What is the name of the programming language created by Guido van Rossum?', 'options': ['Java', 'C++', 'Python', 'Ruby'], 'answer': 'Python'},
            {'question': 'What is the name of the device that converts digital signals into analog signals?', 'options': ['Modem', 'Router', 'Switch', 'Amplifier'], 'answer': 'Modem'}
        ],
        'History': [
            {'question': 'What year was the Declaration of Independence signed?', 'options': ['1776', '1787', '1812', '1861'], 'answer': '1776'},
            {'question': 'Who was the first president of the United States?', 'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'], 'answer': 'George Washington'},
            {'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?', 'options': ['Mesopotamia', 'Indus Valley', 'Sumerian', 'Ancient Egypt'], 'answer': 'Ancient Egypt'}
        ],
        'General Knowledge': [
            {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'], 'answer': 'Pacific Ocean'},
            {'question': 'What is the name of the tallest mountain in the world?', 'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'], 'answer': 'Mount Everest'},
            {'question': 'What is the name of the largest mammal on Earth?', 'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Blue Whale'], 'answer': 'Blue Whale'}
        ]
    }
    
    # Select a random quiz from the chosen topic
    quiz = random.choice(quizzes[topic])
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    # Get user's answer
    user_answer = input('Enter your answer (1-4): ')
    if quiz['options'][int(user_answer)-1] == quiz['answer']:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is {quiz["answer"]}.')

# Main function
def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f"{key}. {value}")
    
    topic_choice = input('Enter your choice (1-4): ')
    
    if topic_choice in topics:
        print(f'You have chosen {topics[topic_choice]}.')
        display_fact(topics[topic_choice])
        quiz(topics[topic_choice])
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
