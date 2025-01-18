Here is the Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding API endpoints
TOPICS = {
    "Science": "https://api.sampleapis.com/science/facts",
    "Technology": "https://api.sampleapis.com/tech/facts",
    "History": "https://api.sampleapis.com/history/facts",
    "General Knowledge": "https://api.sampleapis.com/generalknowledge/facts"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = TOPICS[topic]
    response = requests.get(api_url)
    facts = response.json()
    return random.choice(facts)

# Function to display the fact or concept and prompt the user for a quiz
def display_fact_and_quiz(topic, fact):
    print(f"Random {topic} fact: {fact['fact']}")
    print(f"Explanation: {fact['explanation']}")

    # Fetch quiz questions and answers for the topic
    quiz_url = f"{TOPICS[topic]}/quiz"
    quiz_response = requests.get(quiz_url)
    quiz_data = quiz_response.json()
    question = quiz_data["question"]
    options = quiz_data["options"]
    answer = quiz_data["answer"]

    # Display the quiz question and options
    print("\nTest your knowledge with a quiz!")
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    # Get the user's answer and check if it's correct
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

# Main function to run the interactive knowledge app
def run_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Select a topic to get started:")

    # Display the topic menu
    for i, topic in enumerate(TOPICS):
        print(f"{i+1}. {topic}")

    # Get the user's topic selection
    topic_choice = int(input("Enter the number of the topic (1-4): "))
    selected_topic = list(TOPICS)[topic_choice - 1]

    # Fetch and display a random fact or concept for the selected topic
    fact = get_random_fact(selected_topic)
    display_fact_and_quiz(selected_topic, fact)

    print("\nThank you for using the Interactive Knowledge App!")

# Run the main function
run_knowledge_app()