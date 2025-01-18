
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        fact = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return fact, choices
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = random.choice(data)
        return fact["fact"]

# Function to display the menu and get the user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    while True:
        user_input = input("Enter your choice: ").capitalize()
        if user_input in topics:
            return user_input
        else:
            print("Invalid choice. Please try again.")

# Function to run the interactive quiz
def run_quiz(topic):
    fact, choices = get_random_fact(topic)
    print(f"Here's a {topic.lower()} fact for you:")
    print(fact)
    print("Multiple-choice question:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    while True:
        user_answer = input("Enter the number of the correct answer: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
            if choices[int(user_answer) - 1] == choices[-1]:
                print("Correct! Great job!")
                return
            else:
                print("Oops, that's not the right answer. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and", len(choices))

# Main function to run the script
def main():
    topic = display_menu()
    run_quiz(topic)

if __name__ == "__main__":
    main()
