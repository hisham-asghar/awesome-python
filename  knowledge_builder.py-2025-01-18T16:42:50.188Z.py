
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

# API key for API-Ninjas
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question["fact"]]
    for i in range(3):
        choices.append(random.choice(data)["fact"])
    random.shuffle(choices)
    print(f"Question: {question['fact']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == question["fact"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['fact']}")

def main():
    """
    The main function that provides the interactive knowledge-building experience.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic}:")
            print(get_random_fact(selected_topic))
            print("\nNow, let's test your knowledge!")
            quiz(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
