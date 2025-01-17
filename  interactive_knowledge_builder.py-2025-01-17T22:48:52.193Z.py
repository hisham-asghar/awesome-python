
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
api_key = "your_api_key_here"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using the corresponding API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the selected topic.
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

    selected_topic = input("Enter your choice: ")
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz = quiz_question(selected_topic)
    print(quiz["question"])
    for i, choice in enumerate(quiz["choices"], start=1):
        print(f"{i}. {choice}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if quiz["choices"][user_answer - 1] == quiz["answer"]:
        print("Correct! You're a knowledge champion!")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
