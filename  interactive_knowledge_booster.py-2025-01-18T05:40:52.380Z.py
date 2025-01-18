
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

api_endpoints = {
    'Science': 'https://api.api-ninjas.com/v1/facts?category=science',
    'Technology': 'https://api.api-ninjas.com/v1/facts?category=technology',
    'History': 'https://api.api-ninjas.com/v1/facts?category=history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Function to get a random fact from the API
def get_random_fact(topic):
    api_key = 'YOUR_API_KEY_HERE'
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    choice = input('Enter your choice (1-4): ')
    return choice

# Function to run the quiz
def run_quiz(topic):
    print(f'\nLet\'s test your {topics[topic]} knowledge!')
    
    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = [
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['A. Mars', 'B. Jupiter', 'C. Saturn', 'D. Neptune'],
            'answer': 'B'
        },
        {
            'question': 'Which country is known as the "Land of the Rising Sun"?',
            'options': ['A. China', 'B. Japan', 'C. South Korea', 'D. India'],
            'answer': 'B'
        },
        {
            'question': 'What is the rarest blood type?',
            'options': ['A. AB-', 'B. O-', 'C. A-', 'D. B-'],
            'answer': 'A'
        }
    ]

    score = 0
    for question in quiz_data:
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input('Enter your answer (A-D): ').upper()
        if user_answer == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is', question['answer'])
    
    print(f'\nYour final score is {score} out of {len(quiz_data)}.')

# Main function
def main():
    choice = display_menu()
    topic = topics[choice]
    print(f'\nHere\'s a random fact about {topic}:')
    print(get_random_fact(topic))
    run_quiz(choice)

if __name__ == '__main__':
    main()
