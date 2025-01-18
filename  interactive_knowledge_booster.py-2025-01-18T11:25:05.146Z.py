
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "Sharks have been around for over 400 million years, predating the dinosaurs."
        ],
        "quiz_questions": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood throughout the body", "To filter waste from the blood", "To produce insulin", "To control breathing"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 2
            },
            {
                "question": "What is the primary component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Water vapor"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first text message was sent on December 3, 1992, and read 'Merry Christmas'."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of a computer's CPU?",
                "options": ["To store data", "To process data", "To display data", "To input data"],
                "answer": 1
            },
            {
                "question": "What is the purpose of a computer's operating system?",
                "options": ["To control hardware and software", "To run applications", "To protect the computer from viruses", "All of the above"],
                "answer": 3
            },
            {
                "question": "Which of these is not a common type of computer memory?",
                "options": ["RAM", "ROM", "CPU", "SSD"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first Olympics were held in 776 BC in Olympia, Greece."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Biplane", "The Wright Flyer"],
                "answer": 3
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest desert in the world is Antarctica, which is a desert because of its low precipitation.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.",
            "A group of flamingos is called a flamboyance."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
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
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def run_quiz(topic):
    """
    Runs an interactive quiz for the selected topic.
    """
    score = 0
    num_questions = 3
    
    print(f"Welcome to the {topic.upper()} quiz!")
    
    for _ in range(num_questions):
        question, options, answer = get_quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        
        print()
    
    print(f"Your final score is {score} out of {num_questions}.")

def main():
    """
    Displays the topic menu and runs the selected topic's interactive session.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics.keys():
        print(f"- {topic.upper()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\n{get_random_fact(selected_topic)}\n")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
