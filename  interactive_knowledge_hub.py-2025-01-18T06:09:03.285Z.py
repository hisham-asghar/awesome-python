
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the chosen topic."""
    facts = {
        "science": [
            "The largest known prime number as of 2022 has 23,249,425 digits.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Cats have better low-light vision than humans, due to a higher concentration of rods in their retinas."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964 and consisted of a wooden shell with two metal wheels.",
            "The first commercial email service was launched by CompuServe in 1979.",
            "The world's first programmable computer, the ENIAC, was completed in 1946 and occupied a 30-by-50-foot room."
        ],
        "history": [
            "The Great Wall of China is the world's longest manmade structure, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful kidney transplant was performed by Dr. Joseph Murray in 1954."
        ],
        "general": [
            "A group of flamingos is called a flamboyance.",
            "The first product to have a barcode was Wrigley's gum.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises."
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    """Fetch a multiple-choice quiz question and answers from the chosen topic."""
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "answers": ["Au", "Ag", "Cu", "Fe"],
                "correct_answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "answers": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "correct_answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "answers": ["Respiration", "Photosynthesis", "Transpiration", "Osmosis"],
                "correct_answer": 1
            }
        ],
        "technology": [
            {
                "question": "What does the abbreviation 'CPU' stand for?",
                "answers": ["Central Processing Unit", "Computer Power Unit", "Computational Processing Unit", "Computer Processing Unit"],
                "correct_answer": 0
            },
            {
                "question": "Which company developed the first commercially successful graphical user interface (GUI)?",
                "answers": ["Apple", "Microsoft", "Xerox", "IBM"],
                "correct_answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "answers": ["Java", "C++", "Python", "Ruby"],
                "correct_answer": 2
            }
        ],
        "history": [
            {
                "question": "In what year did the United States Declaration of Independence get signed?",
                "answers": ["1776", "1789", "1812", "1865"],
                "correct_answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "answers": ["Roman", "Greek", "Egyptian", "Mesopotamian"],
                "correct_answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "answers": ["Kitty Hawk", "Wright Flyer", "Spirit of St. Louis", "Concorde"],
                "correct_answer": 1
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "answers": ["Heart", "Liver", "Skin", "Brain"],
                "correct_answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "answers": ["China", "Japan", "South Korea", "India"],
                "correct_answer": 1
            },
            {
                "question": "What is the tallest mammal in the world?",
                "answers": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "correct_answer": 1
            }
        ]
    }
    return random.choice(quiz_data[topic])

def main():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = input("Enter the number of your choice: ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting the program.")
        return

    print(f"\nHere's a random fact about {topic.capitalize()}:")
    print(get_random_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])

    for i, answer in enumerate(quiz_question["answers"]):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter the number of your answer: "))
    if user_answer - 1 == quiz_question["correct_answer"]:
        print("Correct! You're a knowledge champion.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

    print("\nThank you for using the Interactive Knowledge Hub. Goodbye!")

if __name__ == "__main__":
    main()
