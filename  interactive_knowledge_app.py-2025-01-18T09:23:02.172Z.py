
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first known computer bug was a real bug - a moth trapped in a Harvard Mark II computer.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quiz_questions": [
            {
                "question": "What is the element with the symbol 'H' on the periodic table?",
                "options": ["Helium", "Hydrogen", "Helium", "Halogens"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Friction", "Centrifugal Force", "Magnetism"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Osmosis"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first computer mouse was invented by Douglas Engelbart in 1964 and had only one button.",
            "The term 'computer bug' was coined after a moth was found trapped in a Harvard Mark II computer in 1947."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular"],
                "answer": 1
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals for transmission over telephone lines?",
                "options": ["Modem", "Router", "Switch", "Firewall"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Gutenberg Bible, printed in 1455, was the first major book printed in the West using movable metal type.",
            "The first successful powered flight occurred on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1776", "1914"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Lewis and Clark Expedition", "The Apollo 11 Mission"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The longest English word without repeating letters is 'uncopyrightable'.",
            "The first person to circumnavigate the globe was Ferdinand Magellan, although he was killed in the Philippines and did not complete the voyage himself."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == quiz_question["answer"] + 1:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
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
