
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    headers = {"X-Api-Key": api_key}

    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        fact = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return fact, choices
    else:
        response = requests.get(topics[topic], headers=headers)
        data = response.json()
        fact = data[0]["fact"]
        return fact

# Function to run the interactive quiz
def run_quiz(topic):
    fact, choices = get_random_fact(topic)
    print(f"Topic: {topic}")
    print(f"Fact or Concept: {fact}")
    print("Multiple-Choice Options:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if topic == "General Knowledge":
        if choices[user_answer - 1] == data["results"][0]["correct_answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {data['results'][0]['correct_answer']}")
    else:
        if user_answer == 1:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 1.")

# Main function to display the menu and run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")

    user_choice = int(input("Enter the number of the topic: "))
    selected_topic = list(topics.keys())[user_choice - 1]

    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
