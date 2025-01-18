
import random
import requests
import json

# Define topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first commercial color television was introduced in 1953."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the closest planet to the Sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": "Mercury"
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company is known for creating the Android operating system?",
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
            "The first successful powered flight was made by the Wright brothers in 1903.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Incas", "Mayans", "Aztecs", "Egyptians"],
                "answer": "Egyptians"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1918", "1955"],
                "answer": "1945"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known snowflake was 15 inches wide and 8 inches thick.",
            "The first commercial airline flight took place on January 1, 1914.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands and rises."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "answer": "Blue Whale"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quizzes = topics[topic]["quizzes"]
    return random.choice(quizzes)

def run_quiz(quiz):
    """
    Runs the specified quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for option in quiz["options"]:
        print(f"{option}")
    user_answer = input("Enter your answer: ").upper()
    if user_answer == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz["answer"])
    return score

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Select a topic to get started:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic not in topics:
        print("Invalid topic. Please try again.")
        return
    
    print(f"You selected: {chosen_topic.capitalize()}")
    print(get_random_fact(chosen_topic))
    
    quiz = get_random_quiz(chosen_topic)
    score = run_quiz(quiz)
    print(f"Your score: {score} out of 1")

if __name__ == "__main__":
    main()
