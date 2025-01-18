
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        return data["results"][random.randint(0, 9)]
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        return data[random.randint(0, len(data) - 1)]

# Function to display the menu and get the user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        user_input = input("Enter your choice: ").capitalize()
        if user_input in topics:
            return user_input
        else:
            print("Invalid input. Please try again.")

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    
    if topic == "General Knowledge":
        print(f"Question: {fact['question']}")
        
        # Shuffle the answer options
        options = fact["incorrect_answers"]
        options.append(fact["correct_answer"])
        random.shuffle(options)
        
        # Display the answer options
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        # Get the user's answer
        while True:
            user_answer = input("Enter your answer (1-4): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                break
            else:
                print("Invalid input. Please try again.")
        
        # Check the user's answer
        if options[int(user_answer) - 1] == fact["correct_answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {fact['correct_answer']}")
    else:
        print(f"Did you know? {fact}")

# Main function
def main():
    topic = display_menu()
    run_quiz(topic)

if __name__ == "__main__":
    main()
