
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API or predefined database.
    """
    # Example using the 'uselessfacts' public API
    api_url = f'https://uselessfacts.jsph.pl/random.json?category={topic}'
    response = requests.get(api_url)
    data = response.json()
    return data['text']

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the chosen topic.
    """
    # Example quiz questions for different topics
    if topic == 'science':
        question = 'What is the chemical symbol for gold?'
        choices = ['Au', 'Ag', 'Cu', 'Fe']
        answer = 0
    elif topic == 'history':
        question = 'Who was the first president of the United States?'
        choices = ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams']
        answer = 0
    elif topic == 'technology':
        question = 'What is the name of the first programmable computer?'
        choices = ['ENIAC', 'Apple II', 'IBM PC', 'UNIVAC I']
        answer = 0
    elif topic == 'general':
        question = 'What is the largest planet in our solar system?'
        choices = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
        answer = 0
    return question, choices, answer

def main():
    """
    Provides an interactive menu for users to select a topic, learn a random fact, and take a quiz.
    """
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    topics = ['Science', 'History', 'Technology', 'General']
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic}')

    topic_choice = int(input('Enter the number of your choice: ')) - 1
    selected_topic = topics[topic_choice].lower()

    print(f'\nRandom fact about {topics[topic_choice]}:')
    print(get_random_fact(selected_topic))

    print('\nTime for a quiz! Answer the multiple-choice question:')
    question, choices, answer = quiz_question(selected_topic)
    print(question)
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')

    user_answer = int(input('Enter the number of your answer: ')) - 1
    if user_answer == answer:
        print('Correct!')
    else:
        print('Incorrect. Better luck next time!')

if __name__ == '__main__':
    main()
