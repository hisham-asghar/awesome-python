
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "Bananas are slightly radioactive.",
            "Neutron stars are the collapsed cores of massive stars, with a density greater than that of an atomic nucleus."
        ],
        "quiz": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce energy", "To regulate body temperature"],
                "answer": 0
            },
            {
                "question": "Which of these is NOT a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 3
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first text message was sent in 1992 and said 'Merry Christmas'.",
            "The world's first website was launched in 1991 and was about the World Wide Web project itself."
        ],
        "quiz": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Multiple Language", "Hyper Text Markup Leap", "Hyper Textual Markup Language"],
                "answer": 0
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the purpose of a firewall in computer security?",
                "options": ["To protect against unauthorized access", "To improve internet speed", "To encrypt data", "To back up files"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first book ever written was the 'Epic of Gilgamesh', dating back to 2100 BC.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Glider", "The Kite", "The Biplane"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The strongest muscle in the human body is the tongue.",
            "Apples are more effective at waking you up in the morning than coffee.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Fetches a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
