
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has approximately 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The largest known prime number has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The term 'bug' was first used in computer programming in 1947 when a moth was found in a Harvard Mark II computer.",
            "The world's first text message was sent on December 3, 1992, and read 'Merry Christmas'."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "macOS", "Linux", "Android"],
                "answer": "macOS"
            },
            {
                "question": "Which technology company is known for its search engine?",
                "options": ["Apple", "Microsoft", "Google", "Amazon"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the programming language that is often used for data analysis and machine learning?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Greek", "Roman", "Egyptian", "Mayan"],
                "answer": "Egyptian"
            },
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "Which explorer is credited with discovering America?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Magellan", "Marco Polo"],
                "answer": "Christopher Columbus"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": "Japan"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
