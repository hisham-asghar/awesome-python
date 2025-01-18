
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

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    return input('Enter the number of your choice: ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == 'Science':
        # Example: Fetch a random science fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science')
        if response.status_code == 200:
            facts = response.json()
            return random.choice(facts)['fact']
    elif topic == 'Technology':
        # Example: Fetch a random technology fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology')
        if response.status_code == 200:
            facts = response.json()
            return random.choice(facts)['fact']
    elif topic == 'History':
        # Example: Fetch a random history fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history')
        if response.status_code == 200:
            facts = response.json()
            return random.choice(facts)['fact']
    elif topic == 'General Knowledge':
        # Example: Fetch a random general knowledge fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general')
        if response.status_code == 200:
            facts = response.json()
            return random.choice(facts)['fact']
    return 'Sorry, no fact available for the selected topic.'

# Function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == 'Science':
        # Example: Fetch a random science quiz from an API
        response = requests.get('https://opentdb.com/api.php?amount=1&category=17&type=multiple')
        if response.status_code == 200:
            quiz_data = response.json()['results'][0]
            question = quiz_data['question']
            choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
            random.shuffle(choices)
            print(f'Question: {question}')
            for i, choice in enumerate(choices):
                print(f'{i+1}. {choice}')
            user_answer = input('Enter the number of your answer: ')
            if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
                print('Correct!')
            else:
                print(f'Incorrect. The correct answer is: {quiz_data["correct_answer"]}')
    elif topic == 'Technology':
        # Example: Fetch a random technology quiz from an API
        response = requests.get('https://opentdb.com/api.php?amount=1&category=18&type=multiple')
        if response.status_code == 200:
            quiz_data = response.json()['results'][0]
            question = quiz_data['question']
            choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
            random.shuffle(choices)
            print(f'Question: {question}')
            for i, choice in enumerate(choices):
                print(f'{i+1}. {choice}')
            user_answer = input('Enter the number of your answer: ')
            if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
                print('Correct!')
            else:
                print(f'Incorrect. The correct answer is: {quiz_data["correct_answer"]}')
    elif topic == 'History':
        # Example: Fetch a random history quiz from an API
        response = requests.get('https://opentdb.com/api.php?amount=1&category=23&type=multiple')
        if response.status_code == 200:
            quiz_data = response.json()['results'][0]
            question = quiz_data['question']
            choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
            random.shuffle(choices)
            print(f'Question: {question}')
            for i, choice in enumerate(choices):
                print(f'{i+1}. {choice}')
            user_answer = input('Enter the number of your answer: ')
            if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
                print('Correct!')
            else:
                print(f'Incorrect. The correct answer is: {quiz_data["correct_answer"]}')
    elif topic == 'General Knowledge':
        # Example: Fetch a random general knowledge quiz from an API
        response = requests.get('https://opentdb.com/api.php?amount=1&category=9&type=multiple')
        if response.status_code == 200:
            quiz_data = response.json()['results'][0]
            question = quiz_data['question']
            choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
            random.shuffle(choices)
            print(f'Question: {question}')
            for i, choice in enumerate(choices):
                print(f'{i+1}. {choice}')
            user_answer = input('Enter the number of your answer: ')
            if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
                print('Correct!')
            else:
                print(f'Incorrect. The correct answer is: {quiz_data["correct_answer"]}')

# Main function to run the knowledge booster
def main():
    topic_choice = display_menu()
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f'\nHere is a random fact about {topic}:')
        print(get_random_fact(topic))
        print('\nNow, let\'s test your knowledge with a quiz!')
        quiz(topic)
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
