
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    return random.choice(data)

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    api_url = topics[topic] + "/quiz"
    response = requests.get(api_url)
    data = json.loads(response.text)
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]
    return question, choices, correct_answer

def main():
    """
    The main function that runs the interactive knowledge-enhancing script.
    """
    print("Welcome to the Knowledge Enhancer!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        fact = get_random_fact(selected_topic)
        print(fact)

        print("\nLet's test your knowledge with a quiz!")
        question, choices, correct_answer = quiz_question(selected_topic)
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == correct_answer:
            print("Correct! You're a knowledge champion!")
        else:
            print(f"Oops, the correct answer is: {correct_answer}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
