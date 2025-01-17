
import random
import requests
import json

# Define topics and their corresponding APIs or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "general_knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][0]["question"]
        options = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(options)
        return fact, options
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        fact = data[0]["fact"]
        return fact, None

# Function to run the interactive quiz
def run_quiz(topic):
    fact, options = get_random_fact(topic)
    print(f"Topic: {topic.capitalize()}")
    print(f"Fact: {fact}")
    
    if options:
        print("Multiple-choice options:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        user_answer = int(input("Enter the number of the correct answer: "))
        if options[user_answer - 1] == data["results"][0]["correct_answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", data["results"][0]["correct_answer"])
    else:
        input("Press Enter to continue...")

# Main program loop
while True:
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")
