
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first confirmed black hole was discovered in 1971."
        ],
        "quiz_questions": [
            {
                "question": "Which of these is not a fundamental force in nature?",
                "options": ["Gravity", "Electromagnetism", "Strong Nuclear Force", "Weak Nuclear Force", "Magnetism"],
                "answer": 4
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Europa", "Callisto", "Io"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971.",
            "The world's first text message was sent on December 3, 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby", "JavaScript"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome", "WorldWideWeb"],
                "answer": 4
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical connection?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Fiber Optic", "Satellite"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Roman", "Greek", "Egyptian", "Mesopotamian", "Aztec"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Vasco da Gama Expedition", "The Drake Circumnavigation", "The Leif Erikson Voyage"],
                "answer": 0
            },
            {
                "question": "Which event is considered the starting point of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The rise of the Nazi Party", "The Cuban Missile Crisis", "The fall of the Berlin Wall"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can reach up to 6 meters (19.7 feet) in height.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first known use of the word 'OK' was in a Boston Morning Post article on March 23, 1839."
        ],
        "quiz_questions": [
            {
                "question": "Which of these is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Southern Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest continent by land area?",
                "options": ["Africa", "Asia", "North America", "South America", "Europe"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest bone in the human body?",
                "options": ["Femur", "Tibia", "Humerus", "Radius", "Ulna"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic, with multiple-choice questions.
    """
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        quiz_question = get_quiz_question(topic)
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-5): ")) - 1
        if user_answer == quiz_question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is: {score}/{num_questions}")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
