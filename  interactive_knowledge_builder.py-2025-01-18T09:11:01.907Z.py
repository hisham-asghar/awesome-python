
import random
import json
import requests

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first known computer bug was a real bug (a moth) trapped in a Harvard Mark II computer.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the name of the closest planet to the Sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": 2
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first commercially available personal computer was the Altair 8800, introduced in 1975.",
            "The word 'robot' was first used in the 1920 play 'R.U.R.' (Rossum's Universal Robots) by Karel Čapek."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Management Language", "Hyper Text Markup Lingo", "Hyper Text Management Lingo"],
                "answer": 0
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Internet Explorer", "Mosaic"],
                "answer": 3
            },
            {
                "question": "Which company developed the first commercial microprocessor?",
                "options": ["Intel", "Apple", "IBM", "Microsoft"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful manned space mission?",
                "options": ["Apollo 11", "Sputnik 1", "Vostok 1", "Mercury-Redstone 3"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The strongest muscle in the human body is the tongue.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet)."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the largest continent by land area?",
                "options": ["Africa", "Asia", "North America", "South America"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz(topic):
    """
    Retrieves a random quiz from the given topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Runs the interactive quiz for the user.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"You selected: {selected_topic.capitalize()}")
    print(get_random_fact(selected_topic))
    print()

    quiz = get_quiz(selected_topic)
    run_quiz(quiz)

if __name__ == "__main__":
    main()
