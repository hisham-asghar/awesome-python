
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quizzes": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the sun?",
                "options": ["Gravity", "Centrifugal force", "Electromagnetic force", "Friction"],
                "answer": 0
            },
            {
                "question": "Which scientist is famous for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company is known for developing the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the process by which a computer executes a series of instructions?",
                "options": ["Rendering", "Compilation", "Execution", "Iteration"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Babylonian", "Egyptian", "Greek", "Chinese"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers in 1903?",
                "options": ["The Flyer", "The Biplane", "The Glider", "The Kite"],
                "answer": 0
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "North America", "Europe"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the given topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["question"], quiz["options"]

def check_answer(topic, answer_index):
    """
    Checks if the user's answer is correct for the given topic and answer index.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["answer"] == answer_index

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Tool!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    topic = input("Enter your choice: ").lower()
    if topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {topic.capitalize()}:")
    print(get_random_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options = get_quiz_question(topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    answer = int(input("Enter your answer (1-4): "))
    if check_answer(topic, answer - 1):
        print("Correct! You're a knowledge champion!")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
