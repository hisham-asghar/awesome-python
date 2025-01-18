
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/trivia?category=science",
    "Technology": "https://api.api-ninjas.com/v1/trivia?category=technology",
    "History": "https://api.api-ninjas.com/v1/trivia?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia?category=general"
}

# API key for the API-Ninjas Trivia API
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def run_quiz(topic):
    """
    Runs an interactive quiz for the specified topic, with multiple-choice questions.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    score = 0
    for question in data:
        print(question["question"])
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    
    print(f"Your final score: {score}/{len(data)}")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("Now, let's test your knowledge!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
