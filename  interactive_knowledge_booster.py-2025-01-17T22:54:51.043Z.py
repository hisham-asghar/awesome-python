
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

# Function to display the multiple-choice quiz
def quiz(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic] + "?amount=5"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()

    score = 0
    for question in data:
        print(question['question'])
        choices = question['options']
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", choices[question['answer']-1])
    print(f"Your score: {score}/5")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print("\nHere's a random fact or concept from the", selected_topic, "topic:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
