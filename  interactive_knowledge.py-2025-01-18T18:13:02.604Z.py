
import random
import json
import requests

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": 0
            },
            {
                "question": "Which is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Lungs"],
                "answer": 2
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The internet was originally called ARPANET, and it was created by the US Department of Defense.",
            "The QR code was invented in 1994 by the Japanese company Denso Wave."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Chrome"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.",
            "The Pyramids of Giza were built as tombs for the Egyptian pharaohs Khufu, Khafre, and Menkaure."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Greece", "Rome", "China"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers in 1903?",
                "options": ["The Flyer", "The Wright Flyer", "The Kitty Hawk", "The Biplane"],
                "answer": 1
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23,249,425 digits.",
            "The largest known prime number as of 2023 has 23,249,425 digits.",
            "The largest known prime number as of 2023 has 23,249,425 digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the given topic.
    """
    question = random.choice(topics[topic]["quiz_questions"])
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question["answer"] + 1:
                print("Correct!")
                break
            else:
                print("Incorrect. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")

def main():
    """
    Main function that runs the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your topic choice: ").lower()
        if user_topic in topics:
            print(f"\nHere's a random fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            print("\nNow let's test your knowledge with a quiz!")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
