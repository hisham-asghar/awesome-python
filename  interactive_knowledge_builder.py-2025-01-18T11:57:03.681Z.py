
import random
import json
import requests

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has 206 bones.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Water is the only substance on Earth that is naturally found in three forms: solid, liquid, and gas."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and occupied 1,800 square feet.",
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What does 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Processing Unit", "Centralized Processing Unit", "Computational Power Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the first commercial smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "IBM"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Mayans", "Incas", "Aztecs", "Egyptians"],
                "answer": "Egyptians"
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The attack on Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            },
            {
                "question": "Which famous explorer discovered America?",
                "options": ["Christopher Columbus", "Magellan", "Marco Polo", "Vasco da Gama"],
                "answer": "Christopher Columbus"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    Runs the quiz and returns the user's answer.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    return user_answer.strip()

def check_answer(quiz, user_answer):
    """
    Checks the user's answer and returns whether it's correct or not.
    """
    if user_answer == quiz["answer"]:
        return True
    else:
        return False

def main():
    """
    The main function that runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Exiting the program.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz = get_quiz(selected_topic)
    user_answer = run_quiz(quiz)
    if check_answer(quiz, user_answer):
        print("Correct! You're a knowledge champion!")
    else:
        print(f"Oops, the correct answer is: {quiz['answer']}")

    print("\nThank you for using the Interactive Knowledge Builder. Goodbye!")

if __name__ == "__main__":
    main()
