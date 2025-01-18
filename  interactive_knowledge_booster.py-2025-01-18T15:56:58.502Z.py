
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

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    choice = int(input("Enter your choice (1-4): "))
    return choice

# Function to fetch a random fact or concept for the chosen topic
def get_random_fact(topic_id):
    # Fetch data from a public API or predefined database
    facts = {
        1: ["The human body has 206 bones.", "The largest planet in our solar system is Jupiter.", "Photosynthesis is the process by which plants convert sunlight into energy."],
        2: ["The first computer virus was created in 1983.", "The World Wide Web was invented by Tim Berners-Lee in 1989.", "Artificial Intelligence (AI) is the simulation of human intelligence in machines."],
        3: ["The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.", "The Roman Empire lasted for over 400 years.", "The Renaissance was a period of cultural, artistic, political, and economic 'rebirth' in Europe."],
        4: ["The largest organ in the human body is the skin.", "The Mona Lisa has no eyebrows.", "The tallest mammal is the giraffe."]
    }
    return random.choice(facts[topic_id])

# Function to display the random fact or concept
def display_fact(topic_id):
    fact = get_random_fact(topic_id)
    print(f"Here's a random fact or concept about {topics[topic_id]}:")
    print(fact)

# Function to run the interactive quiz
def run_quiz(topic_id):
    # Fetch quiz questions and answers from a public API or predefined database
    quiz_data = {
        1: [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Combustion", "Evaporation"],
                "answer": 1
            }
        ],
        2: [
            {
                "question": "Who is considered the 'father of the World Wide Web'?",
                "options": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Elon Musk"],
                "answer": 2
            },
            {
                "question": "What is the name of the first computer virus?",
                "options": ["Melissa", "I Love You", "Morris Worm", "Stuxnet"],
                "answer": 2
            }
        ],
        3: [
            {
                "question": "What is the name of the largest ancient civilization in the Americas?",
                "options": ["Aztec", "Inca", "Maya", "Olmec"],
                "answer": 2
            },
            {
                "question": "In what year did the Roman Empire fall?",
                "options": ["476 AD", "1453 AD", "1789 AD", "1917 AD"],
                "answer": 0
            }
        ],
        4: [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Lungs", "Skin"],
                "answer": 3
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Rhinoceros", "Hippopotamus", "Giraffe"],
                "answer": 3
            }
        ]
    }

    score = 0
    for question in quiz_data[topic_id]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_data[topic_id])}")

# Main program loop
while True:
    topic_choice = display_menu()
    display_fact(topic_choice)
    run_quiz(topic_choice)
    print("Thanks for using the Interactive Knowledge Booster!")
    break
