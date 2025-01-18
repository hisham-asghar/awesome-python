
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][0]["question"]
        return fact
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        fact = data[0]["fact"]
        return fact

# Function to display the interactive quiz
def quiz(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        
        # Shuffle the answers
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)
        
        print(question)
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        user_answer = int(input("Enter the number of the correct answer: "))
        if answers[user_answer-1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        fact = data[0]["fact"]
        print(fact)
        
        # Add a quiz for the selected topic (e.g., science, technology, history)
        # Implement the quiz logic based on the specific topic

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        random_fact = get_random_fact(selected_topic)
        print(f"Here's a random {selected_topic.lower()} fact or concept: {random_fact}")
        
        quiz_choice = input("Would you like to take a quiz on this topic? (y/n) ")
        if quiz_choice.lower() == "y":
            quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")
