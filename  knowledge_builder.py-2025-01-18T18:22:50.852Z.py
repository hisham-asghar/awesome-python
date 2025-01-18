
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_fact(topic):
    """
    Fetch a random fact or concept from the selected topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provide an interactive quiz for the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    answers = [correct_answer] + question["incorrect_answers"]
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
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Main function to run the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    chosen_topic = input("Enter your choice: ")
    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic}:")
        print(get_fact(chosen_topic))
        print("\nNow let's test your knowledge with a quiz!")
        quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
