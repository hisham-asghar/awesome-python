Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Define the API endpoints for fetching trivia data
api_endpoints = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/tech",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Define the API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas service.
    """
    url = api_endpoints[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Presents a multiple-choice quiz to the user for the specified topic.
    """
    url = api_endpoints[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question["answer"]] + question["alternatives"]
    random.shuffle(choices)
    print(f"Question: {question['question']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that displays the topic menu, allows the user to select a topic,
    and then presents a random fact and a multiple-choice quiz for the selected topic.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic_choice = input("Enter the number of the topic (1-4): ")
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f"\nRandom {topic} fact: {get_random_fact(topic)}")
        print("\nTime for a quiz!")
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
