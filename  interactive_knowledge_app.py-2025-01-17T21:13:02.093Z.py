
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has 206 bones.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Photosynthesis is the process by which plants convert light energy into chemical energy."
        ],
        "quizzes": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood", "To digest food", "To breathe"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Energy"],
                "answer": 3
            },
            {
                "question": "What is the chemical formula for water?",
                "options": ["H2O", "CO2", "NaCl", "O2"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Management Language", "Hyper Transmission Markup Language", "Hypertext Modeling Language"],
                "answer": 0
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mozilla Firefox", "Google Chrome", "Internet Explorer", "Mosaic"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The American Declaration of Independence was signed on July 4, 1776."
        ],
        "quizzes": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
                "answer": 1
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1942", "1950"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23,249,425 digits.",
            "The largest known organism on Earth is a fungus that covers an area of 2,200 acres in Oregon.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Green", "Yellow"],
                "answer": 2
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
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (0-3): "))
    if user_answer == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Exiting...")
        return

    print(f"You selected: {selected_topic.capitalize()}")
    print(get_random_fact(selected_topic))
    print()

    quiz = get_quiz(selected_topic)
    score = run_quiz(quiz)
    print(f"Your score: {score} out of 1")

if __name__ == "__main__":
    main()
