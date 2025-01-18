
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

API_ENDPOINTS = {
    'Science': 'https://api.api-ninjas.com/v1/science',
    'Technology': 'https://api.api-ninjas.com/v1/technology',
    'History': 'https://api.api-ninjas.com/v1/history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/trivia'
}

API_KEY = 'your_api_key_here'

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = API_ENDPOINTS[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic.
    """
    url = API_ENDPOINTS[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)['question']
    answers = [question['answer']] + question['options']
    random.shuffle(answers)
    
    print(f"Question: {question['question']}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = input("Enter the number of the correct answer: ")
    if answers[int(user_answer) - 1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Displays the menu, allows the user to select a topic, and runs the corresponding functionality.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    
    topic_choice = input("Enter the number of the topic: ")
    
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f"\nYou selected: {topic}")
        
        print("\nHere's a random fact or concept about this topic:")
        print(get_random_fact(topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
