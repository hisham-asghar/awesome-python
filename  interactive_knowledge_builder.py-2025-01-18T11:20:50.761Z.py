
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API or predefined data.
    """
    if topic in topics:
        # Use the API endpoint or predefined data to fetch a random fact
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        return random.choice(data)
    else:
        return "Sorry, that topic is not available."

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    if topic in topics:
        # Use the API endpoint or predefined data to fetch a random quiz question
        response = requests.get(topics[topic] + "/quiz")
        data = json.loads(response.text)
        question = data["question"]
        choices = data["choices"]
        correct_answer = data["correct_answer"]
        return {
            "question": question,
            "choices": choices,
            "correct_answer": correct_answer
        }
    else:
        return {
            "question": "Sorry, that topic is not available.",
            "choices": [],
            "correct_answer": ""
        }

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    chosen_topic = input("Enter your choice: ")

    print(f"\nHere's a random fact about {chosen_topic}:")
    print(get_random_fact(chosen_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz_data = quiz_question(chosen_topic)
    print(quiz_data["question"])
    for i, choice in enumerate(quiz_data["choices"]):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-{}): ".format(len(quiz_data["choices"]))))
    if quiz_data["choices"][user_answer-1] == quiz_data["correct_answer"]:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
