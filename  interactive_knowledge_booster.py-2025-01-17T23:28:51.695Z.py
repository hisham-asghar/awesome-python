
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

# API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Select a random question and answers from the API response
    question = random.choice(data)["question"]
    answers = [random.choice(data)["answer"] for _ in range(3)]
    correct_answer = random.choice(data)["answer"]
    answers.append(correct_answer)
    random.shuffle(answers)
    
    print(f"Question: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Main function that displays the menu and handles user interaction.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    choice = int(input("Enter the number of your choice: "))
    topic = list(topics.keys())[choice-1]
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_random_fact(topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
