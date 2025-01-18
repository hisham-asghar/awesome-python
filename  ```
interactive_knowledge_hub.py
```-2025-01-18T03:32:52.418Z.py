
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to display a random fact or concept from the selected topic
def display_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = TOPICS[topic]
    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        fact = data[0]["fact"]
        print(f"Random {topic} fact: {fact}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function to run the interactive quiz
def run_quiz(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = TOPICS[topic]
    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        quiz_questions = random.sample(data, 3)

        for question in quiz_questions:
            print(question["question"])
            options = question["options"]
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")

            user_answer = int(input("Enter your answer (1-4): "))
            if options[user_answer - 1] == question["answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {question['answer']}")
            print()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")

    for topic in TOPICS:
        print(f"{topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in TOPICS:
        print(f"You selected: {selected_topic}")
        display_fact(selected_topic)
        print()
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
