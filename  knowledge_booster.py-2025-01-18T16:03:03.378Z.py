
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of flamingos is called a 'flamboyance'."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": "Gravity"
            },
            {
                "question": "Which organ in the human body produces insulin?",
                "options": ["Heart", "Liver", "Pancreas", "Kidneys"],
                "answer": "Pancreas"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was the size of a large room and weighed 30 tons.",
            "The 'qwerty' keyboard layout was designed to slow down typists to prevent mechanical typewriters from jamming.",
            "The first cellphone call was made on April 3, 1973, by Martin Cooper of Motorola."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first graphical user interface (GUI) for personal computers?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": "Xerox"
            },
            {
                "question": "What is the name of the software that allows multiple users to access a computer system simultaneously?",
                "options": ["Operating System", "Web Browser", "Antivirus", "Database"],
                "answer": "Operating System"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first woman to win a Nobel Prize was Marie Curie, who won the Nobel Prize in Physics in 1903."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Greek", "Roman", "Egyptian", "Aztec"],
                "answer": "Egyptian"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["D-Day", "The Holocaust", "The atomic bombings of Hiroshima and Nagasaki", "The fall of the Berlin Wall"],
                "answer": "The atomic bombings of Hiroshima and Nagasaki"
            }
        ]
    },
    "general": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "A 'jiffy' is an actual unit of time, measuring one-hundredth of a second.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the name of the tallest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
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
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs the quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if question["options"][user_answer - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that runs the interactive knowledge booster.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
