Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The deepest known cave in the world is Veryovkina Cave in Abkhazia, Georgia, with a depth of 2,212 meters (7,257 feet)."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": "Albert Einstein"
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
            "The first electronic computer, ENIAC, was 30 feet long, 8 feet high, and weighed 30 tons.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola."
        ],
        "quizzes": [
            {
                "question": "What does the term 'USB' stand for?",
                "options": ["Universal Serial Bus", "Unified System Bus", "Universal System Bridge", "Unified Serial Backup"],
                "answer": "Universal Serial Bus"
            },
            {
                "question": "Which company created the first commercially successful search engine?",
                "options": ["Microsoft", "Apple", "Google", "Yahoo"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from the 1st century BC to the 5th century AD.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematical and astronomical knowledge?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": "Mayans"
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands and raises the structure.",
            "The world's largest desert is Antarctica, which is a desert because it receives very little precipitation.",
            "The first person to circumnavigate the globe was the Portuguese explorer Ferdinand Magellan, although he did not complete the entire journey himself."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": "Japan"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic.capitalize()}:\n{fact}")

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"\nQuiz about {topic.capitalize()}:")
    print(quiz["question"])
    for option in quiz["options"]:
        print(f"- {option}")
    user_answer = input("Enter your answer: ")
    if user_answer.lower() == quiz["answer"].lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz['answer']}.")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
