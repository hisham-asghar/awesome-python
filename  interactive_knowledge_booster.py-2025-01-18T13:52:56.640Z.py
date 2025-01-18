
import random
import requests
import json

# Define the available topics
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_id):
    topic_name = topics[topic_id]
    
    # Fetch data from a public API or predefined database
    if topic_id == 1:  # Science
        response = requests.get("https://api.example.com/science/random")
        data = response.json()
        fact = data["fact"]
    elif topic_id == 2:  # Technology
        response = requests.get("https://api.example.com/technology/random")
        data = response.json()
        fact = data["fact"]
    elif topic_id == 3:  # History
        response = requests.get("https://api.example.com/history/random")
        data = response.json()
        fact = data["fact"]
    else:  # General Knowledge
        facts = [
            "The largest planet in our solar system is Jupiter.",
            "The Great Wall of China is the longest man-made structure in the world.",
            "The Mona Lisa is a painting by the Italian artist Leonardo da Vinci."
        ]
        fact = random.choice(facts)
    
    print(f"\nHere's a random {topic_name} fact for you:")
    print(f"- {fact}")

# Function to display the quiz and get user answers
def quiz_time(topic_id):
    topic_name = topics[topic_id]
    print(f"\nTime for a {topic_name} quiz!")
    
    # Fetch quiz questions and answers from a public API or predefined database
    if topic_id == 1:  # Science
        response = requests.get("https://api.example.com/science/quiz")
        data = response.json()
    elif topic_id == 2:  # Technology
        response = requests.get("https://api.example.com/technology/quiz")
        data = response.json()
    elif topic_id == 3:  # History
        response = requests.get("https://api.example.com/history/quiz")
        data = response.json()
    else:  # General Knowledge
        data = {
            "questions": [
                "What is the capital of Australia?",
                "Who wrote the novel 'To Kill a Mockingbird'?",
                "What is the largest ocean on Earth?"
            ],
            "answers": ["Canberra", "Harper Lee", "Pacific Ocean"]
        }
    
    score = 0
    for i, question in enumerate(data["questions"]):
        print(f"Question {i+1}: {question}")
        for option in ["A", "B", "C", "D"]:
            print(f"{option}) {data['answers'][i*4 + ord(option) - 65]}")
        user_answer = input("Your answer (A-D): ").upper()
        if user_answer == "ABCD"[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"\nYour final score is {score} out of {len(data['questions'])}")

# Main program loop
while True:
    topic_choice = display_menu()
    get_random_fact(topic_choice)
    quiz_time(topic_choice)
    
    play_again = input("\nWould you like to try another topic? (y/n) ").lower()
    if play_again != "y":
        print("Thanks for using the Interactive Knowledge Booster!")
        break
