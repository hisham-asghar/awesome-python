
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

api_endpoints = {
    'Science': 'https://api.api-ninjas.com/v1/science',
    'Technology': 'https://api.api-ninjas.com/v1/technology',
    'History': 'https://api.api-ninjas.com/v1/history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/trivia'
}

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    return input('Enter your choice (1-4): ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    headers = {'X-Api-Key': api_key}
    response = requests.get(api_endpoints[topic], headers=headers)
    data = response.json()
    return data[0]['fact']

# Function to display a random fact or concept and run a quiz
def interactive_knowledge_booster():
    user_choice = display_menu()
    selected_topic = topics[user_choice]
    print(f'You selected: {selected_topic}')
    
    # Fetch and display a random fact or concept
    random_fact = get_random_fact(selected_topic)
    print(f'Random {selected_topic} fact: {random_fact}')
    
    # Run a quiz
    quiz_questions = [
        {
            'question': 'What is the chemical symbol for gold?',
            'options': ['Au', 'Ag', 'Cu', 'Fe'],
            'answer': 'Au'
        },
        {
            'question': 'Who invented the telephone?',
            'options': ['Alexander Graham Bell', 'Thomas Edison', 'Nikola Tesla', 'Marie Curie'],
            'answer': 'Alexander Graham Bell'
        },
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
            'answer': 'Jupiter'
        },
        {
            'question': 'What is the capital of Australia?',
            'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
            'answer': 'Canberra'
        }
    ]
    
    score = 0
    for question in quiz_questions:
        print(question['question'])
        for index, option in enumerate(question['options'], start=1):
            print(f'{index}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer) - 1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    
    print(f'Your final score is: {score}/{len(quiz_questions)}')

# Run the interactive knowledge booster
interactive_knowledge_booster()
