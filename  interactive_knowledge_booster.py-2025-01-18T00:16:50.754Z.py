
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to fetch a random fact from the API
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        facts = response.json()
        return random.choice(facts)['fact']
    else:
        return "Sorry, we couldn't fetch a fact at the moment."

# Function to display the menu and get user's topic choice
def get_topic_choice():
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    # Fetch 5 random multiple-choice questions from the API
    url = f"https://api.api-ninjas.com/v1/trivia?category={topic.lower()}&limit=5"
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        questions = response.json()
        score = 0
        for question in questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.")
        print(f"Your score: {score}/5")
    else:
        print("Sorry, we couldn't fetch the quiz questions at the moment.")

# Main program loop
while True:
    topic_choice = get_topic_choice()
    if topic_choice in topics:
        print(f"\nHere's a random fact about {topic_choice}:")
        print(get_random_fact(topic_choice))
        print("\nNow, let's test your knowledge!")
        run_quiz(topic_choice)
        break
    else:
        print("Invalid topic choice. Please try again.")
