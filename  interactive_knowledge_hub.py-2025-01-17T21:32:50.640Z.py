
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

# API key for API-Ninjas (replace with your own if using a different source)
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using an API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    answers = [correct_answer] + question["incorrect_answers"]
    random.shuffle(answers)
    
    print(f"Question: {question['question']}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Displays the topic menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    user_choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[user_choice-1]
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_random_fact(topic))
    
    print("\nNow let's test your knowledge!")
    quiz(topic)

if __name__ == "__main__":
    main()
