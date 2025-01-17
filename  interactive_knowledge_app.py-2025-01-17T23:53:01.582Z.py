
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than Mount Everest."
        ],
        "quiz_questions": [
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 2
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first self-driving car was developed by Carnegie Mellon University in the 1980s."
        ],
        "quiz_questions": [
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
                "question": "What is the name of the process by which a computer's operating system is loaded into memory?",
                "options": ["Booting", "Compiling", "Rendering", "Debugging"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "Which event is considered the start of the American Civil War?",
                "options": ["The Battle of Gettysburg", "The Emancipation Proclamation", "The Assassination of Abraham Lincoln", "The Attack on Fort Sumter"],
                "answer": 3
            },
            {
                "question": "Which famous explorer is credited with discovering the Americas?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Marco Polo"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["O-", "A+", "B-", "AB-"],
                "answer": 3
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
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
