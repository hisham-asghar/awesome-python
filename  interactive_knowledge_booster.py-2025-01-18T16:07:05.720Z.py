
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

# Function to display the main menu
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    print('5. Exit')

# Function to display a random fact or concept for the selected topic
def display_random_fact(topic):
    # Fetch data from an API or a predefined database
    if topic == 'Science':
        facts = [
            'The human body contains around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Supermassive black holes are found at the center of most galaxies, including our own.'
        ]
    elif topic == 'Technology':
        facts = [
            'The first digital computer, ENIAC, was developed in 1946 and weighed over 30 tons.',
            'The internet was initially called ARPANET and was created by the U.S. Department of Defense in 1969.',
            'The first smartphone, the IBM Simon, was introduced in 1992.'
        ]
    elif topic == 'History':
        facts = [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ]
    elif topic == 'General Knowledge':
        facts = [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The Eiffel Tower can be 15 cm taller during the summer, when thermal expansion causes the iron to expand.'
        ]
    else:
        return

    random_fact = random.choice(facts)
    print(f'Did you know that {random_fact}?')

# Function to display a multiple-choice quiz for the selected topic
def display_quiz(topic):
    # Fetch quiz questions and answers from an API or a predefined database
    if topic == 'Science':
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system is known as the "Red Planet"?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Venus'],
                'answer': 'Mars'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ]
    elif topic == 'Technology':
        questions = [
            {
                'question': 'What is the name of the first programmable computer?',
                'options': ['ENIAC', 'UNIVAC', 'ARPANET', 'IBM Simon'],
                'answer': 'ENIAC'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            }
        ]
    elif topic == 'History':
        questions = [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which ancient civilization is known for building the Pyramids of Giza?',
                'options': ['Mesopotamia', 'Indus Valley', 'Aztec', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            }
        ]
    elif topic == 'General Knowledge':
        questions = [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'Which animal is known as the tallest living terrestrial animal?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            }
        ]
    else:
        return

    score = 0
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
    print(f'Your final score is: {score}/{len(questions)}')

# Main program loop
while True:
    display_menu()
    user_choice = input('Enter your choice (1-5): ')

    if user_choice == '1':
        display_random_fact('Science')
        display_quiz('Science')
    elif user_choice == '2':
        display_random_fact('Technology')
        display_quiz('Technology')
    elif user_choice == '3':
        display_random_fact('History')
        display_quiz('History')
    elif user_choice == '4':
        display_random_fact('General Knowledge')
        display_quiz('General Knowledge')
    elif user_choice == '5':
        print('Exiting the Interactive Knowledge Booster. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
