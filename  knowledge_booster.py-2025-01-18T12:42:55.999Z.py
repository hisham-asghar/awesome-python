
# Knowledge Booster - An Interactive Learning Experience
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url)
    data = response.json()
    return random.choice(data)

# Function to display a multiple-choice quiz question
def quiz_question(topic):
    api_url = topics[topic] + "/quiz"
    response = requests.get(api_url)
    data = response.json()
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]

    print(f"Question: {question}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to run the interactive learning experience
def main():
    print("Welcome to Knowledge Booster!")
    print("Select a topic to get started:")

    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    topic_choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[topic_choice - 1]

    # Get a random fact or concept and display it
    fact = get_random_fact(selected_topic)
    print(f"\nFact about {selected_topic}: {fact}")

    # Run the quiz
    print(f"\nNow, let's test your {selected_topic} knowledge!")
    quiz_question(selected_topic)

if __name__ == "__main__":
    main()
