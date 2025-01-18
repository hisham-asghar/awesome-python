
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
        return random.choice(data['facts'])
    except:
        return "Sorry, we couldn't fetch a random fact for that topic."

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic] + "/quiz")
        data = json.loads(response.text)
        score = 0
        for question in data['questions']:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"Your score: {score}/{len(data['questions'])}")
    except:
        print("Sorry, we couldn't load the quiz for that topic.")

def main():
    """
    The main function that displays the menu and handles user interaction.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        user_topic = input("Enter your choice (or 'q' to quit): ")
        if user_topic.lower() == 'q':
            break
        if user_topic in topics:
            print("\nHere's a random fact about", user_topic + ":")
            print(get_random_fact(user_topic))
            print("\nNow, let's test your knowledge!")
            quiz(user_topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
