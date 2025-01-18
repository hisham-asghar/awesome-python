
import random
import requests
import json

def get_fact(topic):
    """Fetch a random fact or concept from the chosen topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The sun is 93 million miles away from the Earth.",
            "Dinosaurs lived on Earth for over 150 million years."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first smartphone was the IBM Simon, released in 1992.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first Olympics were held in 776 BC in Olympia, Greece."
        ],
        "general": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.",
            "A group of porcupines is called a prickle.",
            "Maine is the only state that has a one-syllable name."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provide a multiple-choice quiz on the chosen topic."""
    questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": 2
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "choices": ["Respiration", "Photosynthesis", "Combustion", "Evaporation"],
                "answer": 1
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first programmable computer?",
                "choices": ["ENIAC", "Apple I", "IBM 5150", "Commodore 64"],
                "answer": 0
            },
            {
                "question": "What is the name of the software that allows multiple users to access a computer system at the same time?",
                "choices": ["Operating system", "Database", "Spreadsheet", "Web browser"],
                "answer": 0
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without wires?",
                "choices": ["Bluetooth", "Wi-Fi", "Ethernet", "Modem"],
                "answer": 1
            }
        ],
        "history": [
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers in 1903?",
                "choices": ["The Wright Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": 0
            },
            {
                "question": "What was the name of the ancient Egyptian queen who ruled alongside her son, Tutankhamun?",
                "choices": ["Cleopatra", "Nefertiti", "Hatshepsut", "Neferkare"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful vaccine, developed by Edward Jenner in 1796?",
                "choices": ["Smallpox", "Polio", "Measles", "Influenza"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "choices": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "choices": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "choices": ["Yen", "Won", "Renminbi", "Baht"],
                "answer": 0
            }
        ]
    }
    
    question = random.choice(questions[topic])
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["choices"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    topics = ["Science", "Technology", "History", "General"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    topic_choice = int(input("Enter your choice (1-4): ")) - 1
    topic = topics[topic_choice].lower()
    
    print(f"You have chosen the '{topics[topic_choice]}' topic.")
    print(get_fact(topic))
    
    quiz_choice = input("Would you like to take a quiz on this topic? (y/n) ")
    if quiz_choice.lower() == "y":
        quiz(topic)
    else:
        print("Okay, no problem. Have a great day!")

if __name__ == "__main__":
    main()
