
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/randomfact?category=trivia"
}

# Define the quiz questions and answers
quiz_data = {
    "Science": [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
            "answer": 0
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Cu", "Pb"],
            "answer": 0
        }
    ],
    "Technology": [
        {
            "question": "What is the name of the first computer programming language?",
            "options": ["BASIC", "FORTRAN", "COBOL", "Ada"],
            "answer": 1
        },
        {
            "question": "What is the name of the device that converts digital signals into analog signals?",
            "options": ["Modem", "Router", "Switch", "Codec"],
            "answer": 3
        },
        {
            "question": "What is the name of the process by which data is transferred from one computer to another?",
            "options": ["Networking", "Encoding", "Encryption", "Transmission"],
            "answer": 3
        }
    ],
    "History": [
        {
            "question": "What year was the Declaration of Independence signed?",
            "options": ["1776", "1789", "1812", "1865"],
            "answer": 0
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "James Madison"],
            "answer": 2
        },
        {
            "question": "What event marked the end of World War II?",
            "options": ["D-Day", "The Holocaust", "The Atomic Bombings", "The Fall of Berlin"],
            "answer": 2
        }
    ],
    "General Knowledge": [
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "answer": 0
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
            "answer": 3
        },
        {
            "question": "What is the name of the tallest mountain in the world?",
            "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
            "answer": 0
        }
    ]
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic using the API.
    """
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    fact = response.json()['fact']
    return fact

def run_quiz(topic):
    """
    Runs a quiz for the specified topic, with multiple-choice questions.
    """
    questions = quiz_data[topic]
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    while True:
        print("\nPlease select a topic:")
        for topic in topics:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic}:")
            print(get_random_fact(selected_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
