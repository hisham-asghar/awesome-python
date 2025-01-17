
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the chosen topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    wrong_answers = [random.choice(data)["answer"] for _ in range(3)]
    all_answers = [correct_answer] + wrong_answers
    random.shuffle(all_answers)
    
    # Display the question and answers
    print(question["question"])
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    
    # Display the menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic.replace('_', ' ').title()}")
    
    # Get the user's choice
    choice = int(input("Enter the number of the topic: "))
    topic = list(topics.keys())[choice-1]
    
    # Display a random fact or concept
    print(f"\nHere's a random fact about {topic.replace('_', ' ')}:")
    print(get_random_fact(topic))
    
    # Run the quiz
    print(f"\nNow, let's test your {topic.replace('_', ' ')} knowledge with a quiz!")
    quiz(topic)
    
    print("\nThank you for participating in the Interactive Knowledge Session!")

if __name__ == "__main__":
    main()
