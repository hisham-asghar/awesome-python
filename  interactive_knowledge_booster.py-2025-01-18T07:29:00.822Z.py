
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quiz": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": "Plasma"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial email was sent in 1971 by Ray Tomlinson.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
            {
                "question": "What does the term 'HTTP' stand for?",
                "options": ["Hyper Text Transmission Protocol", "Hyper Text Transfer Protocol", "Hyper Textual Transfer Protocol", "Hyper Text Transforming Protocol"],
                "answer": "Hyper Text Transfer Protocol"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mozilla", "Internet Explorer", "Netscape Navigator", "Google Chrome"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for their development of the calendar and writing system?",
                "options": ["Mesopotamia", "Egypt", "China", "India"],
                "answer": "Mesopotamia"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["Flyer I", "Kitty Hawk", "Spirit of St. Louis", "Wright Flyer"],
                "answer": "Flyer I"
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["D-Day", "Pearl Harbor", "Hiroshima and Nagasaki bombings", "VE Day"],
                "answer": "Hiroshima and Nagasaki bombings"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters tall.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Venus"],
                "answer": "Jupiter"
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question["options"][user_answer - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nTime for a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
