
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(TOPICS[topic])
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        response = requests.get(TOPICS[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    fact, correct_answer, incorrect_answers = get_random_fact(topic)
    print(f"Topic: {topic}")
    print(f"Fact or Concept: {fact}")

    # Combine the correct and incorrect answers and shuffle them
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    # Display the multiple-choice options
    print("Choose the correct answer:")
    for i, answer in enumerate(all_answers, start=1):
        print(f"{i}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter the number of your answer: "))

    # Check if the user's answer is correct
    if all_answers[user_answer - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to display the menu and run the interactive session
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    # Display the topic menu
    for i, topic in enumerate(TOPICS, start=1):
        print(f"{i}. {topic}")

    # Get the user's topic choice
    topic_choice = int(input("Enter the number of your topic choice: "))
    selected_topic = list(TOPICS.keys())[topic_choice - 1]

    # Run the interactive quiz for the selected topic
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
