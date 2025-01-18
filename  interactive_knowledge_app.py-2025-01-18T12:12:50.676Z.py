
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or trivia
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    headers = {"X-Api-Key": api_key}
    response = requests.get(topics[topic], headers=headers)
    
    if topic == "General Knowledge":
        data = response.json()
        return data["question"], data["options"], data["answer"]
    else:
        data = response.json()
        return data["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"Welcome to the {topic} quiz!")
    
    # Fetch a random question and options
    question, options, answer = get_random_fact(topic)
    print(question)
    
    # Display the multiple-choice options
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check if the user's answer is correct
    if options[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {answer}")

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        # Display the menu of topics
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        print("- Exit")
        
        # Get the user's topic choice
        choice = input("Enter your choice: ")
        
        if choice == "Exit":
            print("Goodbye!")
            break
        elif choice in topics:
            # Fetch a random fact or trivia and display it
            fact = get_random_fact(choice)
            print(f"\nRandom {choice} fact: {fact}")
            
            # Run the interactive quiz
            run_quiz(choice)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
