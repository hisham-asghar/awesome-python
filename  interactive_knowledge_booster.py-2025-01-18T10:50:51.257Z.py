
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to display the menu and get the user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").capitalize()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][0]["question"]
    else:
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = data[0]["fact"]
    
    return fact

# Function to run the interactive quiz
def run_quiz(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        
        # Combine the correct and incorrect answers
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)
        
        # Display the question and answers
        print(question)
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        # Get the user's answer
        while True:
            user_answer = input("Enter the number of your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                if answers[int(user_answer)-1] == correct_answer:
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
                break
            else:
                print("Invalid input. Please try again.")
    else:
        print("Sorry, interactive quizzes are not available for this topic yet.")

# Main function
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    print(f"\nDid you know? {fact}")
    
    print("\nLet's test your knowledge!")
    run_quiz(topic)

if __name__ == "__main__":
    main()
