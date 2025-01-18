Here is the raw Python code without any additional commentary:

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

# Define the data sources for each topic
data_sources = {
    'Science': 'https://api.api-ninjas.com/v1/science',
    'Technology': 'https://api.api-ninjas.com/v1/technology',
    'History': 'https://api.api-ninjas.com/v1/history',
    'General Knowledge': 'https://opentdb.com/api.php?amount=1&type=multiple'
}

# Define the API key for the API-Ninjas APIs
api_key = 'YOUR_API_KEY_HERE'

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the selected topic.
    """
    if topic in ['Science', 'Technology', 'History']:
        url = data_sources[topic]
        headers = {'X-Api-Key': api_key}
        response = requests.get(url, headers=headers)
        data = response.json()
        return data[0]['fact']
    elif topic == 'General Knowledge':
        url = data_sources[topic]
        response = requests.get(url)
        data = response.json()
        return data['results'][0]['question']

def run_quiz(topic):
    """
    Run an interactive quiz for the selected topic.
    """
    if topic in ['Science', 'Technology', 'History']:
        url = data_sources[topic]
        headers = {'X-Api-Key': api_key}
        response = requests.get(url, headers=headers)
        data = response.json()
        question = data[0]['question']
        options = data[0]['options']
        answer = data[0]['answer']
    elif topic == 'General Knowledge':
        url = data_sources[topic]
        response = requests.get(url)
        data = response.json()
        question = data['results'][0]['question']
        options = [data['results'][0]['correct_answer']] + data['results'][0]['incorrect_answers']
        random.shuffle(options)
        answer = data['results'][0]['correct_answer']

    print(f'Question: {question}')
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')

    user_answer = input('Enter your answer (1-4): ')
    if options[int(user_answer) - 1] == answer:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is: {answer}')

def main():
    """
    Main function to run the interactive knowledge app.
    """
    print('Welcome to the Interactive Knowledge App!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')

    selected_topic = input('Enter the topic number (1-4): ')
    if selected_topic in topics:
        print(f'You selected: {topics[selected_topic]}')
        print(get_random_fact(topics[selected_topic]))
        run_quiz(topics[selected_topic])
    else:
        print('Invalid topic selection. Please try again.')

if __name__ == '__main__':
    main()