
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

# Function to fetch a random fact from the API
def get_random_fact(topic):
    api_key = 'YOUR_API_KEY_HERE'
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    topic_choice = input('Enter the number of the topic: ')
    return topics[topic_choice]

# Function to display the random fact and quiz
def display_fact_and_quiz(topic):
    fact = get_random_fact(topic)
    print(f'Random {topic} fact: {fact}')

    # Quiz questions and answers
    quiz_questions = {
        'Science': [
            ('What is the chemical symbol for gold?', ['Au', 'Ag', 'Cu', 'Fe']),
            ('What is the name of the largest planet in our solar system?', ['Jupiter', 'Saturn', 'Mars', 'Venus'])
        ],
        'Technology': [
            ('What is the name of the world's first programmable computer?', ['ENIAC', 'Apple I', 'IBM PC', 'Commodore 64']),
            ('What is the name of the operating system developed by Apple Inc.?', ['macOS', 'Windows', 'Linux', 'Android'])
        ],
        'History': [
            ('In what year did World War II end?', ['1945', '1939', '1918', '1975']),
            ('Who was the first president of the United States?', ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams'])
        ],
        'General Knowledge': [
            ('What is the capital city of Australia?', ['Canberra', 'Sydney', 'Melbourne', 'Brisbane']),
            ('What is the largest ocean on Earth?', ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'])
        ]
    }

    # Display the quiz questions and get user input
    for question, options in quiz_questions[topic]:
        print(question)
        for i, option in enumerate(options):
            print(f'{i+1}. {option}')
        user_answer = input('Enter the number of the correct answer: ')
        if options[int(user_answer)-1] == quiz_questions[topic][0][1][0]:
            print('Correct!')
        else:
            print('Incorrect. Please try again.')

# Main function to run the script
def main():
    topic = display_menu()
    display_fact_and_quiz(topic)

if __name__ == '__main__':
    main()
