
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 37.2 trillion cells.",
            "The sun is about 93 million miles (150 million km) from Earth.",
            "The largest known prime number as of 2022 has 23 million digits.",
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "choices": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": "Gravity"
            },
            {
                "question": "Which scientist is famous for developing the theory of relativity?",
                "choices": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The largest hard drive currently available has a capacity of 20TB.",
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "choices": ["Windows", "Linux", "macOS", "Android"],
                "answer": "macOS"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "choices": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles (21,000 km).",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first president of the United States?",
                "choices": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did World War II end?",
                "choices": ["1945", "1939", "1918", "1950"],
                "answer": "1945"
            },
            {
                "question": "What was the name of the ancient civilization that built the Machu Picchu site in Peru?",
                "choices": ["Aztec", "Maya", "Inca", "Olmec"],
                "answer": "Inca"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The fastest land animal is the cheetah, which can reach speeds of up to 75 mph (120 km/h).",
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Mars", "Saturn", "Jupiter", "Venus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "choices": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the capital city of Australia?",
                "choices": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
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
    Retrieves a random quiz question from the specified topic.
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
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}. {choice}")

    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if question["choices"][int(user_answer)-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Invalid input. Please try again.")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print(f"\nA random fact about {chosen_topic.capitalize()} is: {get_random_fact(chosen_topic)}")
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
