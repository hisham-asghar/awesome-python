
import random
import requests
import json

# List of topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, with an average surface temperature of 462°C (864°F).",
            "The largest known prime number as of 2022 has 23,249,425 digits."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which of these is not a fundamental force in physics?",
                "options": ["Gravity", "Electromagnetism", "Strong nuclear force", "Weak nuclear force", "Centrifugal force"],
                "answer": 4
            },
            {
                "question": "What is the name of the first artificial satellite launched into Earth's orbit?",
                "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Telstar 1"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first text message was sent on December 3, 1992, and read "Merry Christmas".",
            "The first digital camera, the Mavica, was developed by Sony in 1981 and could store up to 50 images on a floppy disk."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser, developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1775", "1812"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Aztec", "Ancient Egypt"],
                "answer": 3
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Vasco da Gama Expedition", "The Lewis and Clark Expedition"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2022 has 23,249,425 digits.",
            "The first person to circumnavigate the globe was Ferdinand Magellan, although he was killed in the Philippines and did not complete the voyage himself."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Green", "Yellow", "Purple"],
                "answer": 4
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the given topic.
    """
    quiz = topics[topic]["quiz"]
    question = random.choice(quiz)
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
            if user_answer < 1 or user_answer > len(question["options"]):
                print("Invalid answer. Please try again.")
                continue
            if user_answer - 1 == question["answer"]:
                print("Correct!")
            else:
                print("Incorrect. Better luck next time.")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter a topic or 'quit' to exit: ").lower()
        if user_topic == "quit":
            print("Goodbye!")
            break
        if user_topic in topics:
            print(get_random_fact(user_topic))
            run_quiz(user_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
