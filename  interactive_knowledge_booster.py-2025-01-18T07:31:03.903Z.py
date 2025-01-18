
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mariana Trench is the deepest part of the world's oceans, reaching nearly 7 miles deep.",
            "The human brain contains around 86 billion neurons."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
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
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial cellphone call was made in 1973 by Martin Cooper of Motorola.",
            "The first digital camera was developed by Kodak in 1975."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC and are the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamian", "Aztec", "Mayan", "Egyptian"],
                "answer": 3
            },
            {
                "question": "What is the name of the famous explorer who discovered the Americas?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Magellan", "Marco Polo"],
                "answer": 0
            },
            {
                "question": "What is the name of the ancient Greek philosopher who is considered the father of modern philosophy?",
                "options": ["Plato", "Aristotle", "Socrates", "Pythagoras"],
                "answer": 2
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
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["North America", "South America", "Asia", "Africa"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def run_quiz(topic):
    """
    Runs a quiz for the given topic, with multiple-choice questions.
    """
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question, options, answer = get_quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{num_questions}")

def main():
    """
    Displays a menu for the user to select a topic, and then runs the corresponding interactive session.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nYou have chosen the {chosen_topic.capitalize()} topic.")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
