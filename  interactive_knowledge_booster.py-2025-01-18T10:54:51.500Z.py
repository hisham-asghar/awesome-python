
import random
import requests
import json

def get_topic_info(topic):
    """
    Fetches information about a given topic from a predefined database or public API.
    """
    topics = {
        "science": "https://api.example.com/science",
        "technology": "https://api.example.com/technology",
        "history": "https://api.example.com/history",
        "general_knowledge": "https://api.example.com/general_knowledge"
    }
    
    if topic in topics:
        response = requests.get(topics[topic])
        return response.json()
    else:
        return None

def display_topic_info(topic_info):
    """
    Displays a random fact or concept from the provided topic information.
    """
    if topic_info:
        fact = random.choice(topic_info["facts"])
        print(f"Did you know? {fact}")
    else:
        print("Sorry, that topic is not available.")

def quiz_topic(topic_info):
    """
    Presents a multiple-choice quiz for the user to test their knowledge on the given topic.
    """
    if topic_info:
        question = random.choice(topic_info["quiz_questions"])
        print(question["question"])
        
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["correct_answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Sorry, that topic is not available.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    if topic_choice == 1:
        topic_info = get_topic_info("science")
        display_topic_info(topic_info)
        quiz_topic(topic_info)
    elif topic_choice == 2:
        topic_info = get_topic_info("technology")
        display_topic_info(topic_info)
        quiz_topic(topic_info)
    elif topic_choice == 3:
        topic_info = get_topic_info("history")
        display_topic_info(topic_info)
        quiz_topic(topic_info)
    elif topic_choice == 4:
        topic_info = get_topic_info("general_knowledge")
        display_topic_info(topic_info)
        quiz_topic(topic_info)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
