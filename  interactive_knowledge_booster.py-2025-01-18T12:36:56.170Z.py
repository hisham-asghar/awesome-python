
import random
import requests
import json

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter your choice (1-4): ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    else:
        return "Invalid topic."

    if response.status_code == 200:
        facts = response.json()
        return random.choice(facts)["fact"]
    else:
        return "Error fetching data."

# Function to display a quiz and get the user's answer
def quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=17&type=multiple", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "Technology":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "History":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=23&type=multiple", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    elif topic == "General Knowledge":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=9&type=multiple", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    else:
        return "Invalid topic."

    if response.status_code == 200:
        quiz_data = response.json()["results"][0]
        question = quiz_data["question"]
        answers = quiz_data["incorrect_answers"] + [quiz_data["correct_answer"]]
        random.shuffle(answers)

        print(f"Question: {question}")
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")

        user_answer = input("Enter your answer (1-4): ")
        if answers[int(user_answer) - 1] == quiz_data["correct_answer"]:
            return "Correct!"
        else:
            return "Incorrect. The correct answer is: " + quiz_data["correct_answer"]
    else:
        return "Error fetching quiz data."

# Main program loop
while True:
    user_choice = display_menu()
    if user_choice in topics:
        topic = topics[user_choice]
        print(f"\nRandom {topic} fact: {get_random_fact(topic)}")
        print(f"\n{topic} quiz: {quiz(topic)}")
    else:
        print("Invalid choice. Please try again.")
    print("\nPress Enter to continue, or type 'exit' to quit.")
    if input().lower() == "exit":
        break
