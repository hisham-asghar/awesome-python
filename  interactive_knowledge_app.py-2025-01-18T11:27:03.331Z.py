
import random
import json
import requests

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Earth's core is as hot as the surface of the Sun.",
            "Honey is the only food that does not spoil."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which organ in the human body produces insulin?",
                "options": ["Heart", "Liver", "Pancreas", "Kidney"],
                "answer": "Pancreas"
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Friction", "Magnetism", "Centrifugal"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and occupied 1,800 square feet.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge."
        ],
        "quiz_questions": [
            {
                "question": "What does 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Computer Processing Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": "Xerox"
            },
            {
                "question": "What is the name of the software that translates high-level programming languages into machine-readable code?",
                "options": ["Compiler", "Interpreter", "Assembler", "Linker"],
                "answer": "Compiler"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization built the Hanging Gardens of Babylon?",
                "options": ["Egyptian", "Greek", "Roman", "Babylonian"],
                "answer": "Babylonian"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Sinking of the Lusitania", "Invasion of Poland", "Battle of the Somme"],
                "answer": "Assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "A 'jiffy' is an actual unit of time, equivalent to one-thousandth of a second."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Yuan", "Euro", "Yen", "Dollar"],
                "answer": "Yen"
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
    quiz_questions = topics[topic]["quiz_questions"]
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
    
    user_answer = input("Enter the number of your answer: ")
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["answer"])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
