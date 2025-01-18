
import random
import json
import requests

# Dictionary to store topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles need more space and push the structure upwards.",
            "Apples are more effective at waking you up in the morning than coffee."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the name of the closest star to our solar system?",
                "options": ["Proxima Centauri", "Betelgeuse", "Sirius", "Polaris"],
                "answer": "Proxima Centauri"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The password for the first Apple computer was '1234'.",
            "The first domain name ever registered was Symbolics.com on March 15, 1985."
        ],
        "quiz": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Markup Lexicon", "Hyper Text Markup Linkage"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "Commodore 64", "IBM PC", "Altair 8800"],
                "answer": "Altair 8800"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the largest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "In what year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Aztecs", "Incas", "Romans", "Egyptians"],
                "answer": "Egyptians"
            }
        ]
    },
    "general": {
        "facts": [
            "Fingernails grow nearly 4 times faster than toenails.",
            "A 'jiffy' is an actual unit of time, equal to one-thousandth of a second.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Brain", "Heart", "Skin", "Liver"],
                "answer": "Skin"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "Korea"],
                "answer": "Japan"
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
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

def main():
    """
    Main function that displays the topic menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics:
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
