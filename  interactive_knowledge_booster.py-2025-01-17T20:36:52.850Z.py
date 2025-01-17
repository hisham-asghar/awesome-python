
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

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the chosen topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random trivia question
    question = random.choice(data)
    
    # Prepare the multiple-choice options
    options = [question["answer"]] + question["incorrect_answers"]
    random.shuffle(options)
    
    # Display the question and options
    print(f"Question: {question['question']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    
    # Check if the user's answer is correct
    if options[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic choice
    choice = int(input("Enter the number of the topic: "))
    
    # Fetch and display a random fact or concept
    topic = list(topics.keys())[choice-1]
    print(f"\nRandom {topic} fact: {get_random_fact(topic)}")
    
    # Provide a quiz for the chosen topic
    print(f"\nNow, let's test your {topic.lower()} knowledge!")
    quiz(topic)

if __name__ == "__main__":
    main()
