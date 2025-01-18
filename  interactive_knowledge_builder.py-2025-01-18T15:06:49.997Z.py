
import random
import requests
import json

def get_topic_info(topic):
    """
    Fetches information about the selected topic from a predefined database or public API.
    """
    topics = {
        "science": "https://api.example.com/science",
        "technology": "https://api.example.com/technology",
        "history": "https://api.example.com/history",
        "general_knowledge": "https://api.example.com/general_knowledge"
    }
    
    if topic in topics:
        response = requests.get(topics[topic])
        if response.status_code == 200:
            return response.json()
        else:
            return None
    else:
        return None

def display_fact(topic_info):
    """
    Displays a random fact or concept from the selected topic.
    """
    fact = random.choice(topic_info["facts"])
    print(f"Did you know? {fact}")

def quiz_question(topic_info):
    """
    Displays a multiple-choice quiz question from the selected topic.
    """
    question = random.choice(topic_info["quiz_questions"])
    print(question["question"])
    
    options = question["options"]
    random.shuffle(options)
    
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer-1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}")

def main():
    """
    Displays a menu for users to select a topic and interactively learn about it.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general_knowledge"]
    topic = topics[topic_choice - 1]
    
    topic_info = get_topic_info(topic)
    if topic_info:
        display_fact(topic_info)
        quiz_question(topic_info)
    else:
        print("Sorry, we couldn't fetch information for the selected topic.")

if __name__ == "__main__":
    main()
