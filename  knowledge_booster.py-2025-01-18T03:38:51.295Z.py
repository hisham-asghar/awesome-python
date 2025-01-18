
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetch a random fact or concept from the chosen topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provide an interactive quiz for the chosen topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and its options
    question = random.choice(data)
    options = [question["answer"]] + question["options"]
    random.shuffle(options)
    
    print(f"Question: {question['question']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    if options[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function to display the menu and handle user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the menu of topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    user_choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[user_choice-1]
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_fact(topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
