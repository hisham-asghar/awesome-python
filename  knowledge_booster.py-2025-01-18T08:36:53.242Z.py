
import random
import requests
import json

# Define the available topics
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    choice = int(input("Enter your choice (1-4): "))
    return choice

# Function to fetch a random fact or concept for the chosen topic
def get_random_fact(topic_id):
    facts = {
        1: "The human body has 206 bones.",
        2: "The first computer bug was a real moth found trapped in a Harvard Mark II computer.",
        3: "The Great Wall of China is the only man-made structure visible from space.",
        4: "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
    }
    return facts[topic_id]

# Function to display the quiz and get user's answers
def run_quiz(topic_id):
    questions = {
        1: {
            "question": "What is the most abundant element in the universe?",
            "options": ["Hydrogen", "Helium", "Oxygen", "Carbon"],
            "answer": 0
        },
        2: {
            "question": "Who is considered the father of the World Wide Web?",
            "options": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Linus Torvalds"],
            "answer": 2
        },
        3: {
            "question": "Which ancient civilization built the Pyramids of Giza?",
            "options": ["Mesopotamians", "Egyptians", "Greeks", "Romans"],
            "answer": 1
        },
        4: {
            "question": "What is the largest organ in the human body?",
            "options": ["Heart", "Liver", "Skin", "Brain"],
            "answer": 2
        }
    }

    # Randomly select a question from the topic
    question_id = random.choice(list(questions.keys()))
    question = questions[question_id]

    # Display the question and options
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): ")) - 1

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

# Main function to run the script
def main():
    choice = display_menu()
    topic_name = topics[choice]
    print(f"\nYour chosen topic is: {topic_name}")

    # Fetch a random fact or concept for the chosen topic
    random_fact = get_random_fact(choice)
    print(f"\nFact about {topic_name}: {random_fact}")

    # Run the quiz for the chosen topic
    print("\nTime for a quiz!")
    run_quiz(choice)

    print("\nThank you for using the Knowledge Booster!")

if __name__ == "__main__":
    main()
