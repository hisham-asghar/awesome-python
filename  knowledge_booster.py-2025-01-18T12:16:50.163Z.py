
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

# Function to fetch random fact or concept from the chosen topic
def get_random_fact(topic):
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        fact = random.choice(data["facts"])
        return fact
    except:
        return "Sorry, we couldn't fetch a fact for this topic at the moment."

# Function to display the multiple-choice quiz
def quiz(topic):
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        quiz_data = random.choice(data["quizzes"])
        question = quiz_data["question"]
        options = quiz_data["options"]
        answer = quiz_data["answer"]

        print(f"Question: {question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    except:
        print("Sorry, we couldn't load the quiz for this topic at the moment.")

# Main function to display the menu and handle user interaction
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    user_choice = int(input("Enter your choice (1-4): "))
    chosen_topic = list(topics.keys())[user_choice-1]

    print(f"\nYou've chosen: {chosen_topic}")
    print(get_random_fact(chosen_topic))

    quiz_choice = input("\nWould you like to take a quiz? (y/n) ")
    if quiz_choice.lower() == "y":
        quiz(chosen_topic)

if __name__ == "__main__":
    main()
