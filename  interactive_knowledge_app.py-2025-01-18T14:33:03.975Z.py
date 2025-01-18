
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first artificial satellite, Sputnik 1, was launched by the Soviet Union in 1957.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the name of the first artificial satellite launched into space?",
                "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Telstar 1"],
                "answer": "Sputnik 1"
            },
            {
                "question": "What is the main component of the human body that carries oxygen and nutrients to the cells?",
                "options": ["Nervous system", "Digestive system", "Cardiovascular system", "Respiratory system"],
                "answer": "Cardiovascular system"
            },
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["2^74,207,281 - 1", "2^77,232,917 - 1", "2^82,589,933 - 1", "2^23,000,000 - 1"],
                "answer": "2^82,589,933 - 1"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial email service was launched by CompuServe in 1979.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "Who invented the first computer mouse?",
                "options": ["Steve Jobs", "Bill Gates", "Douglas Engelbart", "Ada Lovelace"],
                "answer": "Douglas Engelbart"
            },
            {
                "question": "What year was the first commercial email service launched?",
                "options": ["1979", "1989", "1995", "2000"],
                "answer": "1979"
            },
            {
                "question": "Who invented the World Wide Web?",
                "options": ["Linus Torvalds", "Mark Zuckerberg", "Elon Musk", "Tim Berners-Lee"],
                "answer": "Tim Berners-Lee"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta was a charter agreed to by King John of England in 1215, which limited the power of the monarch.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "Which is the oldest and largest of the three pyramids in the Giza pyramid complex?",
                "options": ["The Pyramid of Khafre", "The Pyramid of Menkaure", "The Great Pyramid of Giza", "The Sphinx"],
                "answer": "The Great Pyramid of Giza"
            },
            {
                "question": "What year was the Magna Carta agreed to by King John of England?",
                "options": ["1215", "1066", "1492", "1776"],
                "answer": "1215"
            },
            {
                "question": "Who made the first successful powered flight in 1903?",
                "options": ["Leonardo da Vinci", "Wilbur and Orville Wright", "Charles Lindbergh", "Amelia Earhart"],
                "answer": "Wilbur and Orville Wright"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The highest point on Earth is Mount Everest, with a peak of 29,032 feet (8,849 meters) above sea level.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quiz": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Brain", "Skin"],
                "answer": "Skin"
            },
            {
                "question": "What is the highest point on Earth?",
                "options": ["K2", "Kilimanjaro", "Denali", "Mount Everest"],
                "answer": "Mount Everest"
            },
            {
                "question": "In what year were the first Olympic Games held?",
                "options": ["776 BC", "480 BC", "336 BC", "200 AD"],
                "answer": "776 BC"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    return random.choice(topics[topic]["quiz"])

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question["options"][user_answer - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

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
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
