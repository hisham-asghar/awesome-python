
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][0]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return random.choice(data)

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to display the random fact or concept and the interactive quiz
def interactive_quiz(topic, fact):
    print(f"\nHere's a {topic.lower()} fact for you:")
    if topic == "General Knowledge":
        print(fact["question"])
        answers = fact["incorrect_answers"] + [fact["correct_answer"]]
        random.shuffle(answers)
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if answers[user_answer-1] == fact["correct_answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print(f"Oops, the correct answer is {fact['correct_answer']}.")
    else:
        print(fact["fact"])

# Main function to run the script
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    interactive_quiz(topic, fact)

if __name__ == "__main__":
    main()
