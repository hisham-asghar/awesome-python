
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][random.randint(0, 9)]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[random.randint(0, len(data) - 1)]

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to display the random fact or concept and the interactive quiz
def run_knowledge_booster():
    topic = display_menu()
    fact = get_random_fact(topic)

    print(f"\nYour {topic} fact/concept:")
    if topic == "General Knowledge":
        print(f"Question: {fact['question']}")
        print(f"Correct answer: {fact['correct_answer']}")
        print(f"Incorrect answers: {', '.join(fact['incorrect_answers'])}")
    else:
        print(fact["fact"])

    input("\nPress Enter to start the quiz...")

    if topic == "General Knowledge":
        answers = fact["incorrect_answers"]
        answers.append(fact["correct_answer"])
        random.shuffle(answers)

        print(f"\nQuestion: {fact['question']}")
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")

        user_answer = int(input("Enter the number of the correct answer: "))
        if answers[user_answer - 1] == fact["correct_answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {fact['correct_answer']}")
    else:
        print("Sorry, no quiz available for this topic yet.")

    print("\nThank you for using the Knowledge Booster!")

if __name__ == "__main__":
    run_knowledge_booster()
