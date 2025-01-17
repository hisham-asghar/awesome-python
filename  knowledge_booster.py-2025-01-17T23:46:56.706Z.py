Here is the raw Python code without any additional commentary:

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

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return data[0]['fact']

# Function to display the interactive quiz
def quiz(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    question = data[0]['question']
    options = data[0]['options']
    answer = data[0]['answer']

    print(f"Question: {question}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

# Main function to run the interactive learning experience
def main():
    print("Welcome to the Knowledge Booster!")
    print("Select a topic to get started:")

    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()