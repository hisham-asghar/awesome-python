
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
    '1': 'https://api.api-ninjas.com/v1/facts?category=science',
    '2': 'https://api.api-ninjas.com/v1/facts?category=technology',
    '3': 'https://api.api-ninjas.com/v1/facts?category=history',
    '4': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Function to fetch a random fact from the selected topic
def get_random_fact(topic):
    api_key = 'YOUR_API_KEY_HERE'
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the menu and get user's topic selection
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    return input('Enter your choice (1-4): ')

# Function to run the interactive quiz
def run_quiz(topic):
    print(f'\nLet\'s test your {topics[topic]} knowledge!')
    fact = get_random_fact(topic)
    print(f'Did you know that: {fact}')

    # Multiple-choice questions
    questions = {
        '1': 'What is the chemical symbol for gold?',
        '2': 'Who invented the telephone?',
        '3': 'In what year did the American Civil War begin?',
        '4': 'What is the largest planet in our solar system?'
    }
    answers = {
        '1': 'a) Au, b) Ag, c) Cu, d) Fe',
        '2': 'a) Alexander Graham Bell, b) Thomas Edison, c) Nikola Tesla, d) Guglielmo Marconi',
        '3': 'a) 1861, b) 1865, c) 1775, d) 1812',
        '4': 'a) Mars, b) Saturn, c) Jupiter, d) Neptune'
    }
    correct_answers = {
        '1': 'a',
        '2': 'a',
        '3': 'a',
        '4': 'c'
    }

    score = 0
    for question, options in questions.items():
        print(f'\n{questions[question]}')
        print(answers[question])
        user_answer = input('Enter your answer (a, b, c, or d): ')
        if user_answer.lower() == correct_answers[question]:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', correct_answers[question])
    print(f'\nYour final score is: {score}/{len(questions)}')

# Main function to run the program
def main():
    topic_choice = display_menu()
    run_quiz(topic_choice)

if __name__ == '__main__':
    main()
