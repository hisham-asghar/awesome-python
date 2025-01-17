
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than Mount Everest."
        ],
        "quiz_questions": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "Which element is the most abundant in the Earth's crust?",
                "options": ["Oxygen", "Silicon", "Aluminum", "Iron"],
                "answer": "Oxygen"
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
            "The first computer mouse was invented in 1964 and had only one button.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first digital computer, ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the protocol used to transfer data over the internet?",
                "options": ["HTTP", "FTP", "SMTP", "TCP/IP"],
                "answer": "TCP/IP"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "China", "India"],
                "answer": "Mesopotamia"
            },
            {
                "question": "Which war lasted from 1939 to 1945?",
                "options": ["World War I", "World War II", "Vietnam War", "Korean War"],
                "answer": "World War II"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters.",
            "The longest river in the world is the Nile River, which flows for over 6,650 km.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe", "South America"],
                "answer": "Asia"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
                "answer": "Yen"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:\n{fact}")

def quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == "__main__":
    main()
