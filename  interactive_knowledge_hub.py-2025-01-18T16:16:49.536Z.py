
import random
import requests
import json

# API endpoints for fetching educational content
API_ENDPOINTS = {
    'science': 'https://api.example.com/science',
    'technology': 'https://api.example.com/technology',
    'history': 'https://api.example.com/history',
    'general': 'https://api.example.com/general'
}

# Function to display a random fact or concept
def display_fact(topic):
    url = API_ENDPOINTS[topic]
    response = requests.get(url)
    data = json.loads(response.text)
    fact = random.choice(data['facts'])
    print(f"Did you know? {fact}")

# Function to run a quiz for the selected topic
def run_quiz(topic):
    url = API_ENDPOINTS[topic]
    response = requests.get(url)
    data = json.loads(response.text)
    questions = data['quiz_questions']
    
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
            print("Incorrect.")
    
    print(f"Your final score: {score}/{len(questions)}")

# Main function to handle user interaction
def main():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        display_fact('science')
        run_quiz('science')
    elif choice == 2:
        display_fact('technology')
        run_quiz('technology')
    elif choice == 3:
        display_fact('history')
        run_quiz('history')
    elif choice == 4:
        display_fact('general')
        run_quiz('general')
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
