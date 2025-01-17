
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The hottest planet in the Solar System is Venus, not Mercury."
        ],
        "quiz_questions": [
            {
                "question": "Which of these is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that pulls objects towards each other?",
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet of space.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The internet was originally called ARPANET, which stood for Advanced Research Projects Agency Network."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the first widely used web browser?",
                "options": ["Microsoft", "Apple", "Google", "Netscape"],
                "answer": 3
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Printer", "Scanner"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Aztec", "Inca", "Egyptian", "Roman"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Spirit of St. Louis", "The Kitty Hawk", "The Bleriot XI"],
                "answer": 0
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The invasion of Poland", "The bombing of Pearl Harbor", "The dropping of the atomic bomb"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": 0
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if int(user_answer) - 1 == quiz_question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your topic choice: ").lower()
        if user_topic in topics:
            print(f"\nRandom fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            print("\nTime for a quiz!")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
