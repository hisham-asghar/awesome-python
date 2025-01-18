
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to get a random fact from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    # Define the quiz questions and answers for the selected topic
    quiz_data = {
        "Science": [
            {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Cu", "Fe"], "correct": 0},
            {"question": "What is the largest planet in our solar system?", "answers": ["Mars", "Jupiter", "Saturn", "Uranus"], "correct": 1},
            {"question": "What is the process by which plants convert sunlight into energy?", "answers": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"], "correct": 0}
        ],
        "Technology": [
            {"question": "What is the name of the first programmable computer?", "answers": ["ENIAC", "UNIVAC", "Apple I", "IBM PC"], "correct": 0},
            {"question": "What is the name of the software that translates high-level programming languages into machine code?", "answers": ["Compiler", "Interpreter", "Assembler", "Linker"], "correct": 0},
            {"question": "What is the name of the network protocol used for web browsing?", "answers": ["HTTP", "FTP", "SMTP", "DHCP"], "correct": 0}
        ],
        "History": [
            {"question": "What year was the Declaration of Independence signed?", "answers": ["1776", "1789", "1812", "1865"], "correct": 0},
            {"question": "Who was the first president of the United States?", "answers": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "Franklin D. Roosevelt"], "correct": 0},
            {"question": "What event marked the end of World War II?", "answers": ["D-Day", "Pearl Harbor", "Atomic bombings of Hiroshima and Nagasaki", "VE Day"], "correct": 2}
        ],
        "General Knowledge": [
            {"question": "What is the capital city of Australia?", "answers": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "correct": 3},
            {"question": "What is the largest ocean on Earth?", "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "correct": 3},
            {"question": "What is the tallest mammal on Earth?", "answers": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"], "correct": 1}
        ]
    }

    # Run the quiz
    score = 0
    for question in quiz_data[topic]:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["correct"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_data[topic])}")

# Main program loop
while True:
    topic = display_menu()
    if topic in topics:
        print(f"\nHere's a random fact about {topic}:")
        print(get_random_fact(topic))
        print("\nNow let's test your knowledge!")
        run_quiz(topic)
        break
    else:
        print("Invalid topic. Please try again.")
