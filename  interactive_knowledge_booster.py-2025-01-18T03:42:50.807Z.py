
import random
import requests
import json

# Define the topics and corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        if topic == "General Knowledge":
            data = response.json()
            return data["question"], data["options"], data["answer"]
        else:
            return response.json()["fact"]
    else:
        return "Error fetching data."

def quiz(topic):
    """
    Provides an interactive quiz for the user to test their knowledge on the selected topic.
    """
    question, options, answer = get_random_fact(topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    topic = list(topics.keys())[topic_choice-1]
    
    fact = get_random_fact(topic)
    print(f"\nHere's a random {topic} fact: {fact}")
    
    quiz(topic)

if __name__ == "__main__":
    main()
