
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/trivia?category=science",
    "Technology": "https://api.api-ninjas.com/v1/trivia?category=technology",
    "History": "https://api.api-ninjas.com/v1/trivia?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia?category=general"
}

# API key for the API-Ninjas Trivia API
api_key = "YOUR_API_KEY_HERE"

def get_trivia(topic):
    """
    Fetches a random trivia fact or concept from the selected topic using the API-Ninjas Trivia API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic, with multiple-choice questions.
    """
    trivia = get_trivia(topic)
    print(f"Question: {trivia['question']}")
    print("Options:")
    for i, option in enumerate(trivia['options'], start=1):
        print(f"{i}. {option}")
    
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == trivia['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {trivia['answer']}.")

def main():
    """
    Displays a menu for users to select a topic, and then provides a trivia fact or concept and a quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        trivia = get_trivia(selected_topic)
        print(f"\nFact or Concept: {trivia['fact']}")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
