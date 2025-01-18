
import random
import requests
import json

# Define the topics and their corresponding API endpoints or predefined data
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API or predefined data.
    """
    if topic in topics:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        return random.choice(data)
    else:
        return "Sorry, that topic is not available."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    if topic in topics:
        response = requests.get(topics[topic] + "/quiz")
        data = json.loads(response.text)
        
        # Display the quiz question and options
        print(data["question"])
        for i, option in enumerate(data["options"]):
            print(f"{i+1}. {option}")
        
        # Get the user's answer
        user_answer = int(input("Enter your answer (1-4): "))
        
        # Check if the user's answer is correct
        if user_answer == data["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {data['answer']}.")
    else:
        print("Sorry, that topic is not available.")

def main():
    """
    Main function that displays the menu and handles user interactions.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Get the user's topic selection
    topic_choice = int(input("Enter the number of the topic (1-4): "))
    
    # Get a random fact or concept for the selected topic
    fact = get_random_fact(list(topics.keys())[topic_choice - 1])
    print(f"\nFact: {fact}")
    
    # Run the quiz for the selected topic
    quiz(list(topics.keys())[topic_choice - 1])

if __name__ == "__main__":
    main()
