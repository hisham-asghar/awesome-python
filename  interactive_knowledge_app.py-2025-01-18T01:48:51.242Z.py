
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
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

# Function to display the menu and get user's topic selection
def display_menu():
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        return selected_topic
    else:
        print("Invalid topic. Please try again.")
        return None

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    if fact:
        print(f"\nHere's a {topic.lower()} fact:")
        print(f"{fact['fact']}")
        
        # Multiple-choice questions
        questions = [
            {
                "question": fact["question"],
                "options": fact["options"],
                "answer": fact["answer"]
            }
        ]
        
        score = 0
        for question in questions:
            print(f"\n{question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", question['options'][question['answer']-1])
        
        print(f"\nYour score: {score}/{len(questions)}")
    else:
        print("Failed to fetch data. Please try again later.")

# Main program loop
while True:
    selected_topic = display_menu()
    if selected_topic:
        run_quiz(selected_topic)
    
    continue_prompt = input("\nDo you want to try another topic? (y/n) ")
    if continue_prompt.lower() != 'y':
        break

print("Thank you for using the interactive knowledge app!")
