
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API.
    """
    api_key = "your_api_key_here"
    url = f"https://api.example.com/facts?topic={topic}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz_questions(topic):
    """
    Fetches multiple-choice quiz questions for the selected topic using a public API.
    """
    api_key = "your_api_key_here"
    url = f"https://api.example.com/quiz?topic={topic}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def run_quiz(topic):
    """
    Runs an interactive quiz for the selected topic.
    """
    questions = quiz_questions(topic)
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    """
    Displays a menu for users to select a topic and run the interactive knowledge session.
    """
    topics = ["Science", "Technology", "History", "General Knowledge"]
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic}")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Goodbye!")
            break
        elif 1 <= choice <= 4:
            topic = topics[choice-1]
            print(f"\nRandom fact about {topic}: {get_random_fact(topic)}")
            run_quiz(topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
