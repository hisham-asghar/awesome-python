Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define topics and their corresponding API endpoints
TOPICS = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API.
    """
    url = TOPICS[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using a public API.
    """
    url = TOPICS[topic] + "/quiz"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    """
    The main function that provides an interactive menu for users to select a topic,
    displays a random fact or concept, and tests their knowledge with a quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic in TOPICS:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in TOPICS:
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact or concept:")
        print(fact)

        quiz_data = quiz_question(selected_topic)
        print("\nLet's test your knowledge with a quiz!")
        print(quiz_data["question"])
        for option in quiz_data["options"]:
            print(f"- {option}")

        user_answer = input("Enter your answer: ")
        if user_answer == quiz_data["correct_answer"]:
            print("Correct! You're a knowledge champion!")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
