
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    topic_choice = input("Enter your choice: ")
    return topic_choice

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

# Function to display the fact or concept and run the quiz
def run_quiz(topic, fact):
    print(f"\nHere's a {topic.lower()} fact for you:")
    print(fact)

    # Generate multiple-choice questions
    questions = [
        {
            "question": "What is the main topic of this fact?",
            "options": [topic.lower(), "Random", "Unrelated"],
            "answer": 0
        },
        {
            "question": "How interesting do you find this fact?",
            "options": ["Very interesting", "Somewhat interesting", "Not interesting"],
            "answer": 0
        },
        {
            "question": "On a scale of 1-5, how much did you learn from this fact?",
            "options": ["1", "2", "3", "4", "5"],
            "answer": 3
        }
    ]

    # Run the quiz
    score = 0
    for question in questions:
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-3): "))
        if user_answer == question['answer'] + 1:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour score: {score}/{len(questions)}")

# Main function
def main():
    topic_choice = display_menu()
    if topic_choice in topics:
        fact = get_random_fact(topic_choice)
        if fact:
            run_quiz(topic_choice, fact['fact'])
        else:
            print("Sorry, we couldn't fetch a fact for the selected topic.")
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
