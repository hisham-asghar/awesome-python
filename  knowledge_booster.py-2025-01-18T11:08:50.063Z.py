
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

# Function to display the multiple-choice quiz
def quiz(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "?amount=5"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()

    score = 0
    for question in data:
        print(question["question"])
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    print(f"Your final score: {score}/5")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to get started:")

    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"\nA random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
