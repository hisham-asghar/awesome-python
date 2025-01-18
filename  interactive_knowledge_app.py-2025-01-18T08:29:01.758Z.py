
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Oxidation"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and occupied 1,800 square feet.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The first commercial website, www.info.cern.ch, was launched in 1991."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the software that translates human-readable code into machine-readable instructions?",
                "options": ["Compiler", "Interpreter", "Debugger", "Linker"],
                "answer": "Compiler"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": "Modem"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Eiffel Tower was built in 1889 for the Paris World's Fair and was the tallest structure in the world for 41 years.",
            "The first successful powered flight by the Wright brothers took place on December 17, 1903."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Lewis and Clark Expedition", "The Apollo 11 Mission"],
                "answer": "The Magellan Expedition"
            },
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Kitty Hawk", "The Spirit of St. Louis", "The Flyer", "The Wright Flyer"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["Elephant", "Hippopotamus", "Giraffe", "Blue Whale"],
                "answer": "Blue Whale"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Mount Everest"
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
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.strip() == str(question['options'].index(question['answer']) + 1):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
