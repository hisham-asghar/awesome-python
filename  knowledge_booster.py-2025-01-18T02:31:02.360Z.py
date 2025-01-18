
import random
import requests
import json

# Dictionary to store topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been on Earth for over 400 million years, predating the dinosaurs."
        ],
        "quizzes": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To generate energy", "To control breathing"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was invented in 1975 by Steven Sasson, an engineer at Kodak."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful web browser?",
                "options": ["Microsoft", "Apple", "Netscape", "Google"],
                "answer": 2
            },
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "Turing Machine", "Analytical Engine", "Z1"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC, making them over 4,500 years old.",
            "The Roman Empire lasted for over 1,000 years, from the 8th century BC to the 5th century AD."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematical and astronomical knowledge?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 2
            },
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Rock", "Roanoke Colony", "New Amsterdam"],
                "answer": 0
            },
            {
                "question": "Which event is considered the starting point of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Attack on Pearl Harbor", "Fall of the Berlin Wall", "Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The highest mountain in the world is Mount Everest, standing at 8,849 meters (29,032 feet) above sea level."
        ],
        "quizzes": [
            {
                "question": "Which of these is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which continent is the largest by land area?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz(topic):
    """
    Retrieves a random quiz from the selected topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's answer.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    return user_answer

def main():
    """
    Displays the topic menu, retrieves a fact or quiz, and runs the quiz.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(chosen_topic)
        user_answer = run_quiz(quiz)
        if user_answer == quiz["answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
