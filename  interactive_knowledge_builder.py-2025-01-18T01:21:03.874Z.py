
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
        ],
        "quiz": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Modeling Language", "Hypertext Management Language", "Hypertext Manipulation Language"],
                "answer": "Hypertext Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first known computer programmer was a woman named Ada Lovelace, who lived in the 19th century."
        ],
        "quiz": [
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Flyer", "The Biplane", "The Glider", "The Aeroplane"],
                "answer": "The Flyer"
            },
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Aztec", "Egyptian"],
                "answer": "Egyptian"
            },
            {
                "question": "What was the name of the first successful moon landing mission?",
                "options": ["Apollo 11", "Sputnik 1", "Gemini 3", "Skylab 1"],
                "answer": "Apollo 11"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "A group of flamingos is called a flamboyance.",
            "The world's largest desert is Antarctica, not the Sahara.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
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
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
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
