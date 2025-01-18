
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

# Function to display the menu and get user's topic choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    return input('Enter the number of your chosen topic: ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == 'Science':
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science')
    elif topic == 'Technology':
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology')
    elif topic == 'History':
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history')
    elif topic == 'General Knowledge':
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general')
    
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return 'Failed to fetch a random fact. Please try again later.'

# Function to display a multiple-choice quiz for the selected topic
def display_quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == 'Science':
        response = requests.get('https://opentdb.com/api.php?amount=1&category=17&type=multiple')
    elif topic == 'Technology':
        response = requests.get('https://opentdb.com/api.php?amount=1&category=18&type=multiple')
    elif topic == 'History':
        response = requests.get('https://opentdb.com/api.php?amount=1&category=23&type=multiple')
    elif topic == 'General Knowledge':
        response = requests.get('https://opentdb.com/api.php?amount=1&category=9&type=multiple')
    
    if response.status_code == 200:
        quiz_data = json.loads(response.text)['results'][0]
        print(quiz_data['question'])
        
        # Shuffle the correct and incorrect answers
        answers = quiz_data['incorrect_answers']
        answers.append(quiz_data['correct_answer'])
        random.shuffle(answers)
        
        # Display the multiple-choice options
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        # Get the user's answer and check if it's correct
        user_answer = int(input('Enter the number of your answer: '))
        if answers[user_answer-1] == quiz_data['correct_answer']:
            print('Correct! You've increased your knowledge.')
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['correct_answer']}")
    else:
        print('Failed to fetch quiz questions. Please try again later.')

# Main program loop
while True:
    topic_choice = display_menu()
    if topic_choice in topics:
        print(f'\nHere's a random fact about {topics[topic_choice]}:')
        print(get_random_fact(topics[topic_choice]))
        print('\nNow, let's test your knowledge with a quiz!')
        display_quiz(topics[topic_choice])
        print('\nThank you for using the Interactive Knowledge Booster. Have a great day!')
        break
    else:
        print('Invalid choice. Please try again.')
