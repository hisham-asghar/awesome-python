
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which type of electromagnetic radiation has the highest frequency?",
                "options": ["Infrared", "Ultraviolet", "Gamma Rays", "X-Rays"],
                "answer": 2
            },
            {
                "question": "What is the name of the force that holds the planets in orbit around the Sun?",
                "options": ["Gravitational force", "Electromagnetic force", "Nuclear force", "Centrifugal force"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet of floor space.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense in the 1960s."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process by which data is transmitted between computers?",
                "options": ["Networking", "Programming", "Encryption", "Rendering"],
                "answer": 0
            },
            {
                "question": "Which technology is used to wirelessly charge electronic devices?",
                "options": ["Bluetooth", "Wi-Fi", "Infrared", "Induction"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language that is commonly used for web development?",
                "options": ["Java", "Python", "C++", "JavaScript"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Gutenberg Bible was the first major book printed in the West using movable metal type."
        ],
        "quiz_questions": [
            {
                "question": "In what year was the United States Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Airplane", "The Wright Flyer"],
                "answer": 3
            },
            {
                "question": "What was the name of the ancient civilization that built the Colosseum in Rome?",
                "options": ["Greeks", "Egyptians", "Romans", "Mayans"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", "Indian Ocean"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Venus"],
                "answer": 1
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yuan", "Euro", "Yen", "Dollar"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if int(user_answer) - 1 == question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    """
    Main function that runs the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your choice: ").lower()
        if user_topic in topics:
            print(f"\nRandom fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            print("\nNow let's test your knowledge with a quiz!")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
