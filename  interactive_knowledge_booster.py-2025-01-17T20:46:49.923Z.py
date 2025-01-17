
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from the corresponding API endpoint or database
    if topic in topics:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        # Select a random fact or concept from the data
        fact = random.choice(data)
        return fact
    else:
        return "Sorry, that topic is not available."

# Function to display the multiple-choice quiz
def quiz(topic):
    # Fetch quiz questions and answers from the corresponding API endpoint or database
    if topic in topics:
        response = requests.get(topics[topic] + "/quiz")
        data = json.loads(response.text)
        # Loop through the quiz questions and get user answers
        score = 0
        for question in data:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"Your score: {score}/{len(data)}")
    else:
        print("Sorry, that topic is not available.")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        print("- Exit")
        user_choice = input("Enter your choice: ")
        if user_choice.lower() == "exit":
            break
        elif user_choice in topics:
            print("\nHere's a random fact or concept:")
            print(get_random_fact(user_choice))
            print("\nNow, let's test your knowledge!")
            quiz(user_choice)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
