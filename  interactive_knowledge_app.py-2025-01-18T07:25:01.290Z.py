
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer was the ENIAC, which was completed in 1946.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
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
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made by Martin Cooper of Motorola in 1973.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What does the acronym 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Central Power Unit"],
                "answer": 0
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Google Chrome"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Roanoke Colony", "New Amsterdam"],
                "answer": 0
            },
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Benjamin Franklin", "George Washington", "Abraham Lincoln"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
                "answer": 1
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
    Retrieves a random quiz question from the specified topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
