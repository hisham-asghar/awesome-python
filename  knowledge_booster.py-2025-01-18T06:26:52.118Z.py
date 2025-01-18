
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"\nLet's test your {topic.lower()} knowledge!")
    
    # Fetch trivia questions from the API
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random trivia question
    trivia = random.choice(data)
    question = trivia['question']
    options = trivia['options']
    answer = trivia['answer']
    
    # Display the question and options
    print(f"\nQuestion: {question}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check the user's answer and provide feedback
    if options[user_answer-1] == answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is '{answer}'.")

# Main function to run the knowledge booster
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    print(f"\nHere's a random {topic.lower()} fact for you:")
    print(f"- {fact}")
    run_quiz(topic)

if __name__ == "__main__":
    main()
