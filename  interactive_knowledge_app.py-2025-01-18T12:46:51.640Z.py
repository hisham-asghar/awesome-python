
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    'Science': 'https://api.sampleapis.com/science/facts',
    'Technology': 'https://api.sampleapis.com/tech/facts',
    'History': 'https://api.sampleapis.com/history/facts',
    'General Knowledge': 'https://api.sampleapis.com/generalknowledge/facts'
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic's data source.
    """
    try:
        response = requests.get(topics[topic])
        data = response.json()
        return random.choice(data)
    except (KeyError, requests.exceptions.RequestException):
        return 'Sorry, there was an error fetching the fact.'

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = response.json()
        fact = random.choice(data)
        options = [fact['fact']] + [random.choice(data)['fact'] for _ in range(3)]
        random.shuffle(options)
        return {
            'question': fact['description'],
            'options': options,
            'answer': fact['fact']
        }
    except (KeyError, requests.exceptions.RequestException):
        return {
            'question': 'Sorry, there was an error generating the quiz question.',
            'options': [],
            'answer': ''
        }

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print('Welcome to the Interactive Knowledge App!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic}')

    selected_topic = input('Enter your choice: ').strip()
    if selected_topic in topics:
        print(f'\nHere\'s a random fact about {selected_topic}:')
        print(get_random_fact(selected_topic))

        print('\nNow, let\'s test your knowledge with a quiz!')
        quiz = quiz_question(selected_topic)
        print(quiz['question'])
        for i, option in enumerate(quiz['options'], start=1):
            print(f'{i}. {option}')
        user_answer = input('Enter the number of the correct answer: ').strip()
        if quiz['options'][int(user_answer) - 1] == quiz['answer']:
            print('Correct! You're a knowledge expert.')
        else:
            print(f'Oops, the correct answer is: {quiz["answer"]}')
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()
