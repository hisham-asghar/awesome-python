
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

def get_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using an API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = response.json()
    fact = random.choice(data)
    return fact

def quiz(topic):
    """
    Present a multiple-choice quiz for the specified topic.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = response.json()
    question = random.choice(data)
    choices = question["choices"]
    correct_answer = question["correct_answer"]

    print(question["question"])
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if choices[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    """
    Main function to run the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        fact = get_fact(selected_topic)
        print(f"\nHere's a random fact about {selected_topic}:")
        print(fact)

        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
