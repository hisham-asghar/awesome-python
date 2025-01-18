Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2021 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Osmosis", "Transpiration"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Neptune"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Printer", "Converter"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BCE.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Mesopotamians"],
                "answer": 3
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["Christopher Columbus", "Ferdinand Magellan", "Vasco da Gama", "James Cook"],
                "answer": 1
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "V-E Day", "Hiroshima bombing", "Fall of Berlin"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The world's largest desert is Antarctica, which is a desert due to its low precipitation."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the smallest planet in our solar system?",
                "options": ["Mercury", "Venus", "Mars", "Earth"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
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

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYou selected the {selected_topic.capitalize()} topic.")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")

        quiz_question = get_quiz_question(selected_topic)
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == quiz_question["answer"]:
            print("Correct!")
        else:
            print("Incorrect. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

run_interactive_knowledge_app()
