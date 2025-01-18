
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using an API or predefined data.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    fact = random.choice(data["facts"])
    return fact

def quiz(topic):
    """
    Provide an interactive quiz for the selected topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    questions = data["questions"]
    score = 0

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
