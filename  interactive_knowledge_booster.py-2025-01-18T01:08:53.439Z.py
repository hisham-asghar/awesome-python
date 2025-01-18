
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

topic_apis = {
    '1': 'https://api.api-ninjas.com/v1/facts?category=science',
    '2': 'https://api.api-ninjas.com/v1/facts?category=technology',
    '3': 'https://api.api-ninjas.com/v1/facts?category=history',
    '4': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    return input('Enter the number of your chosen topic: ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_id):
    api_url = topic_apis[topic_id]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return random.choice(data)['fact']

# Function to display the quiz and get user answers
def quiz(topic_id):
    print(f'Time to test your {topics[topic_id]} knowledge!')
    print('Answer the following multiple-choice questions:')

    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = {
        '1': {
            'question': 'What is the chemical symbol for gold?',
            'options': ['Au', 'Ag', 'Cu', 'Fe'],
            'answer': 0
        },
        '2': {
            'question': 'Who invented the telephone?',
            'options': ['Thomas Edison', 'Alexander Graham Bell', 'Nikola Tesla', 'Charles Babbage'],
            'answer': 1
        },
        # Add more quiz questions and answers here
    }

    score = 0
    for question_id, question_data in quiz_data.items():
        print(question_data['question'])
        for i, option in enumerate(question_data['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == question_data['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. Try again next time.')
    print(f'Your final score is {score} out of {len(quiz_data)}.')

# Main program loop
while True:
    topic_id = display_menu()
    if topic_id in topics:
        fact = get_random_fact(topic_id)
        print(f'Did you know? {fact}')
        quiz(topic_id)
        continue_prompt = input('Would you like to explore another topic? (y/n) ')
        if continue_prompt.lower() != 'y':
            break
    else:
        print('Invalid topic. Please try again.')
