
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas (replace with your own if using a different API)
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and its choices
    question = random.choice(data)
    choices = [question["answer"]] + question["options"]
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
    Main function that displays the topic menu and handles user interaction.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic}")
    
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
