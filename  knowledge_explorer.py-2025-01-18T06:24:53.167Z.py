import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': {'name': 'Science', 'api': 'https://api.api-ninjas.com/v1/science'},
    '2': {'name': 'Technology', 'api': 'https://api.api-ninjas.com/v1/technology'},
    '3': {'name': 'History', 'api': 'https://api.api-ninjas.com/v1/history'},
    '4': {'name': 'General Knowledge', 'api': 'https://api.api-ninjas.com/v1/trivia'}
}

# Function to display the topic menu and get user's choice
def display_topic_menu():
    print('Select a topic:')
    for topic_id, topic_info in topics.items():
        print(f'{topic_id}. {topic_info["name"]}')
    
    while True:
        choice = input('Enter your choice (1-4): ')
        if choice in topics:
            return choice
        else:
            print('Invalid choice. Please try again.')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_id):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    headers = {'X-Api-Key': api_key}
    url = topics[topic_id]['api']
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data[0]  # Assuming the API returns a single fact/concept
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None

# Function to display the random fact or concept and the interactive quiz
def display_knowledge_content(fact):
    print(f'Random {topics[choice]["name"]} fact or concept:')
    print(fact)
    
    # Interactive quiz
    print('Test your knowledge with a multiple-choice question:')
    question = fact['question']
    options = fact['options']
    answer = fact['answer']
    
    print(question)
    for i, option in enumerate(options, start=1):
        print(f'{i}. {option}')
    
    while True:
        user_answer = input('Enter your answer (1-4): ')
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            if options[int(user_answer) - 1] == answer:
                print('Correct!')
            else:
                print(f'Incorrect. The correct answer is: {answer}')
            break
        else:
            print('Invalid input. Please try again.')

# Main program loop
while True:
    choice = display_topic_menu()
    fact = get_random_fact(choice)
    if fact:
        display_knowledge_content(fact)
    
    again = input('Do you want to explore another topic? (y/n) ').lower()
    if again != 'y':
        print('Thank you for using the knowledge exploration tool. Goodbye!')
        break