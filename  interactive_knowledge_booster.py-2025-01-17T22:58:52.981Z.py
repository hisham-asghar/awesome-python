import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints or data sources
topics = {
    '1': {'name': 'Science', 'api': 'https://api.api-ninjas.com/v1/science'},
    '2': {'name': 'Technology', 'api': 'https://api.api-ninjas.com/v1/technology'},
    '3': {'name': 'History', 'api': 'https://api.api-ninjas.com/v1/history'},
    '4': {'name': 'General Knowledge', 'api': 'https://api.api-ninjas.com/v1/trivia'}
}

# Function to display the menu and get user's topic choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f"{key}. {value['name']}")
    return input('Enter your choice (1-4): ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    headers = {'X-Api-Key': api_key}
    response = requests.get(topic['api'], headers=headers)
    data = response.json()
    return data[0]

# Function to display the random fact or concept
def display_fact(fact):
    print(f"Did you know? {fact}")

# Function to create and display a multiple-choice quiz question
def quiz_question(topic):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    headers = {'X-Api-Key': api_key}
    response = requests.get(topic['api'], headers=headers)
    data = response.json()
    
    # Select a random question and its options
    question = random.choice(data)
    options = [question['answer']] + question['options']
    random.shuffle(options)
    
    # Display the question and options
    print(f"Question: {question['question']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer and check if it's correct
    user_answer = int(input('Enter your answer (1-4): '))
    if options[user_answer-1] == question['answer']:
        print('Correct!')
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

# Main function to run the interactive knowledge booster
def main():
    choice = display_menu()
    if choice in topics:
        fact = get_random_fact(topics[choice])
        display_fact(fact)
        quiz_question(topics[choice])
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()