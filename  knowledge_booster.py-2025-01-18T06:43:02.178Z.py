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

# Function to display the menu
def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    
    topic_choice = input('Enter your choice (1-4): ')
    return topic_choice

# Function to fetch a random fact or concept
def get_random_fact(topic):
    facts = {
        'Science': [
            'The human body has around 100 trillion cells.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Diamonds are formed from carbon under extreme heat and pressure deep within the Earth.'
        ],
        'Technology': [
            'The first programmable computer was the ENIAC, which was completed in 1946.',
            'The world's first website was launched in 1991 by Tim Berners-Lee.',
            'Artificial intelligence (AI) is the simulation of human intelligence processes by machines.'
        ],
        'History': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'General Knowledge': [
            'The largest ocean on Earth is the Pacific Ocean.',
            'The Mona Lisa is a painting by the Italian Renaissance artist Leonardo da Vinci.',
            'The tallest mammal on Earth is the giraffe.'
        ]
    }
    
    return random.choice(facts[topic])

# Function to display the quiz
def display_quiz(topic):
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 'Au'},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Transpiration'], 'answer': 'Photosynthesis'},
            {'question': 'What is the name of the force that attracts objects with mass towards each other?', 'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'], 'answer': 'Gravity'}
        ],
        'Technology': [
            {'question': 'What is the name of the computer operating system developed by Microsoft?', 'options': ['Windows', 'macOS', 'Linux', 'Android'], 'answer': 'Windows'},
            {'question': 'What is the name of the programming language used to create websites?', 'options': ['HTML', 'Java', 'Python', 'C++'], 'answer': 'HTML'},
            {'question': 'What is the name of the device that converts digital signals into analog signals?', 'options': ['Modem', 'Router', 'Printer', 'Scanner'], 'answer': 'Modem'}
        ],
        'History': [
            {'question': 'What year did the American Revolutionary War begin?', 'options': ['1776', '1812', '1861', '1917'], 'answer': '1776'},
            {'question': 'Who was the first president of the United States?', 'options': ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams'], 'answer': 'George Washington'},
            {'question': 'What was the name of the first successful powered flight?', 'options': ['The Wright Flyer', 'The Concorde', 'The Apollo 11', 'The Sputnik'], 'answer': 'The Wright Flyer'}
        ],
        'General Knowledge': [
            {'question': 'What is the largest planet in our solar system?', 'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'], 'answer': 'Jupiter'},
            {'question': 'What is the name of the famous painting of the Mona Lisa?', 'options': ['The Mona Lisa', 'The Starry Night', 'The Persistence of Memory', 'The Birth of Venus'], 'answer': 'The Mona Lisa'},
            {'question': 'What is the name of the tallest mammal on Earth?', 'options': ['Giraffe', 'Elephant', 'Rhinoceros', 'Hippopotamus'], 'answer': 'Giraffe'}
        ]
    }
    
    quiz = random.choice(quizzes[topic])
    print(f'Question: {quiz["question"]}')
    for i, option in enumerate(quiz['options'], start=1):
        print(f'{i}. {option}')
    
    user_answer = input('Enter your answer (1-4): ')
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print('Correct!')
    else:
        print('Incorrect. The correct answer is:', quiz['answer'])

# Main function
def main():
    topic_choice = display_menu()
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f'\nRandom {topic} fact: {get_random_fact(topic)}')
        print('\nNow let\'s test your knowledge with a quiz!')
        display_quiz(topic)
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()