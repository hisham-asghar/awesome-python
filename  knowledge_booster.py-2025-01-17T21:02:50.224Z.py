
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    try:
        response = requests.get(topics[topic])
        data = response.json()
        return random.choice(data)
    except:
        return "Sorry, we couldn't fetch the information right now."

# Function to display the random fact or concept
def display_fact(fact):
    print(f"\nFact: {fact}")

# Function to create and display a multiple-choice quiz question
def quiz_question(topic):
    try:
        response = requests.get(topics[topic])
        data = response.json()
        question = random.choice(data)
        options = [question["answer"]] + question["distractors"]
        random.shuffle(options)
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    except:
        print("Sorry, we couldn't create a quiz question right now.")

# Main function to run the Knowledge Booster
def run_knowledge_booster():
    topic = display_menu()
    fact = get_random_fact(topic)
    display_fact(fact)
    quiz_question(topic)

if __name__ == "__main__":
    run_knowledge_booster()
