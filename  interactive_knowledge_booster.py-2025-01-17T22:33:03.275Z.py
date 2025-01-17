
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has 206 bones.",
            "The largest organ in the human body is the skin.",
            "Photosynthesis is the process by which plants convert sunlight into energy."
        ],
        "quiz": [
            {
                "question": "What is the term for the study of living organisms?",
                "options": ["Astronomy", "Biology", "Geology"],
                "answer": "Biology"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electricity"],
                "answer": "Gravity"
            },
            {
                "question": "What is the name of the chemical element with the symbol H?",
                "options": ["Helium", "Hydrogen", "Helium"],
                "answer": "Hydrogen"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964.",
            "The World Wide Web was invented in 1989 by Tim Berners-Lee.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the technology used to send data wirelessly between devices?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet"],
                "answer": "Bluetooth"
            },
            {
                "question": "What is the name of the company that created the first commercially successful personal computer?",
                "options": ["Apple", "Microsoft", "IBM"],
                "answer": "IBM"
            }
        ]
    },
    "history": {
        "facts": [
            "The first pyramids were built in Egypt around 2700 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Gutenberg printing press was invented in 1440, revolutionizing the spread of information."
        ],
        "quiz": [
            {
                "question": "What is the name of the ancient Greek philosopher who is considered the 'father of democracy'?",
                "options": ["Plato", "Aristotle", "Socrates"],
                "answer": "Socrates"
            },
            {
                "question": "What is the name of the war that lasted from 1939 to 1945?",
                "options": ["World War I", "World War II", "Vietnam War"],
                "answer": "World War II"
            },
            {
                "question": "What is the name of the first successful powered flight, made by the Wright brothers in 1903?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest ocean on Earth is the Pacific Ocean.",
            "The tallest mammal is the giraffe.",
            "The Mona Lisa is a painting by the Italian artist Leonardo da Vinci."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe"],
                "answer": "Asia"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Mississippi River"],
                "answer": "Nile River"
            },
            {
                "question": "What is the name of the currency used in the United States?",
                "options": ["Euro", "Pound", "Dollar"],
                "answer": "Dollar"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-3): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
