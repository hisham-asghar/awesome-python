
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

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic.
    """
    fact = get_random_fact(topic)
    question = fact['question']
    options = fact['options']
    answer = fact['answer']

    print(f"Question: {question}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

def main():
    """
    Displays a menu for users to select a topic, then provides a random fact and a quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    topic_choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[topic_choice-1]

    print(f"\nRandom fact about {selected_topic}:")
    fact = get_random_fact(selected_topic)
    print(fact['fact'])

    print("\nNow let's test your knowledge!")
    quiz(selected_topic)

    print("\nThank you for using the Interactive Knowledge Booster!")

if __name__ == "__main__":
    main()
