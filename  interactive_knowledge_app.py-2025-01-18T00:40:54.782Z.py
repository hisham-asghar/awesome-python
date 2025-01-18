Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return data[0]['fact']

# Function to generate a multiple-choice quiz question
def generate_quiz_question(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    question = data[0]['question']
    choices = data[0]['choices']
    answer = data[0]['answer']
    return question, choices, answer

# Main function to run the interactive knowledge app
def run_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")

    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        selected_topic = input("Enter your choice: ")

        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic}:")
            print(get_random_fact(selected_topic))

            print("\nLet's test your knowledge with a quiz!")
            question, choices, answer = generate_quiz_question(selected_topic)
            print(question)
            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice}")
            user_answer = int(input("Enter your answer (1-4): "))
            if choices[user_answer-1] == answer:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {answer}")
        else:
            print("Invalid topic. Please try again.")

# Run the knowledge app
run_knowledge_app()