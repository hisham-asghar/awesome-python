
import random
import json
import requests

# Define topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Earth's core is as hot as the surface of the Sun."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Friction", "Electromagnetism", "Centrifugal force"],
                "answer": 0
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The world's first programmable computer, the ENIAC, was completed in 1946."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language developed by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the first commercially successful smartphone, the iPhone?",
                "options": ["Samsung", "Google", "Apple", "Microsoft"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical connection?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular data"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1775", "1914"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient civilization located in present-day Mexico and Central America?",
                "options": ["Inca", "Maya", "Aztec", "Olmec"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion causing the iron to expand.",
            "A 'jiffy' is an actual unit of time, equal to one-thousandth of a second."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 0
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["African Elephant", "Blue Whale", "Sperm Whale", "Humpback Whale"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def main():
    """
    Interactively engages the user in learning about different topics.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    score = 0
    for _ in range(3):
        question, options, answer = get_quiz_question(selected_topic)
        print(f"\n{question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", options[answer])

    print(f"\nYour final score is {score} out of 3.")

if __name__ == "__main__":
    main()
