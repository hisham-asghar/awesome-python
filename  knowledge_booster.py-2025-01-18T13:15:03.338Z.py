
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The sun is approximately 93 million miles away from the Earth.",
            "The human brain has around 86 billion neurons.",
            "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into oxygen and energy in the form of sugar."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary gas produced by plants during photosynthesis?",
                "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
                "answer": 0
            },
            {
                "question": "What is the approximate diameter of the sun?",
                "options": ["1 million miles", "93 million miles", "864,000 miles", "109 times the diameter of the Earth"],
                "answer": 3
            },
            {
                "question": "How many neurons are there in the human brain?",
                "options": ["1 billion", "10 billion", "86 billion", "100 trillion"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and occupied 1,800 square feet.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What year was the first electronic computer, ENIAC, completed?",
                "options": ["1936", "1946", "1951", "1989"],
                "answer": 1
            },
            {
                "question": "Who invented the World Wide Web?",
                "options": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Linus Torvalds"],
                "answer": 2
            },
            {
                "question": "Which was the first commercial computer?",
                "options": ["ENIAC", "UNIVAC I", "IBM PC", "Apple I"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "When did the Roman Empire end?",
                "options": ["27 BC", "476 AD", "1066 AD", "1492 AD"],
                "answer": 1
            },
            {
                "question": "When did the Wright brothers make the first successful powered flight?",
                "options": ["1903", "1919", "1939", "1969"],
                "answer": 0
            },
            {
                "question": "Which is the oldest and largest of the three pyramids in the Giza pyramid complex?",
                "options": ["The Pyramid of Khafre", "The Pyramid of Menkaure", "The Great Pyramid of Giza", "The Sphinx"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest ocean on Earth is the Pacific Ocean.",
            "The Mona Lisa is a painting by the Italian Renaissance artist Leonardo da Vinci.",
            "The tallest mammal in the world is the giraffe."
        ],
        "quiz_questions": [
            {
                "question": "Which is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Michelangelo", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"],
                "answer": 3
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Hippopotamus", "Giraffe", "Rhinoceros"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print(f"Here's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("Now, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
