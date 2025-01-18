Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The first computer bug was a real moth trapped in a Harvard Mark II computer."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Magnetism", "Friction", "Electricity"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The internet was originally called ARPANET, and it was created by the U.S. Department of Defense."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Router", "Modem", "Switch", "Amplifier"],
                "answer": "Modem"
            },
            {
                "question": "What is the name of the process by which a computer executes a series of instructions?",
                "options": ["Compilation", "Interpretation", "Execution", "Rendering"],
                "answer": "Execution"
            }
        ]
    },
    "history": {
        "facts": [
            "The first known written alphabet was developed by the Phoenicians around 1500 BC.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Eiffel Tower was built in 1889 as the entrance arch for the World's Fair."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": "Mayans"
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers?",
                "options": ["Kitty Hawk", "Wright Flyer", "Concorde", "Sputnik"],
                "answer": "Wright Flyer"
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "Pearl Harbor", "V-E Day", "Hiroshima"],
                "answer": "V-E Day"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["K2", "Everest", "Kilimanjaro", "Denali"],
                "answer": "Everest"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Yuan", "Won", "Rupee"],
                "answer": "Yen"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your topic choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow let's test your knowledge with a quiz!")
    quiz_question = get_quiz_question(selected_topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number of your answer: ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct! You're a knowledge champion!")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    run_knowledge_app()