
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

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        return random.choice(data["facts"])
    except (KeyError, IndexError, requests.exceptions.RequestException):
        return "Sorry, we couldn't fetch a fact for that topic right now."

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        question = random.choice(data["quiz_questions"])
        choices = question["choices"]
        random.shuffle(choices)
        return {
            "question": question["question"],
            "choices": choices,
            "answer": question["answer"]
        }
    except (KeyError, IndexError, requests.exceptions.RequestException):
        return {
            "question": "Sorry, we couldn't generate a quiz question for that topic right now.",
            "choices": [],
            "answer": ""
        }

def main():
    """
    The main function that interacts with the user.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz_data = quiz_question(selected_topic)
        print(quiz_data["question"])
        for i, choice in enumerate(quiz_data["choices"], start=1):
            print(f"{i}. {choice}")

        user_answer = int(input("Enter the number of the correct answer: "))
        if quiz_data["choices"][user_answer - 1] == quiz_data["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['answer']}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
