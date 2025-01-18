
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the chosen topic using a public API or database.
    """
    # Example using the 'uselessfacts' API
    api_url = f'https://uselessfacts.jsph.pl/random.json?category={topic}'
    response = requests.get(api_url)
    data = response.json()
    return data['text']

def quiz_question(topic):
    """
    Generate a multiple-choice quiz question for the chosen topic.
    """
    # Example quiz questions for different topics
    if topic == 'science':
        question = 'What is the chemical symbol for gold?'
        options = ['Au', 'Ag', 'Cu', 'Fe']
        answer = 0
    elif topic == 'history':
        question = 'Who was the first president of the United States?'
        options = ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'James Madison']
        answer = 0
    elif topic == 'technology':
        question = 'What is the name of the first programmable computer?'
        options = ['ENIAC', 'Apple I', 'IBM PC', 'Commodore 64']
        answer = 0
    elif topic == 'general':
        question = 'What is the largest planet in our solar system?'
        options = ['Jupiter', 'Saturn', 'Mars', 'Neptune']
        answer = 0
    return question, options, answer

def main():
    """
    The main function that runs the interactive knowledge-boosting script.
    """
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    print('1. Science')
    print('2. History')
    print('3. Technology')
    print('4. General Knowledge')

    while True:
        topic_choice = input('Enter the number of the topic (or "q" to quit): ')
        if topic_choice.lower() == 'q':
            break

        if topic_choice == '1':
            topic = 'science'
        elif topic_choice == '2':
            topic = 'history'
        elif topic_choice == '3':
            topic = 'technology'
        elif topic_choice == '4':
            topic = 'general'
        else:
            print('Invalid choice. Please try again.')
            continue

        print(f'\nHere is a random fact about {topic}:')
        print(get_random_fact(topic))

        print('\nNow let\'s test your knowledge with a quiz!')
        question, options, answer = quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f'{i+1}. {option}')

        user_answer = input('Enter the number of your answer: ')
        if int(user_answer) == answer + 1:
            print('Correct! Well done.')
        else:
            print('Incorrect. Better luck next time.')

        print('\nWould you like to try another topic?')

if __name__ == '__main__':
    main()
