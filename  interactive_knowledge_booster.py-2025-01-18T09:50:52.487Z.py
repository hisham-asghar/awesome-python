
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]["fact"]
    else:
        return "Failed to fetch data. Please try again later."

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic.
    """
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        question = random.choice(data)["question"]
        answers = question["options"]
        correct_answer = question["answer"]
        
        print(f"Question: {question['question']}")
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        user_answer = int(input("Enter the number of the correct answer: "))
        if answers[user_answer-1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    else:
        print("Failed to fetch data. Please try again later.")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in TOPICS:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in TOPICS:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
