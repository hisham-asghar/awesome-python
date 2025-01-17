
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your topic choice: ").capitalize()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch and display a random fact or concept
def display_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][random.randint(0, 9)]["question"]
    else:
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = data[random.randint(0, len(data) - 1)]["fact"]
    
    print(f"\nRandom {topic} fact or concept:\n{fact}")

# Function to run the interactive quiz
def run_quiz(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        questions = data["results"]
    else:
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        questions = [{"question": fact["fact"], "answers": [fact["fact"], fact["fact"].replace(" ", "-"), fact["fact"].split(" ")[0]]} for fact in data]
    
    score = 0
    for question in questions:
        print(f"\n{question['question']}")
        
        # Shuffle the answers
        answers = question["answers"]
        random.shuffle(answers)
        
        # Display the multiple-choice options
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        user_answer = int(input("Enter your answer (1-3): "))
        if answers[user_answer - 1] == question["answers"][0]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

# Main function to run the program
def main():
    topic = display_menu()
    display_random_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
