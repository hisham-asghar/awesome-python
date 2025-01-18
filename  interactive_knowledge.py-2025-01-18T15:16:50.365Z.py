
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
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
    data = json.loads(response.text)
    return random.choice(data)

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    data = json.loads(response.text)
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]
    return question, choices, correct_answer

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    score = 0
    for i in range(5):
        question, choices, correct_answer = quiz_question(topic)
        print(f"Question {i+1}: {question}")
        for j, choice in enumerate(choices):
            print(f"{j+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    print(f"Your final score: {score}/5")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nLet's learn about {selected_topic}!")
        fact = get_random_fact(selected_topic)
        print(f"Did you know? {fact}")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
