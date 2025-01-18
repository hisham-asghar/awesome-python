Here is the raw Python code extracted from the JSON:

```python
# knowledge_booster.py

import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = response.json()
        return random.choice(data)
    except (requests.exceptions.RequestException, KeyError):
        return "Sorry, we couldn't fetch a random fact for that topic."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic] + "/quiz")
        quiz_data = response.json()
        question = quiz_data["question"]
        choices = quiz_data["choices"]
        correct_answer = quiz_data["correct_answer"]

        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    except (requests.exceptions.RequestException, KeyError):
        print("Sorry, we couldn't load the quiz for that topic.")

def main():
    """
    Displays a menu for users to select a topic, then provides a random fact and a quiz.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")

    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
