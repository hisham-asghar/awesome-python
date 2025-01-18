
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    return selected_topic

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    print(f"\nHere's a {topic.lower()} fact for you:")
    print(fact["fact"])

    # Multiple-choice quiz
    print("\nTest your knowledge with a quiz:")
    question = fact["question"]
    options = fact["options"]
    correct_answer = fact["answer"]

    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Oops, the correct answer is: {correct_answer}")

# Main function
def main():
    selected_topic = display_menu()
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
