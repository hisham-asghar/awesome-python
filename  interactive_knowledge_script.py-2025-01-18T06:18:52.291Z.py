
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

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the selected topic using the API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

def quiz_question(topic):
    """
    Fetch a multiple-choice quiz question from the selected topic using the API.
    """
    url = topics[topic] + "/quiz"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return {
        'question': data['question'],
        'options': data['options'],
        'answer': data['answer']
    }

def main():
    """
    The main function that runs the interactive knowledge-sharing script.
    """
    print("Welcome to the Interactive Knowledge-Sharing Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz_data = quiz_question(selected_topic)
        print(quiz_data['question'])
        for i, option in enumerate(quiz_data['options']):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if quiz_data['options'][user_answer-1] == quiz_data['answer']:
            print("Correct! You're a knowledge champion.")
        else:
            print(f"Oops, the correct answer is: {quiz_data['answer']}")
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
