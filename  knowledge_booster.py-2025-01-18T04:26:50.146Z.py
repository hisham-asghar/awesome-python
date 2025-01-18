
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using an API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    return random.choice(data)

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    question = random.choice(data)
    options = question["options"]
    correct_answer = question["correct_answer"]

    print(question["question"])
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    """
    The main function that presents the menu and handles user interactions.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")

    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        fact = get_random_fact(selected_topic)
        print(fact)

        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
