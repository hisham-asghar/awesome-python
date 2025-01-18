
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz_question(topic):
    """
    Generate a multiple-choice quiz question for the specified topic.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    data = response.json()
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]
    return question, choices, correct_answer

def main():
    """
    Main function that runs the interactive knowledge-boosting script.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to get started:")

    # Display the topic menu
    for topic in topics:
        print(f"- {topic}")

    chosen_topic = input("Enter your topic choice: ")

    if chosen_topic in topics:
        # Fetch a random fact or concept for the chosen topic
        fact = get_random_fact(chosen_topic)
        print(f"\nHere's a random {chosen_topic.lower()} fact for you:")
        print(fact)

        # Generate a multiple-choice quiz question for the chosen topic
        question, choices, correct_answer = quiz_question(chosen_topic)
        print(f"\nTest your knowledge with this {chosen_topic.lower()} quiz question:")
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer - 1] == correct_answer:
            print("Correct! You're a knowledge superstar.")
        else:
            print(f"Oops, the correct answer is: {correct_answer}")
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
