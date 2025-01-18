
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

# Function to display the multiple-choice quiz
def quiz(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic] + "?type=multiple_choice"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    answers = [correct_answer] + question["incorrect_answers"]
    random.shuffle(answers)
    
    # Display the question and answers
    print(question["question"])
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    # Get user's answer and check if it's correct
    user_answer = int(input("Enter your answer (1-4): "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to display the menu and handle user interaction
def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get user's topic choice
    choice = int(input("Enter your choice (1-4): "))
    topic = list(topics.keys())[choice-1]
    
    # Display a random fact or concept from the chosen topic
    print(f"\nHere's a random {topic.lower()} fact or concept:")
    print(get_random_fact(topic))
    
    # Run the quiz for the chosen topic
    print(f"\nNow, let's test your {topic.lower()} knowledge!")
    quiz(topic)

if __name__ == "__main__":
    main()
