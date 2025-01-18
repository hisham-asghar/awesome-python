
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

topic_apis = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&category=9"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topic_apis[topic]
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key

    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][0]["question"]
    else:
        headers = {"X-Api-Key": api_key}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        fact = data[0]["fact"]

    return fact

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    topic_choice = int(input("Enter the number of your chosen topic: "))
    return topics[topic_choice]

# Function to run the interactive quiz
def run_quiz(topic):
    if topic == "General Knowledge":
        response = requests.get(topic_apis[topic])
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        all_answers = [correct_answer] + incorrect_answers
        random.shuffle(all_answers)

        print(f"Question: {question}")
        for i, answer in enumerate(all_answers):
            print(f"{i+1}. {answer}")

        user_answer = int(input("Enter the number of the correct answer: "))
        if all_answers[user_answer - 1] == correct_answer:
            print("Correct! You've gained some knowledge.")
        else:
            print(f"Oops, the correct answer is {correct_answer}.")
    else:
        fact = get_random_fact(topic)
        print(f"Did you know? {fact}")

# Main program loop
while True:
    selected_topic = display_menu()
    run_quiz(selected_topic)
    print()
    continue_choice = input("Do you want to learn about another topic? (y/n) ")
    if continue_choice.lower() != "y":
        break

print("Thank you for using the Interactive Knowledge Booster!")
