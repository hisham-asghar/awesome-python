
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API or predefined data.
    """
    if topic in topics:
        if topic == "General Knowledge":
            response = requests.get(topics[topic])
            data = response.json()
            return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
        else:
            headers = {
                "X-Api-Key": api_key
            }
            response = requests.get(topics[topic], headers=headers)
            data = response.json()
            return data["fact"]
    else:
        return "Sorry, that topic is not available."

def quiz(topic):
    """
    Presents a multiple-choice quiz to the user for the specified topic.
    """
    question, correct_answer, incorrect_answers = get_random_fact(topic)
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    print(f"Question: {question}")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Displays a menu for the user to select a topic, then runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic in topics:
        print(f"{topic}")

    selected_topic = input("Enter your choice: ")

    quiz(selected_topic)

if __name__ == "__main__":
    main()
