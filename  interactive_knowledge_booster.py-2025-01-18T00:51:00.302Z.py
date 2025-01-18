
import random
import requests
import json

# Define topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2023 has over 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
                "answer": 0
            },
            {
                "question": "Which scientist is famous for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The world's first programmable computer was the ENIAC, completed in 1946."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Greece", "Ancient Egypt", "Ancient China"],
                "answer": 1
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Attack on Pearl Harbor", "Fall of the Berlin Wall"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Neptune"],
                "answer": 1
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))

        print("\nTime for a quiz!")
        quiz_question = get_quiz_question(chosen_topic)
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == quiz_question["answer"]:
            print("Correct! You're a knowledge master!")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print(f"Sorry, '{chosen_topic.capitalize()}' is not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
