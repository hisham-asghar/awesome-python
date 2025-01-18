
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

# Function to display the menu and get user's topic selection
def display_menu():
    print("Select a topic:")
    for topic in topics:
        print(f"{topic}")
    topic = input("Enter your choice: ")
    return topic

# Function to run the interactive quiz
def run_quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = fetch_quiz_data(topic)
    score = 0
    for question, choices, answer in quiz_data:
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", choices[answer-1])
    print(f"Your final score is {score}/{len(quiz_data)}")

# Function to fetch quiz data from a predefined database or API
def fetch_quiz_data(topic):
    # Implement the logic to fetch quiz data based on the selected topic
    # This can be done by querying a database or calling an API
    quiz_data = [
        ("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune", "Uranus"], 1),
        ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], 1),
        ("Which ancient civilization built the Great Pyramid of Giza?", ["Egyptians", "Greeks", "Romans", "Mayans"], 1)
    ]
    return quiz_data

# Main program loop
while True:
    topic = display_menu()
    random_fact = get_random_fact(topic)
    print(f"\nHere's a random {topic.lower()} fact: {random_fact}")
    run_quiz(topic)
    continue_option = input("\nDo you want to explore another topic? (y/n) ")
    if continue_option.lower() != "y":
        break
