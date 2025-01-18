
import random
import requests
import json

# API endpoints for fetching educational content
TOPIC_ENDPOINTS = {
    'science': 'https://api.api-ninjas.com/v1/science',
    'technology': 'https://api.api-ninjas.com/v1/technology',
    'history': 'https://api.api-ninjas.com/v1/history',
    'general': 'https://api.api-ninjas.com/v1/trivia'
}

# API key for accessing the API-Ninjas API
API_KEY = 'your_api_key_here'

def get_topic_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = TOPIC_ENDPOINTS[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    url = TOPIC_ENDPOINTS[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]['question']
    choices = data[0]['choices']
    answer = data[0]['answer']
    return question, choices, answer

def main():
    """
    The main function that runs the interactive knowledge-boosting script.
    """
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General Knowledge')

    topic_choice = input('Enter the number of your choice (1-4): ')

    if topic_choice == '1':
        topic = 'science'
    elif topic_choice == '2':
        topic = 'technology'
    elif topic_choice == '3':
        topic = 'history'
    elif topic_choice == '4':
        topic = 'general'
    else:
        print('Invalid choice. Exiting...')
        return

    fact = get_topic_fact(topic)
    print(f'\nHere\'s a random fact about {topic.capitalize()}:')
    print(fact)

    question, choices, answer = quiz_question(topic)
    print(f'\nNow, let\'s test your knowledge with a quiz question about {topic.capitalize()}:')
    print(question)
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')

    user_answer = input('Enter the number of your answer (1-4): ')
    if int(user_answer) == answer:
        print('Correct! You\'re a knowledge master.')
    else:
        print('Oops, that\'s not the right answer. Better luck next time!')

if __name__ == '__main__':
    main()
