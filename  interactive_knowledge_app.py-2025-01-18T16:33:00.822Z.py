
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
        ],
        "quiz_questions": [
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
            {"question": "What is the process by which plants convert sunlight into energy?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"], "answer": 0},
            {"question": "What is the name of the largest planet in our solar system?", "options": ["Mars", "Jupiter", "Saturn", "Neptune"], "answer": 1}
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet of floor space.",
            "The first commercially available personal computer was the Altair 8800, released in 1975.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {"question": "What is the name of the programming language created by Guido van Rossum?", "options": ["Java", "C++", "Python", "Ruby"], "answer": 2},
            {"question": "What is the name of the first commercially successful smartphone?", "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"], "answer": 0},
            {"question": "What is the name of the company that created the Android operating system?", "options": ["Apple", "Microsoft", "Google", "Samsung"], "answer": 2}
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Declaration of Independence was signed in 1776."
        ],
        "quiz_questions": [
            {"question": "What was the name of the first successful powered flight, made by the Wright brothers?", "options": ["The Flyer", "The Biplane", "The Glider", "The Kite"], "answer": 0},
            {"question": "What was the name of the ancient Greek philosopher who is considered the father of modern philosophy?", "options": ["Plato", "Aristotle", "Socrates", "Pythagoras"], "answer": 2},
            {"question": "What was the name of the first successful moon landing mission?", "options": ["Apollo 8", "Apollo 11", "Apollo 13", "Apollo 17"], "answer": 1}
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and rises.",
            "The strongest muscle in the human body is the tongue."
        ],
        "quiz_questions": [
            {"question": "What is the largest ocean on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 0},
            {"question": "What is the name of the tallest mammal in the world?", "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"], "answer": 1},
            {"question": "What is the name of the currency used in Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": 0}
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
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
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
