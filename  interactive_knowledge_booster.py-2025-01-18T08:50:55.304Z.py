
import random
import requests
import json

# API endpoints for fetching educational content
API_ENDPOINTS = {
    "science": "https://api.example.com/science",
    "technology": "https://api.example.com/technology",
    "history": "https://api.example.com/history",
    "general": "https://api.example.com/general"
}

# Multiple-choice questions and answers
QUIZ_DATA = {
    "science": [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Cu", "Fe"],
            "answer": 0
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Saturn", "Jupiter", "Mars", "Venus"],
            "answer": 1
        },
        # Add more science-related questions here
    ],
    "technology": [
        {
            "question": "What is the full form of CPU?",
            "options": ["Central Processing Unit", "Computer Processing Unit", "Compact Processor Unit", "Central Power Unit"],
            "answer": 0
        },
        {
            "question": "What is the primary function of a web browser?",
            "options": ["Sending emails", "Playing games", "Accessing websites", "Editing documents"],
            "answer": 2
        },
        # Add more technology-related questions here
    ],
    "history": [
        {
            "question": "In what year was the Declaration of Independence signed?",
            "options": ["1776", "1789", "1812", "1865"],
            "answer": 0
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
            "answer": 2
        },
        # Add more history-related questions here
    ],
    "general": [
        {
            "question": "What is the capital city of Australia?",
            "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
            "answer": 3
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3
        },
        # Add more general knowledge questions here
    ]
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API.
    """
    try:
        response = requests.get(API_ENDPOINTS[topic])
        data = json.loads(response.text)
        return random.choice(data)
    except (requests.exceptions.RequestException, KeyError):
        return "Sorry, we couldn't fetch a random fact for this topic."

def run_quiz(topic):
    """
    Runs a multiple-choice quiz for the specified topic.
    """
    questions = QUIZ_DATA[topic]
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in API_ENDPOINTS.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in API_ENDPOINTS:
        random_fact = get_random_fact(selected_topic)
        print(f"\nRandom {selected_topic.capitalize()} fact: {random_fact}")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
