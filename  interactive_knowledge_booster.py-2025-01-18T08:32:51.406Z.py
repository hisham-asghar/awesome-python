
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.data.gov/trivia/science",
    "Technology": "https://api.data.gov/trivia/technology",
    "History": "https://api.data.gov/trivia/history",
    "General Knowledge": "https://api.data.gov/trivia/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    return data["fact"]

def quiz(topic):
    """
    Provides an interactive quiz for the user to test their knowledge on the specified topic.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    # Select a random question and answers from the API response
    question = data["question"]
    answers = data["answers"]
    correct_answer = data["correct_answer"]
    
    # Shuffle the answers
    random.shuffle(answers)
    
    # Display the question and answers
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    
    # Check if the user's answer is correct
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    The main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic choice
    choice = int(input("Enter the number of the topic: "))
    
    # Get a random fact or concept from the chosen topic
    topic = list(topics.keys())[choice-1]
    fact = get_random_fact(topic)
    print(f"\nHere's a random {topic.lower()} fact: {fact}")
    
    # Start the quiz for the chosen topic
    print("\nNow let's test your knowledge!")
    quiz(topic)

if __name__ == "__main__":
    main()
