Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
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
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = random.choice(data)
    choices = [question["fact"]]
    for i in range(3):
        wrong_answer = random.choice(data)["fact"]
        if wrong_answer not in choices:
            choices.append(wrong_answer)
    random.shuffle(choices)
    return {
        "question": question["fact"],
        "choices": choices,
        "answer": question["fact"]
    }

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    chosen_topic = input("Enter your choice: ")
    if chosen_topic not in topics:
        print("Invalid topic. Exiting...")
        return

    print(f"\nHere's a random fact about {chosen_topic}:")
    print(get_random_fact(chosen_topic))

    print("\nNow, let's test your knowledge with a quiz question!")
    quiz_data = quiz_question(chosen_topic)
    print(quiz_data["question"])
    for i, choice in enumerate(quiz_data["choices"]):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_data["choices"][user_answer - 1] == quiz_data["answer"]:
        print("Correct! Well done.")
    else:
        print("Incorrect. The correct answer is:", quiz_data["answer"])

    print("\nThank you for using the Interactive Knowledge Builder!")

if __name__ == "__main__":
    main()