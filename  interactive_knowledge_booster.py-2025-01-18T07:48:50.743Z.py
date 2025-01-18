
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

# Function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and options
    question = random.choice(data)
    options = [question["fact"]] + random.sample(data, 3)
    random.shuffle(options)
    
    # Display the question and options
    print(f"Question: {question['fact']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check if the user's answer is correct
    if options[user_answer-1] == question["fact"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {options.index(question['fact'])+1}.")

# Main function to display the menu and handle user interactions
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic}")
        print("5. Quit")
        
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Goodbye!")
            break
        elif 1 <= choice <= 4:
            topic = list(topics)[choice-1]
            print(f"\nRandom {topic} fact: {get_random_fact(topic)}")
            quiz(topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
