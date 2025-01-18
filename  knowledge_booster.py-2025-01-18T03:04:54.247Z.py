
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API or a predefined database.
    """
    # Example using the 'uselessfacts' API
    if topic == 'science':
        response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?category=science')
    elif topic == 'technology':
        response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?category=technology')
    elif topic == 'history':
        response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?category=history')
    else:
        response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')

    if response.status_code == 200:
        fact = response.json()['text']
        return fact
    else:
        return 'Error fetching fact.'

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the chosen topic.
    """
    # Example quiz questions
    if topic == 'science':
        question = 'What is the chemical symbol for gold?'
        choices = ['Au', 'Ag', 'Cu', 'Fe']
        answer = 0
    elif topic == 'technology':
        question = 'What does "HTTP" stand for?'
        choices = ['Hyper Text Transfer Protocol', 'Hyper Text Transformation Protocol', 'Hyper Text Transport Protocol', 'Hyper Text Transmission Protocol']
        answer = 0
    elif topic == 'history':
        question = 'In what year was the Declaration of Independence signed?'
        choices = ['1776', '1787', '1789', '1792']
        answer = 0
    else:
        question = 'What is the capital of Australia?'
        choices = ['Sydney', 'Melbourne', 'Brisbane', 'Canberra']
        answer = 3

    return question, choices, answer

def main():
    print('Welcome to the Knowledge Booster!')
    print('Select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General Knowledge')

    topic_choice = int(input('Enter the number of the topic you want to explore: '))

    if topic_choice == 1:
        topic = 'science'
    elif topic_choice == 2:
        topic = 'technology'
    elif topic_choice == 3:
        topic = 'history'
    else:
        topic = 'general'

    fact = get_random_fact(topic)
    print(f'\nDid you know? {fact}')

    question, choices, answer = quiz_question(topic)
    print(f'\n{question}')
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')

    user_answer = int(input('Enter the number of the correct answer: '))
    if user_answer == answer + 1:
        print('Correct! You're a knowledge master.')
    else:
        print('Oops, that's not the right answer. Better luck next time!')

if __name__ == '__main__':
    main()
