Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": 0
            },
            {
                "question": "Which of these is a non-renewable energy source?",
                "options": ["Solar", "Wind", "Hydroelectric", "Fossil Fuels"],
                "answer": 3
            },
            {
                "question": "What is the name of the closest star to our solar system?",
                "options": ["Betelgeuse", "Sirius", "Proxima Centauri", "Andromeda"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer bug was a real moth trapped in a Harvard Mark II computer.",
            "The world's first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The first commercial electronic computer, UNIVAC I, was delivered to the U.S. Census Bureau in 1951."
        ],
        "quiz_questions": [
            {
                "question": "What does the term 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Modular Language", "Hyperlink Text Modular Language"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1775", "1941"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Aztec", "Inca", "Ancient Egypt"],
                "answer": 3
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest organ in the human body is the skin.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. Better luck next time!")

    print("\nThank you for using the Interactive Knowledge App!")

# Run the interactive knowledge application
run_interactive_knowledge_app()
