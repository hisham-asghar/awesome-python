
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The human body is composed of about 60% water.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": 1
            },
            {
                "question": "What is the name of the element with the atomic number 8?",
                "options": ["Hydrogen", "Carbon", "Oxygen", "Nitrogen"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
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
                "question": "What is the name of the first commercial web browser?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta was a document signed by King John of England in 1215, which placed limits on the power of the monarchy.",
            "The Industrial Revolution began in the late 18th century and transformed the way goods were produced."
        ],
        "quiz": [
            {
                "question": "What year was the United States Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Spirit of St. Louis", "The Flyer", "The Kitty Hawk", "The Wright Flyer"],
                "answer": 3
            }
        ]
    },
    "general": {
        "facts": [
            "The Mona Lisa is a painting by the Italian Renaissance artist Leonardo da Vinci.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz": [
            {
                "question": "What is the largest country in the world by land area?",
                "options": ["China", "Russia", "Canada", "United States"],
                "answer": 1
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["African Elephant", "Blue Whale", "Sperm Whale", "Humpback Whale"],
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
    quiz_question = random.choice(topics[topic]["quiz"])
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
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
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
