Here is the raw Python code without any additional commentary:

import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    return selected_topic

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"\nLet's test your {topic} knowledge!")
    
    # Fetch quiz questions and answers from the API
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Randomly select a quiz question
    quiz_question = random.choice(data)
    
    # Display the quiz question and options
    print(quiz_question['question'])
    options = quiz_question['options']
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get user input and check the answer
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == quiz_question['answer']:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

# Main function to run the script
def main():
    selected_topic = display_menu()
    random_fact = get_random_fact(selected_topic)
    print(f"\nHere's a random {selected_topic.lower()} fact: {random_fact}")
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()