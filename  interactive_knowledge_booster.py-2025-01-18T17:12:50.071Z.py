
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    url = topics[topic]
    response = requests.get(url)
    data = json.loads(response.text)
    return random.choice(data)

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    quiz_data = json.loads(response.text)
    
    score = 0
    for question in quiz_data:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", question["answer"])
    
    print(f"Your final score is {score} out of {len(quiz_data)}")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[choice-1]
    
    print(f"You selected: {selected_topic}")
    print(get_random_fact(selected_topic))
    
    quiz_choice = input("Would you like to take a quiz on this topic? (y/n) ")
    if quiz_choice.lower() == "y":
        quiz(selected_topic)
    else:
        print("Okay, no quiz for now. Have a great day!")

if __name__ == "__main__":
    main()
