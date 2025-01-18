
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

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
            print("Incorrect. The correct answer is:", choices[answer-1])
    print(f"Your final score: {score}/{len(quiz_data)}")

# Main function to run the script
def main():
    topic = display_menu()
    print(f"\nHere's a random fact about {topic}:")
    print(get_random_fact(topic))
    print("\nNow, let's test your knowledge with a quiz!")
    run_quiz(topic)

if __name__ == "__main__":
    main()
