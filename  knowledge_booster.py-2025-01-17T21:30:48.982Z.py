
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "1. Science": "https://api.example.com/science",
    "2. Technology": "https://api.example.com/technology",
    "3. History": "https://api.example.com/history",
    "4. General Knowledge": "https://api.example.com/general"
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
            print("Incorrect. The correct answer is", question["answer"])
    print(f"Your final score is {score}/{len(quiz_data)}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(topic)

    user_choice = input("Enter the number of the topic (1-4): ")
    if user_choice in topics:
        fact = get_random_fact(user_choice)
        print(f"Here's a random fact about {user_choice.split('.')[1]}:")
        print(fact)
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(user_choice)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
