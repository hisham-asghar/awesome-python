
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    1: 'Science',
    2: 'Technology',
    3: 'History',
    4: 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept for the selected topic.
    """
    if topic == 1:
        # Fetch a random science fact using an API or from a predefined database
        return "The Earth is the only planet in our solar system with liquid water on its surface."
    elif topic == 2:
        # Fetch a random technology fact using an API or from a predefined database
        return "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons."
    elif topic == 3:
        # Fetch a random history fact using an API or from a predefined database
        return "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles."
    elif topic == 4:
        # Fetch a random general knowledge fact using an API or from a predefined database
        return "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
    else:
        return "Sorry, we don't have any facts for that topic yet."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic.
    """
    if topic == 1:
        # Define science quiz questions and answers
        question = "What is the chemical symbol for gold?"
        choices = ['Au', 'Ag', 'Cu', 'Fe']
        answer = 0
    elif topic == 2:
        # Define technology quiz questions and answers
        question = "Who is considered the father of the World Wide Web?"
        choices = ['Bill Gates', 'Steve Jobs', 'Tim Berners-Lee', 'Linus Torvalds']
        answer = 2
    elif topic == 3:
        # Define history quiz questions and answers
        question = "Which ancient civilization built the Pyramids of Giza?"
        choices = ['Mesopotamians', 'Egyptians', 'Greeks', 'Romans']
        answer = 1
    elif topic == 4:
        # Define general knowledge quiz questions and answers
        question = "What is the largest planet in our solar system?"
        choices = ['Earth', 'Mars', 'Jupiter', 'Saturn']
        answer = 2
    else:
        return "Sorry, we don't have a quiz for that topic yet."

    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", choices[answer])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    selected_topic = int(input("Enter the topic number (1-4): "))

    print(f"You selected: {topics[selected_topic]}")
    print(get_random_fact(selected_topic))
    quiz(selected_topic)

if __name__ == "__main__":
    main()
