
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the selected topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The hottest planet in the solar system is Venus, not Mercury."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The term 'computer bug' was coined after a moth was found stuck in a Harvard Mark II computer.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Pyramids of Giza are the only remaining Wonder of the Ancient World.",
            "The first successful powered flight by the Wright brothers lasted 12 seconds."
        ],
        "general": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury."
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    """Fetch a multiple-choice quiz question from the selected topic."""
    quiz_questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first commercial computer?",
                "options": ["ENIAC", "UNIVAC I", "IBM 701", "Apple I"],
                "answer": 1
            },
            {
                "question": "Which company developed the first graphical user interface (GUI)?",
                "options": ["Microsoft", "Apple", "Xerox", "IBM"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "In what year did World War I begin?",
                "options": ["1914", "1939", "1945", "1918"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Glider"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest known prime number as of 2022?",
                "options": ["10 million digits", "20 million digits", "23 million digits", "30 million digits"],
                "answer": 2
            },
            {
                "question": "How many miles of blood vessels are in the human body?",
                "options": ["30,000 miles", "45,000 miles", "60,000 miles", "75,000 miles"],
                "answer": 2
            },
            {
                "question": "Which planet in the solar system is the hottest?",
                "options": ["Mercury", "Venus", "Earth", "Mars"],
                "answer": 1
            }
        ]
    }
    return random.choice(quiz_questions[topic])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Select a topic to get started:")
    topics = ["Science", "Technology", "History", "General"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    topic_choice = int(input("Enter the number of your chosen topic: "))
    topic = topics[topic_choice - 1].lower()

    print(f"\nHere's a random fact about {topics[topic_choice - 1]}:")
    print(get_random_fact(topic))

    quiz_question = get_quiz_question(topic)
    print(f"\nTest your knowledge with this multiple-choice question:")
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == quiz_question["answer"] + 1:
        print("Correct!")
    else:
        print("Incorrect. Better luck next time!")

if __name__ == "__main__":
    main()
