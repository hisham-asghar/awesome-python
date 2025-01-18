
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
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
        fact = random.choice(data)
        return fact["fact"]

# Function to run the interactive knowledge session
def run_knowledge_session():
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ").strip()

    if selected_topic in topics:
        print(f"\nYou selected: {selected_topic}")
        if selected_topic == "General Knowledge":
            fact, choices = get_random_fact(selected_topic)
            print(f"\nQuestion: {fact}")
            print("Multiple Choice:")
            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice}")
            user_answer = int(input("Enter your answer (1-4): "))
            if choices[user_answer-1] == choices[-1]:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", choices[-1])
        else:
            fact = get_random_fact(selected_topic)
            print(f"\nFact: {fact}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    run_knowledge_session()
