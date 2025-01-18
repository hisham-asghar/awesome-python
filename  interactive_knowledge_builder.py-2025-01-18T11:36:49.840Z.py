
import random
import requests
import json

# Define the topics and their corresponding API endpoints
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
API_KEY = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas API.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic using the API-Ninjas API.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question["answer"]] + question["alternatives"]
    random.shuffle(choices)
    print(f"Question: {question['question']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter the number of the correct answer: "))
    if choices[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that provides the interactive knowledge-building experience.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    while True:
        print("\nSelect a topic:")
        for topic in TOPICS:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")
        if selected_topic not in TOPICS:
            print("Invalid topic. Please try again.")
            continue
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_fact(selected_topic))
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
        continue_input = input("\nDo you want to explore another topic? (y/n) ")
        if continue_input.lower() != "y":
            break

if __name__ == "__main__":
    main()
