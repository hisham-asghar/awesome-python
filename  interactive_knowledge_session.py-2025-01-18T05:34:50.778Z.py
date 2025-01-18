
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

# API key for API-Ninjas (replace with your own)
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

def run_quiz(topic):
    """
    Runs a multiple-choice quiz for the specified topic.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question['answer']
    answers = [correct_answer] + question['incorrect_answers']
    random.shuffle(answers)
    
    # Display the question and answers
    print(f"Question: {question['question']}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    
    # Display the menu of topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic choice
    choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[choice-1]
    
    # Fetch a random fact and run the quiz
    print(f"\nHere's a random fact about {topic}: {get_random_fact(topic)}")
    print(f"\nNow, let's test your {topic} knowledge with a quiz!")
    run_quiz(topic)
    
    print("\nThank you for participating in the Interactive Knowledge Session!")

if __name__ == "__main__":
    main()
