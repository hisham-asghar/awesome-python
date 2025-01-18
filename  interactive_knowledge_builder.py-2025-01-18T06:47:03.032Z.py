
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than Mount Everest."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce oxygen"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Energy"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Neptune"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first microprocessor, the Intel 4004, was introduced in 1971."
        ],
        "quiz_questions": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Management Language", "Hyper Text Machine Language", "Hyperlink Text Markup Language"],
                "answer": 0
            },
            {
                "question": "Which of these is not a type of computer memory?",
                "options": ["RAM", "ROM", "CPU", "SSD"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful personal computer?",
                "options": ["Apple I", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight lasted only 12 seconds and covered 120 feet."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Bleriot XI"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first product to have a barcode was Wrigley's gum.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion causing the iron to expand, and get slightly taller."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"]

def check_answer(topic, answer_index):
    """
    Checks if the user's answer is correct for the given quiz question.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["answer"] == answer_index

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"Here's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))
    print()

    print(f"Now, let's test your knowledge with a quiz on {selected_topic.capitalize()}!")
    question, options = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your answer (0-2): "))
    if check_answer(selected_topic, user_answer):
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
