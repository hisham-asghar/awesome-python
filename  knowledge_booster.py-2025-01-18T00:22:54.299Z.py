
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic in ["Science", "Technology", "History"]:
        api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
        headers = {"X-Api-Key": api_key}
        response = requests.get(topics[topic], headers=headers)
        data = response.json()
        return data[0]["fact"]
    elif topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][random.randint(0, 9)]["question"]

# Function to run the interactive quiz
def run_quiz(topic):
    if topic in ["Science", "Technology", "History"]:
        api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
        headers = {"X-Api-Key": api_key}
        response = requests.get(topics[topic], headers=headers)
        data = response.json()
        question = data[random.randint(0, 9)]["question"]
        answers = data[random.randint(0, 9)]["choices"]
        correct_answer = data[random.randint(0, 9)]["answer"]
    elif topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][random.randint(0, 9)]["question"]
        answers = data["results"][random.randint(0, 9)]["incorrect_answers"]
        answers.append(data["results"][random.randint(0, 9)]["correct_answer"])
        random.shuffle(answers)
        correct_answer = data["results"][random.randint(0, 9)]["correct_answer"]

    print(f"Question: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main program loop
while True:
    print("Welcome to the Knowledge Booster!")
    print("Select a topic:")
    for topic in topics.keys():
        print(f"- {topic}")
    print("- Quit")

    user_input = input("Enter your choice: ")
    if user_input.lower() == "quit":
        break
    elif user_input in topics:
        print(f"Here's a random fact about {user_input}:")
        print(get_random_fact(user_input))
        print("\nNow let's test your knowledge!")
        run_quiz(user_input)
    else:
        print("Invalid choice. Please try again.")
