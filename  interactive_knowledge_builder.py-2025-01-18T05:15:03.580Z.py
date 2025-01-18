
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of red blood cells?",
                "choices": ["Carrying oxygen", "Producing insulin", "Filtering waste"],
                "answer": "Carrying oxygen"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "choices": ["Jupiter", "Saturn", "Uranus"],
                "answer": "Saturn"
            },
            {
                "question": "What is the process by which living organisms produce their own food?",
                "choices": ["Photosynthesis", "Respiration", "Digestion"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and occupied 1,800 square feet.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "Python", "C++"],
                "answer": "Python"
            },
            {
                "question": "What is the primary function of a computer's CPU?",
                "choices": ["Storing data", "Displaying images", "Processing information"],
                "answer": "Processing information"
            },
            {
                "question": "What is the name of the first commercial smartphone?",
                "choices": ["iPhone", "BlackBerry", "Simon Personal Communicator"],
                "answer": "Simon Personal Communicator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2500 BC and are the oldest and largest of the three pyramids.",
            "The Renaissance period in Europe lasted from the 14th to the 17th century and was a time of great cultural and intellectual flourishing."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "choices": ["Mesopotamia", "Ancient Greece", "Ancient Egypt"],
                "answer": "Ancient Greece"
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers in 1903?",
                "choices": ["The Flyer", "The Glider", "The Kite"],
                "answer": "The Flyer"
            },
            {
                "question": "Which famous explorer is credited with discovering the Americas?",
                "choices": ["Christopher Columbus", "Vasco da Gama", "Marco Polo"],
                "answer": "Christopher Columbus"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal in the world is the giraffe."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "choices": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "choices": ["Amazon River", "Nile River", "Mississippi River"],
                "answer": "Nile River"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "choices": ["Asia", "Africa", "Europe"],
                "answer": "Asia"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Fetches a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Fetches a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, choice in enumerate(quiz_question["choices"], start=1):
        print(f"{i}. {choice}")
    
    while True:
        user_answer = input("Enter your answer (1-3): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(quiz_question["choices"]):
            if quiz_question["choices"][int(user_answer) - 1] == quiz_question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please try again.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic in topics:
            print(f"\nRandom fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            print("\nLet's test your knowledge!")
            run_quiz(selected_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
