
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
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][0]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return random.choice(data)

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to display the fact or concept and the interactive quiz
def display_content(topic, data):
    print(f"\nTopic: {topic}")
    print(f"Fact/Concept: {data['fact']}")
    
    # Display the interactive quiz
    print("\nTime to test your knowledge!")
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]
    
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == correct_answer:
        print("Correct! You're a knowledge champion.")
    else:
        print(f"Oops, the correct answer is: {correct_answer}")

# Main function to run the interactive knowledge booster
def main():
    topic = display_menu()
    data = get_random_fact(topic)
    display_content(topic, data)

if __name__ == "__main__":
    main()
