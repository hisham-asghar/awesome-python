
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

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the quiz for the selected topic
def run_quiz(topic):
    print(f"\nLet's test your {topic} knowledge!")
    
    # Fetch 5 multiple-choice questions from the API
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "?type=multiple_choice&limit=5"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    questions = response.json()
    
    # Run the quiz
    score = 0
    for question in questions:
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
    
    print(f"\nYour final score: {score} out of 5")

# Main function to run the program
def main():
    topic = display_menu()
    print(f"\nHere's a random {topic} fact for you:")
    print(get_random_fact(topic))
    run_quiz(topic)

if __name__ == "__main__":
    main()
