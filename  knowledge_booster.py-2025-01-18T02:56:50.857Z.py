
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

api_endpoints = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter the number of your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"\nLet's test your {topics[topic]} knowledge!")
    
    # Fetch quiz questions and answers from the API
    api_key = "YOUR_API_KEY_HERE"
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Randomly select a question and its options
    question = random.choice(data)
    options = question['options']
    
    # Display the question and options
    print(question['question'])
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get user input and check the answer
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == question['answer']:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is: {question['answer']}")

# Main function
def main():
    topic_choice = display_menu()
    topic = topics[topic_choice]
    
    # Display a random fact or concept
    print(f"\nHere's a random {topic} fact for you:")
    print(get_random_fact(topic))
    
    # Run the interactive quiz
    run_quiz(topic_choice)

if __name__ == "__main__":
    main()
