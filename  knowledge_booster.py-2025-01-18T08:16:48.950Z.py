
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/trivia?category=science",
    "Technology": "https://api.api-ninjas.com/v1/trivia?category=technology",
    "History": "https://api.api-ninjas.com/v1/trivia?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia?category=general"
}

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_trivia(topic):
    """
    Fetches a random trivia fact from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]

def quiz(topic):
    """
    Presents a multiple-choice quiz for the specified topic.
    """
    trivia = get_trivia(topic)
    print(f"Question: {trivia['question']}")
    print("Options:")
    options = [trivia['answer']] + trivia['options']
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == trivia['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {trivia['answer']}")

def main():
    """
    Displays the topic menu, prompts the user to select a topic, and runs the quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"You selected: {selected_topic}")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
