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
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2021 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercial text message was sent on December 3, 1992.",
            "The world's first programmable computer was the ENIAC, which was completed in 1946."
        ],
        "quiz": [
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language that is commonly used for web development?",
                "options": ["Java", "Python", "C++", "JavaScript"],
                "answer": 3
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Printer", "Amplifier"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "In what year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "Which ancient civilization is known for its advanced engineering and architectural achievements?",
                "options": ["Greek", "Roman", "Egyptian", "Chinese"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest continent in the world is Asia.",
            "The tallest mammal in the world is the giraffe."
        ],
        "quiz": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                "answer": 0
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz"])
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
