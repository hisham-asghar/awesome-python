
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return random.choice(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    if topic == "General Knowledge":
        url = topics[topic]
        api_key = "YOUR_API_KEY_HERE"
        headers = {'X-Api-Key': api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            question = random.choice(data)
            print(question["question"])
            choices = question["options"]
            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice}")

            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question["answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {choices[question['answer']-1]}.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
    else:
        fact = get_random_fact(topic)
        if fact:
            print(f"Did you know? {fact['fact']}")
            print(f"Source: {fact['source']}")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    user_input = int(input("Enter the number of the topic (1-4): "))

    if 1 <= user_input <= len(topics):
        selected_topic = list(topics.keys())[user_input - 1]
        print(f"You selected: {selected_topic}")
        quiz(selected_topic)
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
