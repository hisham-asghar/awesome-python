
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Define the multiple-choice questions and answers for each topic
questions = {
    "Science": [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
            "answer": 0
        },
        {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
            "answer": 0
        },
        # Add more science questions here
    ],
    "Technology": [
        {
            "question": "What is the name of the first computer programmer?",
            "options": ["Charles Babbage", "Ada Lovelace", "Alan Turing", "Steve Jobs"],
            "answer": 1
        },
        {
            "question": "What is the name of the operating system developed by Apple?",
            "options": ["Windows", "Linux", "macOS", "Android"],
            "answer": 2
        },
        # Add more technology questions here
    ],
    "History": [
        {
            "question": "What year was the Declaration of Independence signed?",
            "options": ["1776", "1789", "1812", "1865"],
            "answer": 0
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"],
            "answer": 1
        },
        # Add more history questions here
    ],
    "General Knowledge": [
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
    Fetch a random fact from the specified topic using the API.
    """
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    fact = response.json()["fact"]
    return fact

def quiz(topic):
    """
    Run a multiple-choice quiz for the specified topic.
    """
    print(f"Welcome to the {topic} quiz!")
    score = 0
    for question in questions[topic]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions[topic])}")

def main():
    """
    Main function to run the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")
        if selected_topic in topics:
            fact = get_random_fact(selected_topic)
            print(f"\nHere's a random fact about {selected_topic}:")
            print(fact)
            quiz(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
