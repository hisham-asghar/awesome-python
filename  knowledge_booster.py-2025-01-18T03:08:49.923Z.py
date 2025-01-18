
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
        fact = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return fact, choices
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = random.choice(data)["fact"]
        return fact, None

# Function to run the interactive knowledge booster
def run_knowledge_booster():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    fact, choices = get_random_fact(selected_topic)
    print(f"\nHere's a {selected_topic.lower()} fact for you:")
    print(fact)

    if choices:
        print("\nMultiple-choice quiz:")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if choices[user_answer-1] == data["results"][0]["correct_answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    run_knowledge_booster()
