
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to get a random fact from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the quiz question and get the user's answer
def quiz_question(topic):
    # Fetch quiz questions and answers from a database or API
    quiz_data = {
        "Science": [
            {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Cu", "Fe"], "correct": 0},
            {"question": "What is the largest planet in our solar system?", "answers": ["Mars", "Jupiter", "Saturn", "Neptune"], "correct": 1}
        ],
        "Technology": [
            {"question": "What is the primary programming language used for artificial intelligence?", "answers": ["Python", "Java", "C++", "Ruby"], "correct": 0},
            {"question": "Which company developed the first commercially successful smartphone?", "answers": ["Apple", "Samsung", "Nokia", "BlackBerry"], "correct": 3}
        ],
        "History": [
            {"question": "In what year did the United States declare independence?", "answers": ["1776", "1789", "1812", "1865"], "correct": 0},
            {"question": "Who was the first president of the United States?", "answers": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"], "correct": 2}
        ],
        "General Knowledge": [
            {"question": "What is the largest ocean on Earth?", "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "correct": 3},
            {"question": "What is the capital city of Australia?", "answers": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "correct": 3}
        ]
    }

    # Select a random question from the chosen topic
    question = random.choice(quiz_data[topic])
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    return question["correct"] == user_answer - 1

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        # Display a random fact from the selected topic
        print(f"\nFact about {selected_topic}:")
        print(get_random_fact(selected_topic))

        # Run the quiz for the selected topic
        print(f"\nTime for a {selected_topic} quiz!")
        if quiz_question(selected_topic):
            print("Correct! You're a knowledge champion!")
        else:
            print("Oops, that's not the right answer. Better luck next time!")

        # Ask the user if they want to continue
        continue_input = input("\nDo you want to try another topic? (y/n) ")
        if continue_input.lower() != "y":
            break
    else:
        print("Invalid topic. Please try again.")
