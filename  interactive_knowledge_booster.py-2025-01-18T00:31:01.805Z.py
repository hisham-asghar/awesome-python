
import random
import requests
import json

def get_topic_menu():
    topics = {
        "1": "Science",
        "2": "Technology",
        "3": "History",
        "4": "General Knowledge"
    }
    return topics

def get_random_fact(topic):
    facts = {
        "Science": [
            "The human body contains around 100 trillion cells.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Water is the only substance that exists naturally on Earth in three forms: solid, liquid, and gas."
        ],
        "Technology": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "History": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Renaissance period in Europe lasted from the 14th to the 17th century."
        ],
        "General Knowledge": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    quiz_questions = {
        "Science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Centrifugal force", "Electromagnetic force", "Friction"],
                "answer": "Gravity"
            }
        ],
        "Technology": [
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "Abacus", "Babbage's Analytical Engine"],
                "answer": "ENIAC"
            },
            {
                "question": "What is the name of the software that translates high-level programming languages into machine code?",
                "options": ["Compiler", "Interpreter", "Debugger", "Linker"],
                "answer": "Compiler"
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": "Modem"
            }
        ],
        "History": [
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamian", "Sumerian", "Phoenician", "Egyptian"],
                "answer": "Egyptian"
            },
            {
                "question": "What was the name of the Chinese dynasty that built the Great Wall of China?",
                "options": ["Ming", "Qin", "Han", "Tang"],
                "answer": "Qin"
            },
            {
                "question": "What was the name of the ancient Greek city-state known for its democracy?",
                "options": ["Athens", "Sparta", "Corinth", "Thebes"],
                "answer": "Athens"
            }
        ],
        "General Knowledge": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Brain", "Heart", "Liver", "Skin"],
                "answer": "Skin"
            },
            {
                "question": "What is the name of the tallest mammal?",
                "options": ["Elephant", "Rhinoceros", "Giraffe", "Hippopotamus"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the name of the famous painting by Leonardo da Vinci that features a mysterious smile?",
                "options": ["The Starry Night", "The Birth of Venus", "The Persistence of Memory", "The Mona Lisa"],
                "answer": "The Mona Lisa"
            }
        ]
    }
    return random.choice(quiz_questions[topic])

def run_quiz(topic):
    question_data = get_quiz_question(topic)
    print(f"Question: {question_data['question']}")
    for i, option in enumerate(question_data['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if question_data['options'][int(user_answer) - 1] == question_data['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question_data['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    topics = get_topic_menu()
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic_choice = input("Enter your choice (1-4): ")
    
    print("\nHere's a random fact about", topics[topic_choice] + ":")
    print(get_random_fact(topics[topic_choice]))
    
    print("\nNow, let's test your knowledge with a quiz!")
    run_quiz(topics[topic_choice])

if __name__ == "__main__":
    main()
