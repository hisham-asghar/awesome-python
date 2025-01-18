
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
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the selected topic using the API-Ninjas API.
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

    # Display the topic menu
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    # Fetch a random fact or concept from the selected topic
    fact = get_random_fact(selected_topic)
    print(f"\nHere's a random fact about {selected_topic}:")
    print(fact)

    # Quiz the user on the selected topic
    print(f"\nNow, let's test your knowledge with a {selected_topic} quiz!")
    question, choices, answer = quiz_question(selected_topic)
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = input("Enter the number of the correct answer: ")
    if int(user_answer) == answer:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
