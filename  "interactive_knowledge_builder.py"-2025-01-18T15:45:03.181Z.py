
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy has over 200 billion stars.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Cu", "Pb"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first email was sent in 1971 by Ray Tomlinson.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the search engine created by Larry Page and Sergey Brin?",
                "options": ["Yahoo", "Bing", "Google", "DuckDuckGo"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight by the Wright brothers took place in 1903."
        ],
        "quiz_questions": [
            {
                "question": "What year did the United States declare independence?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the war that lasted from 1939 to 1945?",
                "options": ["World War I", "World War II", "The Cold War", "The Vietnam War"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows.",
            "The first novel ever written was 'The Tale of Genji' by Murasaki Shikibu, published in 1007."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Who is the author of the 'Harry Potter' book series?",
                "options": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "Suzanne Collins"],
                "answer": 0
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
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
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"You selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
