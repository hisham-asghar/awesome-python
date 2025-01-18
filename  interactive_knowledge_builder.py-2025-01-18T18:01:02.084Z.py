
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Fermentation", "Digestion"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetism", "Centrifugal force"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer bug was a real bug (a moth) trapped in a Harvard Mark II computer.",
            "The 'qwerty' keyboard layout was designed to slow down typists to prevent jams on early typewriters.",
            "The first commercial internet service provider (ISP) was launched in 1989 and was called The World."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser, developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            },
            {
                "question": "What is the name of the company that developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz_questions": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Spirit of St. Louis", "The Wright Flyer", "The Kitty Hawk", "The Concorde"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful moon landing mission?",
                "options": ["Apollo 8", "Apollo 11", "Apollo 13", "Gemini 7"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The first product to have a barcode was Wrigley's gum.",
            "The king of hearts is the only king without a mustache on a standard playing card.",
            "A 'jiffy' is an actual unit of time, equivalent to one-hundredth of a second."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Moose", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile", "Amazon", "Mississippi", "Yangtze"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
