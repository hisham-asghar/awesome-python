
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the chosen topic."""
    facts = {
        "science": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "A single teaspoon of neutron star material would weigh over 1 billion tons on Earth.",
            "The human body contains enough DNA to stretch from the Sun to Pluto and back again. 17 times."
        ],
        "technology": [
            "The first computer 'bug' was a dead moth found stuck in a Harvard Mark II computer in 1947.",
            "The first commercial computer, the UNIVAC I, was delivered to the US Census Bureau in 1951.",
            "The world's first text message was sent on December 3, 1992, and said 'Merry Christmas'."
        ],
        "history": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "The king of hearts is the only king without a mustache on a standard playing card."
        ],
        "general": [
            "A 'jiffy' is an actual unit of time, specifically 1/100th of a second.",
            "The first product to be sold on the internet was a Sting CD for $12.48 on August 11, 1994.",
            "A group of porcupines is called a prickle."
        ]
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """Generate a multiple-choice quiz question for the chosen topic."""
    questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Markup Locator", "Hypertext Markup Link", "Hypertext Markup Lexicon"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Babylonians", "Mayans", "Egyptians", "Greeks"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Attack on Pearl Harbor", "Fall of the Berlin Wall", "Sinking of the Lusitania"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Thailand"],
                "answer": 1
            }
        ]
    }
    return random.choice(questions[topic])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter the number of your chosen topic: "))

    topic_map = {
        1: "science",
        2: "technology",
        3: "history",
        4: "general"
    }

    chosen_topic = topic_map[topic_choice]
    print(f"\nYour chosen topic is: {chosen_topic.capitalize()}")

    print("\nHere's a random fact or concept about your chosen topic:")
    print(get_random_fact(chosen_topic))

    print("\nNow, let's test your knowledge with a multiple-choice quiz!")
    quiz_data = quiz_question(chosen_topic)
    print(quiz_data["question"])
    for i, option in enumerate(quiz_data["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter the number of your answer: "))
    if user_answer - 1 == quiz_data["answer"]:
        print("Correct! You're a knowledge champion!")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
