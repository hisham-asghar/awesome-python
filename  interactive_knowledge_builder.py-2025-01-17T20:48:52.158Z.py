
import random
import requests
import json

# Define the topics and their corresponding API endpoints
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for the API-Ninjas service
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using the API.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Fetch a multiple-choice quiz question from the specified topic using the API.
    """
    url = TOPICS[topic] + "/quiz"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return {
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"]
    }

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")

    # Display the menu of topics
    for topic in TOPICS:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in TOPICS:
        # Display a random fact or concept from the selected topic
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact:")
        print(fact)

        # Quiz the user on the selected topic
        quiz_data = quiz_question(selected_topic)
        print(f"\nNow, let's test your {selected_topic.lower()} knowledge!")
        print(quiz_data["question"])
        for i, option in enumerate(quiz_data["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if quiz_data["options"][user_answer - 1] == quiz_data["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['answer']}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
