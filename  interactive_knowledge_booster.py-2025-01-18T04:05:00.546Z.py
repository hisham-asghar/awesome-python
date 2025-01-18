
import random
import requests
import json

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    print("5. Exit")
    return int(input("Enter your choice (1-5): "))

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the Solar System is Venus, not Mercury.",
            "Bees can fly higher than the tallest mountains on Earth."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
            "The internet was originally called ARPANET, and it was created in 1969."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first book printed in English was the Recuyell of the Historyes of Troye, printed in 1473."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ]
    }
    return random.choice(facts[topic])

# Function to display a quiz with multiple-choice questions
def quiz(topic):
    questions = {
        "science": [
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
            {"question": "Which planet in our solar system is known as the 'Red Planet'?", "options": ["Mars", "Jupiter", "Saturn", "Venus"], "answer": 0},
            {"question": "What is the process by which plants convert sunlight into energy?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"], "answer": 0}
        ],
        "technology": [
            {"question": "What is the name of the first commercially successful web browser?", "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome"], "answer": 0},
            {"question": "Which company is credited with creating the first personal computer?", "options": ["Apple", "IBM", "Microsoft", "Commodore"], "answer": 1},
            {"question": "What is the name of the programming language used to create the World Wide Web?", "options": ["HTML", "JavaScript", "Python", "C++"], "answer": 0}
        ],
        "history": [
            {"question": "Which ancient civilization is known for building the pyramids?", "options": ["Mesopotamia", "Indus Valley", "Egypt", "China"], "answer": 2},
            {"question": "Who was the first president of the United States?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"], "answer": 1},
            {"question": "Which event marked the end of World War II?", "options": ["D-Day", "Pearl Harbor", "Hiroshima and Nagasaki bombings", "VE Day"], "answer": 2}
        ],
        "general": [
            {"question": "What is the largest continent in the world?", "options": ["Africa", "Asia", "North America", "South America"], "answer": 1},
            {"question": "Which animal is known as the 'King of the Jungle'?", "options": ["Lion", "Elephant", "Giraffe", "Zebra"], "answer": 0},
            {"question": "What is the name of the largest ocean on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 0}
        ]
    }
    
    # Select a random question from the chosen topic
    question = random.choice(questions[topic])
    
    # Display the question and options
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check if the answer is correct
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

# Main program loop
while True:
    choice = display_menu()
    if choice == 1:
        print("Random Science Fact:", get_random_fact("science"))
        quiz("science")
    elif choice == 2:
        print("Random Technology Fact:", get_random_fact("technology"))
        quiz("technology")
    elif choice == 3:
        print("Random History Fact:", get_random_fact("history"))
        quiz("history")
    elif choice == 4:
        print("Random General Knowledge Fact:", get_random_fact("general"))
        quiz("general")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
