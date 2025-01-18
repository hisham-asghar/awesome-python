
import random
import requests
import json

def get_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or predefined database.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first confirmed meteorite impact in the United States occurred in 1807 in Weston, Connecticut.",
            "The hottest planet in the Solar System is Venus, not Mercury."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964 and had only one button.",
            "The term 'algorithm' is derived from the name of the 9th-century mathematician, Al-Khwarizmi.",
            "The first programmable computer, the ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first emperor of the Roman Empire was Augustus, who ruled from 27 BC to 14 AD."
        ],
        "general": [
            "The strongest muscle in the human body is the tongue.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).",
            "The largest known prime number as of 2022 has 23 million digits."
        ]
    }

    return random.choice(facts[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz based on the selected topic, using real-time educational content or trivia.
    """
    questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Google Chrome"],
                "answer": 1
            },
            {
                "question": "Which company developed the first personal computer, the MITS Altair 8800?",
                "options": ["Apple", "Microsoft", "IBM", "MITS"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1775", "1914"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Inca", "Ancient Egypt"],
                "answer": 3
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which of these animals is not a mammal?",
                "options": ["Dolphin", "Penguin", "Bat", "Whale"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }

    question = random.choice(questions[topic])
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter your choice (1-4): "))

    topics = ["science", "technology", "history", "general"]
    chosen_topic = topics[topic_choice - 1]

    print("\nHere's a random fact or concept about", chosen_topic.upper() + ":")
    print(get_fact(chosen_topic))

    print("\nNow let's test your knowledge with a quiz!")
    quiz(chosen_topic)

    print("\nThank you for using the Interactive Knowledge Booster!")

if __name__ == "__main__":
    main()
