
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
    """
    url = topics[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    answers = [question['answer']] + question['incorrect_answers']
    random.shuffle(answers)
    
    print(f"Question: {question['question']}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that displays the menu and handles user interaction.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    user_choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[user_choice-1]
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_fact(topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
