
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        return question, correct_answer, incorrect_answers
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    question, correct_answer, incorrect_answers = get_random_fact(topic)
    print(f"Topic: {topic}")
    print(question)
    
    # Combine the correct and incorrect answers and shuffle them
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)
    
    # Display the multiple-choice options
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    
    # Check if the user's answer is correct
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a {selected_topic.lower()} fact for you:")
        print(fact)
        
        print("\nNow, let's test your knowledge!")
        run_quiz(selected_topic)
        
        continue_prompt = input("\nDo you want to try another topic? (y/n) ")
        if continue_prompt.lower() != "y":
            break
    else:
        print("Invalid topic. Please try again.")
