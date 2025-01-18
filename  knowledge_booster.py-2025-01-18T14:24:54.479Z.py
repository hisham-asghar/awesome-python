
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define a function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == '1':
        # Fetch a random science fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY'})
        data = response.json()
        return data[0]['fact']
    elif topic == '2':
        # Fetch a random technology fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY'})
        data = response.json()
        return data[0]['fact']
    elif topic == '3':
        # Fetch a random history fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY'})
        data = response.json()
        return data[0]['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact from an API
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY'})
        data = response.json()
        return data[0]['fact']
    else:
        return 'Invalid topic selection.'

# Define a function to run the interactive quiz
def run_quiz(topic):
    if topic == '1':
        # Load science quiz questions and answers
        with open('science_quiz.json', 'r') as f:
            quiz_data = json.load(f)
    elif topic == '2':
        # Load technology quiz questions and answers
        with open('technology_quiz.json', 'r') as f:
            quiz_data = json.load(f)
    elif topic == '3':
        # Load history quiz questions and answers
        with open('history_quiz.json', 'r') as f:
            quiz_data = json.load(f)
    elif topic == '4':
        # Load general knowledge quiz questions and answers
        with open('general_knowledge_quiz.json', 'r') as f:
            quiz_data = json.load(f)
    else:
        return 'Invalid topic selection.'

    score = 0
    for question, options, answer in zip(quiz_data['questions'], quiz_data['options'], quiz_data['answers']):
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = input('Enter your answer (1-4): ')
        if user_answer == str(answer):
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', options[answer-1])
    print(f"Your final score is {score} out of {len(quiz_data['questions'])}")

# Main program loop
while True:
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic_choice = input('Enter your choice (1-4): ')

    if topic_choice in topics:
        print(f"You selected: {topics[topic_choice]}")
        print(get_random_fact(topic_choice))
        run_quiz(topic_choice)
    else:
        print('Invalid choice. Please try again.')
    
    continue_prompt = input('Do you want to try another topic? (y/n) ')
    if continue_prompt.lower() != 'y':
        break

print('Thank you for using the Interactive Knowledge Booster. Goodbye!')
