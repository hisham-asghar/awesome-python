
import random
import json
import requests

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "Diamonds are formed from carbon under extremely high temperature and pressure conditions."
        ],
        "quizzes": [
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": 0
            },
            {
                "question": "What is the name of the first satellite launched into Earth's orbit?",
                "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Telstar 1"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The term 'bug' was first used in computing when a moth was found trapped in a relay of the Harvard Mark II computer in 1947.",
            "The world's first text message was sent on December 3, 1992, and it read 'Merry Christmas'."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "TRS-80"],
                "answer": 1
            },
            {
                "question": "What is the name of the company that developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC and are the oldest and largest of the three main pyramids.",
            "The first Olympic Games were held in Olympia, Greece, in 776 BC."
        ],
        "quizzes": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient civilization that built the Colosseum in Rome?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": 1
            },
            {
                "question": "What was the name of the event that marked the end of World War II in Europe?",
                "options": ["D-Day", "V-E Day", "Pearl Harbor", "Hiroshima"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, the speed limit at the time was 2 mph."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the tallest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz(topic):
    """
    Returns a random quiz from the selected topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    The main function that runs the interactive knowledge program.
    """
    print("Welcome to the Interactive Knowledge Program!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        quiz = get_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"\nYour score: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
