
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").title()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url)
    data = json.loads(response.text)
    return random.choice(data)

# Function to display the fact or concept and an interactive quiz
def interactive_quiz(topic, fact):
    print(f"\nToday's {topic} fact: {fact['title']}")
    print(fact['description'])
    
    # Generate a multiple-choice quiz
    options = fact['options']
    correct_answer = fact['correct_answer']
    random.shuffle(options)
    
    print("\nTest your knowledge with a quiz:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input(f"Enter the number of the correct answer (1-{len(options)}): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            if options[int(user_answer)-1] == correct_answer:
                print("Correct! You're a knowledge master.")
                break
            else:
                print("Oops, that's not the right answer. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and", len(options))

# Main function to run the script
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    interactive_quiz(topic, fact)

if __name__ == "__main__":
    main()
