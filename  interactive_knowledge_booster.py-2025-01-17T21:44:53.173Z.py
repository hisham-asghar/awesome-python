
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

topic_apis = {
    '1': 'https://api.api-ninjas.com/v1/science?category=random',
    '2': 'https://api.api-ninjas.com/v1/technology?category=random',
    '3': 'https://api.api-ninjas.com/v1/history?category=random',
    '4': 'https://opentdb.com/api.php?amount=1&type=multiple'
}

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    return input('Enter the number of your chosen topic: ')

# Function to fetch and display a random fact or concept
def display_random_fact(topic_id):
    api_url = topic_apis[topic_id]
    if topic_id == '4':
        response = requests.get(api_url)
        data = response.json()['results'][0]
        print(f"Random fact: {data['question']}")
    else:
        response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()[0]
        print(f"Random {topics[topic_id].lower()} fact: {data['fact']}")

# Function to run the interactive quiz
def run_quiz(topic_id):
    api_url = topic_apis[topic_id]
    if topic_id == '4':
        response = requests.get(api_url)
        data = response.json()['results'][0]
        print(f"Question: {data['question']}")
        print("Options:")
        for i, option in enumerate(data['incorrect_answers']):
            print(f"{i+1}. {option}")
        print(f"{len(data['incorrect_answers'])+1}. {data['correct_answer']}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if user_answer == len(data['incorrect_answers']) + 1:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {data['correct_answer']}")
    else:
        print("Sorry, the quiz feature is not available for this topic yet.")

# Main program loop
while True:
    topic_id = display_menu()
    if topic_id in topics:
        display_random_fact(topic_id)
        run_quiz(topic_id)
    else:
        print("Invalid topic. Please try again.")
    print()
