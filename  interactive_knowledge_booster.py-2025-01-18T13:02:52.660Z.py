
import random
import requests
import json

# Define topics and their corresponding API endpoints
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
    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data[0]["fact"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

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
    # Fetch quiz questions and answers from a predefined database
    quiz_data = get_quiz_data(topic)

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
            print("Incorrect. The correct answer is:", choices[answer-1])
    print(f"Your final score: {score} out of {len(quiz_data)}")

# Function to fetch quiz data from a predefined database
def get_quiz_data(topic):
    # Replace this with your own quiz data retrieval logic
    quiz_data = [
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Cu", "Fe"], 1),
        ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Marie Curie"], 1),
        ("In which year did World War II end?", ["1945", "1939", "1941", "1947"], 1),
        ("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Mars", "Earth"], 1)
    ]
    return quiz_data

def main():
    selected_topic = display_menu()
    print(f"\nYour selected topic is: {selected_topic}")
    print(f"Random fact about {selected_topic.lower()}: {get_random_fact(selected_topic)}")
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
