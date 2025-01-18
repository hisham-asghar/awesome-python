
import random
import requests
import json

# Define topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/randomfact?category=general"
}

# Define quiz questions and answers for each topic
quiz_data = {
    "Science": [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Jupiter", "Saturn", "Mars", "Venus"],
            "answer": 0
        },
        {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
            "answer": 0
        },
        # Add more science quiz questions here
    ],
    "Technology": [
        {
            "question": "What is the name of the first computer programming language?",
            "options": ["FORTRAN", "COBOL", "BASIC", "Ada"],
            "answer": 0
        },
        {
            "question": "What is the primary function of a computer's CPU?",
            "options": ["Data storage", "Input/Output", "Data processing", "Network communication"],
            "answer": 2
        },
        # Add more technology quiz questions here
    ],
    "History": [
        {
            "question": "What year did the American Civil War begin?",
            "options": ["1861", "1865", "1914", "1939"],
            "answer": 0
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
            "answer": 1
        },
        # Add more history quiz questions here
    ],
    "General Knowledge": [
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
            "answer": 3
        },
        # Add more general knowledge quiz questions here
    ]
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic using an API.
    """
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        fact = response.json()['fact']
        return fact
    else:
        return "Sorry, we couldn't fetch a fact for that topic."

def run_quiz(topic):
    """
    Runs a quiz for the specified topic, with multiple-choice questions.
    """
    print(f"Let's test your {topic} knowledge!")
    score = 0
    questions = quiz_data[topic]
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer - 1 == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Better luck next time!")
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    """
    Main function that displays the topic menu and runs the selected topic.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact: {fact}")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
