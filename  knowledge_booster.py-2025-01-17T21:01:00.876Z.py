
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the nearest star to our solar system?",
                "options": ["Sirius", "Proxima Centauri", "Betelgeuse", "Andromeda"],
                "answer": "Proxima Centauri"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first programmable computer was the ENIAC, which was completed in 1946."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "Blackberry"],
                "answer": "Blackberry"
            },
            {
                "question": "What is the name of the technology used to transmit data wirelessly between devices?",
                "options": ["Bluetooth", "Wi-Fi", "Cellular", "Infrared"],
                "answer": "Bluetooth"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 1,000 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
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
                "question": "What was the name of the ancient civilization that built the Colosseum in Rome?",
                "options": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": "Romans"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest continent in the world is Asia.",
            "The tallest mammal in the world is the giraffe."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "Maya Angelou"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    question = random.choice(topics[topic]["quiz_questions"])
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
