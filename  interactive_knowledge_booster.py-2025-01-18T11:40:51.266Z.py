
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

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the selected topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provide a multiple-choice quiz for the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and its options
    question = random.choice(data)
    options = [question["answer"]] + question["options"]
    random.shuffle(options)
    
    print(f"Question: {question['question']}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function to display the menu and handle user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic selection
    topic_choice = int(input("Enter the number of your chosen topic: "))
    selected_topic = list(topics.keys())[topic_choice - 1]
    
    # Display a random fact or concept from the selected topic
    print(f"\nHere's a random fact about {selected_topic}:")
    print(get_random_fact(selected_topic))
    
    # Provide a quiz for the selected topic
    print(f"\nNow, let's test your knowledge with a {selected_topic} quiz!")
    quiz(selected_topic)

if __name__ == "__main__":
    main()
