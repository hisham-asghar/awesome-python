
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    quiz_data = response.json()

    score = 0
    for question in quiz_data:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    print(f"Your final score: {score}/{len(quiz_data)}")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic in topics:
        print(f"{topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print("\nHere's a random fact or concept from the", selected_topic, "topic:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
