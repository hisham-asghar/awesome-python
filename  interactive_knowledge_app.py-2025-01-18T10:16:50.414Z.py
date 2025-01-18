
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
    Fetch a random fact or concept from the selected topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

def quiz_question(topic):
    """
    Generate a multiple-choice quiz question for the selected topic.
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
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    # Display the topic menu
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        # Fetch a random fact or concept from the selected topic
        fact = get_random_fact(selected_topic)
        print(f"\nFact about {selected_topic}: {fact}")

        # Generate a multiple-choice quiz question for the selected topic
        question, choices, correct_answer = quiz_question(selected_topic)
        print(f"\nQuiz Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == correct_answer:
            print("Correct! You've increased your knowledge.")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
