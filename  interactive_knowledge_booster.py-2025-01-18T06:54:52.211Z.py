
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
    Fetches a random fact or concept from the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic, with multiple-choice questions.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and its choices
    question = random.choice(data)
    choices = [question["answer"]] + question["choices"]
    random.shuffle(choices)
    
    print(f"Question: {question['question']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    
    while True:
        user_answer = input("Enter the number of your answer (or 'q' to quit): ")
        if user_answer.lower() == 'q':
            break
        try:
            selected_choice = int(user_answer)
            if selected_choice == choices.index(question["answer"]) + 1:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['answer']}")
            break
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    """
    The main function that displays the menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    while True:
        try:
            user_choice = int(input("Enter the number of your choice (or 'q' to quit): "))
            if user_choice == 'q':
                print("Goodbye!")
                break
            topic = list(topics.keys())[user_choice - 1]
            print(f"\nRandom fact about {topic}: {get_random_fact(topic)}")
            quiz(topic)
            print()
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
