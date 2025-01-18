
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz": [
            {
                "question": "What is the name of the process that plants use to convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Magnetism", "Friction", "Electricity"],
                "answer": 0
            },
            {
                "question": "What is the name of the gas that makes up approximately 78% of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language that is widely used for web development?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": 3
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Amplifier", "Converter"],
                "answer": 0
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Infrared"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BCE.",
            "The Roman Empire lasted for over 1,000 years, from 27 BCE to 476 CE."
        ],
        "quiz": [
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Roanoke Colony", "New Amsterdam"],
                "answer": 0
            },
            {
                "question": "What was the name of the war that took place between 1939 and 1945?",
                "options": ["World War I", "World War II", "Vietnam War", "Korean War"],
                "answer": 1
            },
            {
                "question": "What was the name of the ancient civilization that developed in Mesopotamia between the Tigris and Euphrates rivers?",
                "options": ["Aztec", "Inca", "Mesopotamian", "Egyptian"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal in the world is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest organ in the human body is the skin, which covers an area of about 2 square meters.",
            "The largest ocean on Earth is the Pacific Ocean, which covers an area of about 63 million square miles."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Africa", "Asia", "North America", "South America"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest bone in the human body?",
                "options": ["Femur", "Tibia", "Humerus", "Radius"],
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
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz = topics[topic]["quiz"]
    question = random.choice(quiz)
    return question["question"], question["options"], question["answer"]

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Exiting the application.")
        return

    print(f"You selected: {selected_topic.capitalize()}")
    print(get_random_fact(selected_topic))
    print()

    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", options[answer])

if __name__ == "__main__":
    run_interactive_knowledge_app()
