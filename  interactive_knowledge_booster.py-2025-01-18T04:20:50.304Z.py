
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/trivia?category=science",
    "Technology": "https://api.api-ninjas.com/v1/trivia?category=technology",
    "History": "https://api.api-ninjas.com/v1/trivia?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia?category=general"
}

# API key for API-Ninjas
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Select 3 random questions from the topic
    questions = random.sample(data, 3)
    
    score = 0
    for question in questions:
        print(question["question"])
        
        # Display multiple-choice options
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        # Get user's answer
        user_answer = int(input("Enter your answer (1-4): "))
        
        # Check if the user's answer is correct
        if options[user_answer-1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    
    print(f"Your score: {score} out of 3")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the available topics
    for topic in TOPICS:
        print(f"- {topic}")
    
    chosen_topic = input("Enter your choice: ")
    
    if chosen_topic in TOPICS:
        print(f"\nHere's a random fact about {chosen_topic}:")
        print(get_random_fact(chosen_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
