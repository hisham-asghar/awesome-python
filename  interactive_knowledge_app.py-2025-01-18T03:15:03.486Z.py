
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == '1':  # Science
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '2':  # Technology
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '3':  # History
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '4':  # General Knowledge
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    else:
        return "Invalid topic selection."

    if response.status_code == 200:
        facts = response.json()
        random_fact = random.choice(facts)
        return random_fact['fact']
    else:
        return "Error fetching facts."

# Function to display the topic menu and get user input
def display_topic_menu():
    print("Select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic_choice = input("Enter the number of the topic (1-4): ")
    return topic_choice

# Function to display a multiple-choice quiz for the selected topic
def quiz_topic(topic):
    if topic == '1':  # Science
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the name of the closest planet to the Sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": 2
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ]
    elif topic == '2':  # Technology
        questions = [
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "Apple II", "IBM PC", "Commodore 64"],
                "answer": 0
            },
            {
                "question": "What is the name of the operating system developed by Apple?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology used to transfer data wirelessly?",
                "options": ["Bluetooth", "Ethernet", "Wi-Fi", "Fiber Optic"],
                "answer": 2
            }
        ]
    elif topic == '3':  # History
        questions = [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Glider", "The Biplane", "The Monoplane"],
                "answer": 0
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Inca", "Ancient Egypt"],
                "answer": 3
            }
        ]
    elif topic == '4':  # General Knowledge
        questions = [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            }
        ]
    else:
        return "Invalid topic selection."

    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter the number of your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your score: {score}/{len(questions)}")

# Main program loop
while True:
    topic_choice = display_topic_menu()
    if topic_choice in topics:
        print(f"Random fact about {topics[topic_choice]}: {get_random_fact(topic_choice)}")
        quiz_topic(topic_choice)
    else:
        print("Invalid topic selection. Please try again.")
    continue_prompt = input("Do you want to continue? (y/n) ")
    if continue_prompt.lower() != 'y':
        break
