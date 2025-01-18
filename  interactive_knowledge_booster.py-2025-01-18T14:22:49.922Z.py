
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

# Function to get a random fact or concept from the selected topic
def get_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    fact, correct_answer, incorrect_answers = get_fact(topic)
    print(f"Topic: {topic}")
    print(f"Fact or Concept: {fact}")

    # Shuffle the answers
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    # Display the multiple-choice options
    print("Choose the correct answer:")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Your answer (1-4): "))
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to display the menu and run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    # Display the available topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    # Get the user's topic choice
    choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[choice-1]

    # Run the quiz for the selected topic
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
