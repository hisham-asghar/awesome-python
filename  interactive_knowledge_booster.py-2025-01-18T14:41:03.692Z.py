
import random
import requests
import json

# List of topics
topics = ['Science', 'Technology', 'History', 'General Knowledge']

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic}')
    
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            if 1 <= choice <= len(topics):
                return choice - 1
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_index):
    # Fetch data from a public API or a predefined database
    # (replace the placeholder with your actual data source)
    facts = {
        'Science': ['The human body has around 60,000 miles of blood vessels.', 'The hottest planet in the Solar System is Venus.', 'The largest known prime number has over 23 million digits.'],
        'Technology': ['The first computer mouse was invented in 1964.', 'The first smartphone was the IBM Simon, released in 1992.', 'The World Wide Web was invented by Tim Berners-Lee in 1989.'],
        'History': ['The Great Wall of China is the longest man-made structure in the world.', 'The Pyramids of Giza were built around 2560-2540 BC.', 'The Roman Empire lasted for over 400 years.'],
        'General Knowledge': ['The largest ocean on Earth is the Pacific Ocean.', 'The tallest mammal is the giraffe.', 'The largest continent by land area is Asia.']
    }
    
    return random.choice(facts[topics[topic_index]])

# Function to display a quiz for the selected topic
def quiz(topic_index):
    # Fetch quiz questions and answers from a public API or a predefined database
    # (replace the placeholder with your actual data source)
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 0},
            {'question': 'What is the largest planet in our solar system?', 'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'], 'answer': 1},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'options': ['Respiration', 'Photosynthesis', 'Evaporation', 'Combustion'], 'answer': 1}
        ],
        'Technology': [
            {'question': 'What is the name of the first commercially successful web browser?', 'options': ['Internet Explorer', 'Mozilla Firefox', 'Google Chrome', 'Netscape Navigator'], 'answer': 3},
            {'question': 'What is the name of the operating system developed by Apple?', 'options': ['Windows', 'Linux', 'macOS', 'Android'], 'answer': 2},
            {'question': 'What is the name of the programming language used to build websites?', 'options': ['Java', 'Python', 'C++', 'HTML'], 'answer': 3}
        ],
        'History': [
            {'question': 'What year was the Declaration of Independence signed?', 'options': ['1776', '1789', '1812', '1865'], 'answer': 0},
            {'question': 'What was the name of the first successful powered flight?', 'options': ['Wright Flyer', 'Spitfire', 'Concorde', 'Apollo 11'], 'answer': 0},
            {'question': 'What was the name of the ancient Egyptian civilization?', 'options': ['Mesopotamia', 'Aztec', 'Inca', 'Pharaonic'], 'answer': 3}
        ],
        'General Knowledge': [
            {'question': 'What is the largest organ in the human body?', 'options': ['Heart', 'Brain', 'Liver', 'Skin'], 'answer': 3},
            {'question': 'What is the capital city of Australia?', 'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'answer': 3},
            {'question': 'What is the name of the largest mammal in the world?', 'options': ['Elephant', 'Whale', 'Hippopotamus', 'Giraffe'], 'answer': 1}
        ]
    }
    
    quiz_questions = quizzes[topics[topic_index]]
    score = 0
    
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                user_answer = int(input('Enter your answer (1-4): '))
                if 1 <= user_answer <= len(question['options']):
                    if user_answer - 1 == question['answer']:
                        print('Correct!')
                        score += 1
                    else:
                        print('Incorrect. Try again.')
                    break
                else:
                    print('Invalid choice. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')
    
    print(f'Your final score is {score} out of {len(quiz_questions)}.')

# Main program loop
while True:
    topic_index = display_menu()
    print(f'\nRandom fact about {topics[topic_index]}: {get_random_fact(topic_index)}')
    print('\nLet\'s test your knowledge with a quiz!')
    quiz(topic_index)
    
    continue_prompt = input('\nDo you want to try another topic? (y/n) ')
    if continue_prompt.lower() != 'y':
        print('Thank you for using the Interactive Knowledge Booster!')
        break
