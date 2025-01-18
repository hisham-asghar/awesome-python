
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

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the chosen topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]["question"]
    choices = data[0]["choices"]
    answer = data[0]["answer"]

    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

def main():
    """
    Displays a menu for users to select a topic, then provides a fact and a quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
