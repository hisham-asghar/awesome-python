
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Replace with your API key if using the API-Ninjas API
API_KEY = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetch a random fact or concept from the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if topic == "Science":
        fact = data[0]["fact"]
    elif topic == "Technology":
        fact = data[0]["fact"]
    elif topic == "History":
        fact = data[0]["fact"]
    elif topic == "General Knowledge":
        fact = data[0]["question"]
    
    return fact

def quiz(topic):
    """
    Provide a multiple-choice quiz for the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if topic == "Science":
        question = data[0]["question"]
        options = data[0]["options"]
        answer = data[0]["answer"]
    elif topic == "Technology":
        question = data[0]["question"]
        options = data[0]["options"]
        answer = data[0]["answer"]
    elif topic == "History":
        question = data[0]["question"]
        options = data[0]["options"]
        answer = data[0]["answer"]
    elif topic == "General Knowledge":
        question = data[0]["question"]
        options = data[0]["options"]
        answer = data[0]["answer"]
    
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
    
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_fact(selected_topic))
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
