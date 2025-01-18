
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    1: {'name': 'Science', 'api': 'https://api.api-ninjas.com/v1/science'},
    2: {'name': 'Technology', 'api': 'https://api.api-ninjas.com/v1/tech'},
    3: {'name': 'History', 'api': 'https://api.api-ninjas.com/v1/history'},
    4: {'name': 'General Knowledge', 'api': 'https://api.api-ninjas.com/v1/trivia'}
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic_id):
    api_key = 'YOUR_API_KEY_HERE'
    url = topics[topic_id]['api']
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

# Function to display the menu and get user's topic selection
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_info in topics.items():
        print(f'{topic_id}. {topic_info["name"]}')
    return int(input('Enter your choice (1-4): '))

# Function to display a random fact or concept and an interactive quiz
def run_topic_session(topic_id):
    fact = get_random_fact(topic_id)
    print(f'\nRandom {topics[topic_id]["name"]} fact: {fact["fact"]}')

    # Interactive quiz
    print('\nLet\'s test your knowledge with a multiple-choice quiz!')
    question = fact['question']
    options = fact['options']
    correct_answer = fact['answer']

    print(f'\nQuestion: {question}')
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')

    user_answer = int(input('Enter your answer (1-4): '))
    if options[user_answer-1] == correct_answer:
        print('Correct! Well done.')
    else:
        print(f'Oops, the correct answer is: {correct_answer}')

# Main program loop
while True:
    topic_id = display_menu()
    run_topic_session(topic_id)
    print('\nWould you like to try another topic? (y/n)')
    if input().lower() != 'y':
        break

print('Thank you for using the Interactive Knowledge Booster. Have a great day!')
