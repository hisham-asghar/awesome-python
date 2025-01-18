
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Water is the only substance on Earth that is naturally found in three forms: solid, liquid, and gas.",
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical formula for water?",
                "options": ["H2O", "CO2", "NaCl", "O2"],
                "answer": 0
            },
            {
                "question": "Which of these is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Condensation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial barcode was scanned on June 26, 1974, at a Marsh supermarket in Troy, Ohio.",
            "The internet was originally known as ARPANET, which was created by the U.S. Department of Defense in 1969.",
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser, developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, signed in 1215, is considered one of the most important legal documents in the history of democracy.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematical and astronomical knowledge?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
                "answer": 1
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1941", "1947"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23,249,425 digits.",
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis, a type of lung disease.",
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Green", "Yellow"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
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
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_interactive_learning():
    """
    Runs the interactive learning program.
    """
    print("Welcome to the Interactive Learning Program!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))
    print("\nLet's test your knowledge with a quiz!")

    quiz_question = get_quiz_question(selected_topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

    print("\nThank you for using the Interactive Learning Program!")

if __name__ == "__main__":
    run_interactive_learning()
