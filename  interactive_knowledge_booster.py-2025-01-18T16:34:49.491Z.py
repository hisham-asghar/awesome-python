
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
    Fetch a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        return random.choice(data)
    except (requests.exceptions.RequestException, KeyError, IndexError):
        return "Sorry, we couldn't fetch a fact for that topic right now."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        question = random.choice(data)
        choices = question["choices"]
        random.shuffle(choices)
        print(f"Question: {question['question']}")
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if choices[user_answer - 1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    except (requests.exceptions.RequestException, KeyError, IndexError, ValueError):
        print("Sorry, we couldn't load the quiz for that topic right now.")

def main():
    """
    Main function to display the menu and handle user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        user_topic = input("Enter your choice (or 'q' to quit): ")
        if user_topic.lower() == "q":
            break
        if user_topic in topics:
            fact = get_random_fact(user_topic)
            print(f"\nFact about {user_topic}: {fact}")
            quiz(topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
