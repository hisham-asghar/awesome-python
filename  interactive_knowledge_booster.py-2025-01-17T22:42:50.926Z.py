
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and its options
    question = random.choice(data)
    options = [question["fact"]] + [random.choice(data)["fact"] for _ in range(3)]
    random.shuffle(options)
    
    print(f"Question: {question['fact']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer and check if it's correct
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == question["fact"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {options.index(question['fact'])+1}.")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    user_choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[user_choice-1]
    
    print(f"\nRandom fact about {selected_topic}:")
    print(get_random_fact(selected_topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(selected_topic)

if __name__ == "__main__":
    main()
