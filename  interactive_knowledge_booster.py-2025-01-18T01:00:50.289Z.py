
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    chosen_topic = input("Enter your choice: ")
    return chosen_topic

# Function to run the interactive quiz
def run_quiz(topic):
    # Fetch a random fact or concept from the chosen topic
    fact = get_random_fact(topic)
    print(f"\nHere's a {topic} fact for you:")
    print(fact["fact"])

    # Ask the user a multiple-choice question
    print("\nTest your knowledge with this question:")
    print(fact["question"])
    for i, option in enumerate(fact["options"], start=1):
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))

    # Check the user's answer and provide feedback
    if user_answer == fact["answer"]:
        print("Correct! Well done.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

# Main function to run the script
def main():
    chosen_topic = display_menu()
    run_quiz(chosen_topic)

if __name__ == "__main__":
    main()
