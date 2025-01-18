Here is the raw Python code without any additional commentary:

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
    # Use a public API or predefined database to fetch the information
    # Example using the 'uselessfacts' API
    if topic == "Science":
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?category=science")
    elif topic == "Technology":
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?category=technology")
    elif topic == "History":
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?category=history")
    else:
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")

    if response.status_code == 200:
        fact = response.json()["text"]
        return fact
    else:
        return "Sorry, we couldn't fetch a random fact at the moment."

# Function to display a quiz for the selected topic
def quiz(topic):
    # Prepare the quiz questions and answers based on the selected topic
    # Example using predefined questions and answers
    if topic == "Science":
        questions = [
            "What is the chemical symbol for gold?",
            "Which planet in our solar system is known as the 'Red Planet'?",
            "What is the name of the process by which plants convert sunlight into energy?"
        ]
        answers = ["Au", "Mars", "Photosynthesis"]
    elif topic == "Technology":
        questions = [
            "What is the name of the first commercially available personal computer?",
            "Which company created the Android operating system?",
            "What is the name of the programming language used to develop websites?"
        ]
        answers = ["Apple II", "Google", "JavaScript"]
    elif topic == "History":
        questions = [
            "In which year did the American Civil War begin?",
            "Who was the first president of the United States?",
            "What was the name of the ancient Egyptian civilization that built the pyramids?"
        ]
        answers = ["1861", "George Washington", "Ancient Egypt"]
    else:
        questions = [
            "What is the largest planet in our solar system?",
            "What is the capital city of Australia?",
            "Who invented the telephone?"
        ]
        answers = ["Jupiter", "Canberra", "Alexander Graham Bell"]

    # Ask the user the quiz questions and keep track of the score
    score = 0
    for i, question in enumerate(questions):
        print(question)
        user_answer = input("Enter your answer: ")
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answers[i])
    print(f"Your final score is: {score}/{len(questions)}")

# Main function to run the interactive knowledge booster
def main():
    user_choice = display_menu()
    if user_choice in topics:
        topic = topics[user_choice]
        print(f"You have selected the topic: {topic}")
        print(get_random_fact(topic))
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()