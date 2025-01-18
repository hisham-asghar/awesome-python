
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

# API key for API-Ninjas (you'll need to replace this with your own)
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)[0]
    return data["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    answers = [correct_answer] + question["incorrect_answers"]
    random.shuffle(answers)
    
    # Display the question and answers
    print(question["question"])
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic selection
    choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[choice-1]
    
    # Display a random fact or concept for the selected topic
    print(f"\nHere's a random fact or concept about {topic}:")
    print(get_random_fact(topic))
    
    # Run the quiz for the selected topic
    print(f"\nNow let's test your knowledge with a {topic} quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
