
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than Mount Everest."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that holds the planets in orbit around the Sun?",
                "options": ["Gravity", "Magnetism", "Centrifugal force", "Friction"],
                "answer": "Gravity"
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that causes objects to fall towards the Earth?",
                "options": ["Gravity", "Magnetism", "Centrifugal force", "Friction"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was called 'The Creeper' and was created in 1971.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first website was created in 1991 by Tim Berners-Lee."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language that is commonly used for web development?",
                "options": ["Python", "Java", "JavaScript", "C++"],
                "answer": "JavaScript"
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": "Modem"
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Infrared"],
                "answer": "Bluetooth"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560-2540 BCE, making them over 4,500 years old.",
            "The Roman Empire lasted for over 400 years, from 27 BCE to 476 CE."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Roanoke Colony", "New Amsterdam"],
                "answer": "Jamestown"
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Bleriot XI", "The Spirit of St. Louis"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "What was the name of the event that marked the beginning of World War I?",
                "options": ["The Assassination of Archduke Franz Ferdinand", "The Sinking of the Lusitania", "The Zimmermann Telegram", "The Battle of the Somme"],
                "answer": "The Assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest planet in our solar system is Jupiter."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
                "answer": "Yen"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe", "North America"],
                "answer": "Asia"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
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
    Runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
