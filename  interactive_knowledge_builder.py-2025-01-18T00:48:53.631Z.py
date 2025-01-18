Here is the raw Python code without any additional commentary:

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

# API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas service.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]["fact"]
    else:
        return "Error fetching data from the API."

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using the API-Ninjas service.
    """
    url = topics[topic] + "?type=multiple_choice"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        question = data[0]["question"]
        choices = data[0]["options"]
        answer = data[0]["answer"]
        return question, choices, answer
    else:
        return "Error fetching quiz data from the API."

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Select a topic to get started:")
    
    # Display the available topics
    for topic in topics:
        print(f"- {topic}")
    
    # Get the user's topic selection
    selected_topic = input("Enter your topic choice: ")
    
    if selected_topic in topics:
        # Fetch a random fact or concept for the selected topic
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact or concept:")
        print(fact)
        
        # Generate a multiple-choice quiz question for the selected topic
        question, choices, answer = quiz_question(selected_topic)
        print(f"\nNow, let's test your knowledge with a {selected_topic.lower()} quiz question:")
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        # Get the user's answer and check if it's correct
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == answer:
            print("Correct! You've increased your knowledge.")
        else:
            print(f"Incorrect. The correct answer is '{answer}'.")
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()