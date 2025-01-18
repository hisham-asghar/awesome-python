
import random
import requests
import json

# Topics and their associated API endpoints
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
    Fetches a random fact or concept from the selected topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    question = data[0]["question"]
    options = data[0]["options"]
    answer = data[0]["answer"]

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
    Interactively guides the user through the available topics and provides a fact or quiz.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_fact(selected_topic))
        print("\nNow let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
