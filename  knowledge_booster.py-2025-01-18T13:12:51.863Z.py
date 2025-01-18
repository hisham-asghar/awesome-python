
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    '1': {'name': 'Science', 'api': 'https://api.api-ninjas.com/v1/science'},
    '2': {'name': 'Technology', 'api': 'https://api.api-ninjas.com/v1/technology'},
    '3': {'name': 'History', 'api': 'https://api.api-ninjas.com/v1/history'},
    '4': {'name': 'General Knowledge', 'api': 'https://api.api-ninjas.com/v1/trivia'}
}

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for key, topic in topics.items():
        print(f'{key}. {topic["name"]}')
    return input('Enter the number of your choice: ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_id):
    topic = topics[topic_id]
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    headers = {'X-Api-Key': api_key}
    response = requests.get(topic['api'], headers=headers)
    data = response.json()
    return data[0]  # Assuming the API returns a list of facts/concepts

# Function to display the random fact or concept
def display_fact(fact):
    print(f'Did you know that {fact}?')

# Function to create and display a multiple-choice quiz
def quiz(topic_id):
    topic = topics[topic_id]
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    headers = {'X-Api-Key': api_key}
    response = requests.get(topic['api'], headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question['fact']] + [random.choice(data)['fact'] for _ in range(3)]
    random.shuffle(choices)
    print(f'Question: {question["fact"]}')
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')
    user_answer = int(input('Enter the number of the correct answer: '))
    if choices[user_answer-1] == question['fact']:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is: {question["fact"]}')

# Main program loop
while True:
    topic_id = display_menu()
    if topic_id in topics:
        fact = get_random_fact(topic_id)
        display_fact(fact)
        quiz(topic_id)
    else:
        print('Invalid choice. Please try again.')
    print()
