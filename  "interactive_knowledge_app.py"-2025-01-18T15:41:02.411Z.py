
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The world's largest known prime number has over 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "What is the fastest-growing organ in the human body?",
                "options": ["Brain", "Liver", "Skin", "Hair"],
                "answer": 2
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first digital camera, the Mavica, was developed by Sony in 1981."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercial web browser?",
                "options": ["Microsoft", "Apple", "Netscape", "IBM"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "IBM PC", "Commodore 64", "Altair 8800"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Colosseum in Rome was built in the 1st century AD and could hold up to 80,000 people.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Mayans", "Incas", "Egyptians", "Aztecs"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful American space mission?",
                "options": ["Apollo 11", "Gemini 3", "Mercury-Redstone 3", "Sputnik 1"],
                "answer": 2
            },
            {
                "question": "Which country was the first to grant women the right to vote?",
                "options": ["United States", "United Kingdom", "New Zealand", "Sweden"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has over 23 million digits.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2022 has over 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
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

def get_random_quiz(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["question"], quiz["options"], quiz["answer"]

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question, options, answer = get_random_quiz(topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", options[answer])

def main():
    """
    Main function that runs the interactive knowledge app.
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
