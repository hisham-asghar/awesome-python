
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

# Function to display a multiple-choice quiz question
def display_quiz_question(topic):
    # Fetch a random question and answers from the selected topic
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "/quiz"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data['question']
    answers = data['answers']
    correct_answer = data['correct_answer']

    # Display the question and answers
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main program loop
while True:
    # Display the topic menu
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        # Fetch and display a random fact or concept
        fact = get_random_fact(selected_topic)
        print(f"\n{selected_topic} fact: {fact['fact']}")

        # Display a quiz question
        display_quiz_question(selected_topic)

        # Ask the user if they want to continue
        continue_input = input("\nDo you want to try another topic? (y/n) ")
        if continue_input.lower() != 'y':
            break
    else:
        print("Invalid topic. Please try again.")
