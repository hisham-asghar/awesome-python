
import random
import requests
import json

# Topics and their corresponding API endpoints or data sources
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
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Presents a multiple-choice quiz for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question["fact"]] + [random.choice(data)["fact"] for _ in range(3)]
    random.shuffle(choices)
    print(f"Question: {question['fact']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    answer = int(input("Enter the number of the correct answer: "))
    if choices[answer-1] == question["fact"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['fact']}")

def main():
    """
    The main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic}:")
            print(get_fact(selected_topic))
            print("\nLet's test your knowledge!")
            quiz(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
