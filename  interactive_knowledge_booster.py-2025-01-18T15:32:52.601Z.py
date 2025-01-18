
import random
import requests
import json

def get_topic_menu():
    """
    Displays the topic menu and returns the user's selected topic.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    while True:
        try:
            topic = int(input("Enter your choice (1-4): "))
            if 1 <= topic <= 4:
                return topic
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or predefined database.
    """
    facts = {
        1: "The largest known prime number as of 2022 has 23,249,425 digits.",
        2: "The first programmable computer was the ENIAC, which was completed in 1946.",
        3: "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
        4: "The first product to have a barcode was Wrigley's gum."
    }
    
    return facts.get(topic, "Sorry, no fact available for this topic at the moment.")

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the selected topic.
    """
    questions = {
        1: {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Cu", "Hg"],
            "answer": 0
        },
        2: {
            "question": "Which company developed the first commercially successful smartphone?",
            "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
            "answer": 2
        },
        3: {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
            "answer": 2
        },
        4: {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3
        }
    }
    
    question = questions.get(topic, None)
    if question:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    return user_answer == question["answer"] + 1
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        return None

def main():
    topic = get_topic_menu()
    print(get_random_fact(topic))
    
    quiz_result = quiz_question(topic)
    if quiz_result is not None:
        if quiz_result:
            print("Correct! You've increased your knowledge.")
        else:
            print("Incorrect. Better luck next time!")
    else:
        print("Sorry, no quiz available for this topic at the moment.")

if __name__ == "__main__":
    main()
