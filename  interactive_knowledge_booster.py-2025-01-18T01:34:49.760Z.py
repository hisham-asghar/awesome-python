
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or trivia from the API
def get_random_fact_or_trivia(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    user_choice = input("Enter your choice: ").strip()
    return user_choice

# Function to display a random fact or trivia and quiz the user
def display_fact_and_quiz(topic):
    data = get_random_fact_or_trivia(topic)
    if topic == "General Knowledge":
        print(f"Trivia: {data['question']}")
        print("Options:")
        for i, option in enumerate(data['options'], start=1):
            print(f"{i}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == data['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {data['answer']}.")
    else:
        print(f"Random {topic.lower()} fact: {data['fact']}")

# Main function to run the program
def main():
    while True:
        user_choice = display_menu()
        if user_choice in topics:
            display_fact_and_quiz(user_choice)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
