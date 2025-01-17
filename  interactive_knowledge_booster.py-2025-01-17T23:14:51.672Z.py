
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

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
    # Fetch quiz questions and answers from the API or predefined database
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic] + "?limit=3"  # Fetch 3 quiz questions
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    quiz_data = response.json()

    score = 0
    for question in quiz_data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", question['answer'])
    print(f"Your final score: {score}/{len(quiz_data)}")

# Main program loop
while True:
    selected_topic = display_menu()
    if selected_topic in topics:
        print("\nHere's a random fact or concept from the", selected_topic, "topic:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
        break
    else:
        print("Invalid topic. Please try again.")
