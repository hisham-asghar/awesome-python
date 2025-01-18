
import random
import json
import requests

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 37.2 trillion cells.",
            "The first confirmed meteorite impact occurred in Ensisheim, France in 1492.",
            "The hottest planet in the Solar System is Venus, with an average surface temperature of 462°C (864°F)."
        ],
        "quizzes": [
            {
                "question": "What is the scientific name for the study of living organisms?",
                "options": ["Biology", "Astronomy", "Geology", "Chemistry"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial cellphone call was made by Martin Cooper of Motorola in 1973.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "Python", "C++", "Ruby"],
                "answer": 1
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Android", "Nokia"],
                "answer": 1
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quizzes": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1945"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful European expedition to circumnavigate the globe?",
                "options": ["Christopher Columbus", "Magellan", "Vasco da Gama", "Marco Polo"],
                "answer": 1
            },
            {
                "question": "What was the name of the ancient Greek philosopher who is considered the father of Western philosophy?",
                "options": ["Plato", "Aristotle", "Socrates", "Pythagoras"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quizzes": [
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe", "North America"],
                "answer": 0
            },
            {
                "question": "What is the name of the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Dollar", "Euro", "Pound", "Yen"],
                "answer": 3
            }
        ]
    }
}

def interactive_learning():
    print("Welcome to the Interactive Learning Program!")
    print("Please select a topic:")
    
    # Display the available topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic.capitalize()}")
    
    # Get the user's topic choice
    choice = int(input("Enter the number of the topic: "))
    
    # Get a random fact from the chosen topic
    topic_name = list(topics.keys())[choice - 1]
    fact = random.choice(topics[topic_name]["facts"])
    print(f"\nFact: {fact}")
    
    # Display a quiz for the chosen topic
    quiz = random.choice(topics[topic_name]["quizzes"])
    print(f"\nQuiz: {quiz['question']}")
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    user_answer = int(input("Enter the number of your answer: "))
    
    # Check the user's answer and provide feedback
    if user_answer - 1 == quiz["answer"]:
        print("Correct! Well done.")
    else:
        print("Incorrect. Better luck next time.")

if __name__ == "__main__":
    interactive_learning()
