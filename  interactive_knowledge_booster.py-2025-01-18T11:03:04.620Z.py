
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Venus"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the device used to input data into a computer?",
                "options": ["Monitor", "Keyboard", "Printer", "Mouse"],
                "answer": "Keyboard"
            },
            {
                "question": "What is the name of the first commercially successful personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": "IBM PC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.",
            "The American Civil War lasted from 1861 to 1865."
        ],
        "quiz_questions": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer", "The Airplane"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion caused by the heating of the iron."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
                "answer": "Nile River"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["North America", "Asia", "Africa", "Europe"],
                "answer": "Asia"
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
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if question['options'][int(user_answer) - 1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that displays the menu and handles user input.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
