
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][random.randint(0, len(data["results"]) - 1)]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[random.randint(0, len(data) - 1)]

# Function to run the interactive quiz
def run_quiz(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][random.randint(0, len(data["results"]) - 1)]
        print(f"Question: {question['question']}")
        print("Choices:")
        for i, choice in enumerate(question["incorrect_answers"]):
            print(f"{i+1}. {choice}")
        print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == len(question["incorrect_answers"]) + 1:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['correct_answer']}")
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = data[random.randint(0, len(data) - 1)]
        print(fact)

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"You selected: {selected_topic}")
        print("Fetching a random fact or concept...")
        fact = get_random_fact(selected_topic)
        print(f"Did you know? {fact}")
        print("Now, let's test your knowledge!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
