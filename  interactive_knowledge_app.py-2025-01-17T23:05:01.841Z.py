
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "Bees have five eyes: two compound eyes and three simple eyes."
        ],
        "quiz": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood throughout the body", "To filter waste from the blood", "To produce insulin"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Energy"],
                "answer": 3
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had 2,300 transistors.",
            "The internet was originally called ARPANET, and it was created by the U.S. Department of Defense."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
                "answer": 2
            },
            {
                "question": "What does the acronym 'RAM' stand for?",
                "options": ["Random Access Memory", "Read-only Memory", "Rapid Access Memory", "Resistive Array Memory"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight lasted only 12 seconds and covered 120 feet."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Greek", "Roman", "Egyptian", "Mayan"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Benjamin Franklin", "George Washington", "Abraham Lincoln"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first product to have a barcode was Wrigley's gum.",
            "A group of flamingos is called a 'flamboyance'."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
                "answer": 2
            },
            {
                "question": "Which of these is not a type of weather phenomenon?",
                "options": ["Tornado", "Earthquake", "Blizzard", "Hurricane"],
                "answer": 1
            },
            {
                "question": "What is the tallest building in the world?",
                "options": ["Burj Khalifa", "One World Trade Center", "Shanghai Tower", "Abraj Al-Bait"],
                "answer": 0
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
    quiz = topics[topic]["quiz"]
    question = random.choice(quiz)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print("\nHere's a random fact about", chosen_topic.capitalize() + ":")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
