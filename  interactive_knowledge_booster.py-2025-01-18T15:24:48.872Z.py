
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/historicalevents",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = json.loads(response.text)
    return data[0]

# Function to display the menu and get the user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    print(f"\nHere's a {topic.lower()} fact for you:")
    print(fact['fact'])

    # Multiple-choice questions
    questions = [
        {
            "question": fact['question'],
            "options": fact['options'],
            "answer": fact['answer']
        }
    ]

    for question in questions:
        print("\nQuestion:", question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question['options'][question['answer']-1])

    print("\nThank you for participating! Keep learning and exploring.")

# Main function
def main():
    topic_choice = display_menu()
    run_quiz(topic_choice)

if __name__ == "__main__":
    main()
