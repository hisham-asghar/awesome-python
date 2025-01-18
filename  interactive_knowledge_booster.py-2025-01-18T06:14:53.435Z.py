
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

api_endpoints = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Define the API key (replace with your own)
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = api_endpoints[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if topic == "Science":
        return data[0]["fact"]
    elif topic == "Technology":
        return data[0]["fact"]
    elif topic == "History":
        return data[0]["fact"]
    elif topic == "General Knowledge":
        return data[0]["question"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    url = api_endpoints[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if topic == "Science":
        question = data[1]["question"]
        options = data[1]["options"]
        answer = data[1]["answer"]
    elif topic == "Technology":
        question = data[1]["question"]
        options = data[1]["options"]
        answer = data[1]["answer"]
    elif topic == "History":
        question = data[1]["question"]
        options = data[1]["options"]
        answer = data[1]["answer"]
    elif topic == "General Knowledge":
        question = data[1]["question"]
        options = data[1]["options"]
        answer = data[1]["answer"]
    
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f"\nRandom {topic} fact or concept:")
        print(get_random_fact(topic))
        
        print("\nNow let's test your knowledge with a quiz!")
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
