Here is the raw Python code extracted from the JSON:

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

# Define the API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas service.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using the API-Ninjas service.
    """
    url = topics[topic] + "?type=multiple_choice"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]["question"]
    choices = data[0]["options"]
    answer = data[0]["answer"]
    return question, choices, answer

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))

        print("\nTime for a quiz!")
        question, choices, answer = quiz_question(selected_topic)
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()