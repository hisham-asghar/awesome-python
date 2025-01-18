
import random
import json
import requests

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API or predefined database.
    """
    # Replace this with your actual API call or database lookup
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "The largest known prime number as of 2023 has over 23 million digits."
        ],
        "technology": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense in the 1960s.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (19.7 feet) tall.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ]
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using a public API or predefined database.
    """
    # Replace this with your actual API call or database lookup
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Jupiter", "Venus", "Mars", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hyper Text Markup Language", "Hypertext Markup Lingo", "Hypertext Markup Library"],
                "answer": 0
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "IBM PC", "Commodore 64", "Altair 8800"],
                "answer": 1
            }
        ],
        "history": [
            {
                "question": "In what year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1848"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamians", "Mayans", "Incas", "Egyptians"],
                "answer": 3
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["African Elephant", "Blue Whale", "Sperm Whale", "Fin Whale"],
                "answer": 1
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            }
        ]
    }
    return random.choice(quiz_data[topic])

def run_interactive_quiz(topic):
    """
    Runs an interactive quiz for the specified topic, allowing the user to test their knowledge.
    """
    print(f"Welcome to the {topic.capitalize()} quiz!")
    print("Try to answer the multiple-choice questions correctly.")

    score = 0
    question = quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == question["answer"] + 1:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

    print(f"Your score: {score}/1")

def main():
    """
    Main function that presents the topic menu and runs the interactive quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Choose a topic to get started:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter your choice (1-4): "))
    topics = ["science", "technology", "history", "general"]
    topic = topics[topic_choice - 1]

    print("\nHere's a random fact about", topic.capitalize() + ":")
    print(get_random_fact(topic))
    print()

    run_interactive_quiz(topic)

if __name__ == "__main__":
    main()
