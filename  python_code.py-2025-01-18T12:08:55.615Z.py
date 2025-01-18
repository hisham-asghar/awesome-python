Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz_question(topic):
    """
    Generate a multiple-choice quiz question for the specified topic.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    data = response.json()
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]
    return question, choices, correct_answer

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")

    # Display the topic menu
    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")

    # Get user's topic selection
    topic_choice = int(input("Enter the number of the topic: "))
    selected_topic = list(topics.keys())[topic_choice - 1]
    print(f"You selected: {selected_topic}")

    # Display a random fact or concept from the selected topic
    fact = get_random_fact(selected_topic)
    print(f"\nRandom {selected_topic} fact: {fact}")

    # Run a quiz on the selected topic
    print("\nTime for a quiz!")
    question, choices, correct_answer = quiz_question(selected_topic)
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = int(input("Enter the number of the correct answer: "))
    if user_answer == correct_answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is {correct_answer}.")

    print("\nThank you for using the Interactive Knowledge Builder!")

if __name__ == "__main__":
    main()