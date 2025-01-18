
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    return random.choice(data)

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    # Select a random question and its options
    question = random.choice(data["questions"])
    options = question["options"]
    
    print(question["text"])
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check if the user's answer is correct
    if options[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get user's topic choice
    choice = int(input("Enter your choice (1-4): "))
    topic = list(topics.keys())[choice-1]
    
    # Fetch a random fact or concept and display it
    fact = get_fact(topic)
    print(f"\nDid you know? {fact}")
    
    # Run the quiz for the selected topic
    quiz(topic)

if __name__ == "__main__":
    main()
