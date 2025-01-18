
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "quiz_questions": [
            {
                "question": "Which of the following is NOT a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": "Plasma"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first digital computer, ENIAC, was completed in 1946.",
            "The term 'robot' was first used in 1920 in the play 'R.U.R.' by Karel Čapek."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Cellular", "Infrared"],
                "answer": "Bluetooth"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Egypt", "China"],
                "answer": "Egypt"
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Bleriot XI"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The sinking of the Lusitania", "The Treaty of Versailles", "The Battle of the Somme"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the largest continent by land area?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": "Asia"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Yuan", "Dollar", "Euro"],
                "answer": "Yen"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_random_quiz_question(topic):
    """
    Returns a random quiz question from the selected topic.
    """
    return random.choice(topics[topic]["quiz_questions"])

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_random_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer)-1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    while True:
        print("\nSelect a topic:")
        for topic in topics.keys():
            print(f"- {topic.capitalize()}")
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            print("\nLet's test your knowledge with a quiz!")
            run_quiz(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
