
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the selected topic using a public API or predefined database."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and occupied 1,800 square feet.",
            "The first smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was developed by Kodak in 1975 and could capture 0.01 megapixel images."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, we don't have any facts for that topic. Please choose from science, technology, history, or general."

def quiz(topic):
    """Provide a multiple-choice quiz for the selected topic."""
    quizzes = {
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
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Friction", "Gravity", "Magnetism", "Electricity"],
                "answer": 1
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "ARPANET", "FORTRAN"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
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
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1941", "1947"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1848"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
    
    if topic in quizzes:
        quiz_data = random.choice(quizzes[topic])
        print(quiz_data["question"])
        for i, option in enumerate(quiz_data["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer - 1 == quiz_data["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", quiz_data["options"][quiz_data["answer"]])
    else:
        print("Sorry, we don't have a quiz for that topic. Please choose from science, technology, history, or general.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = int(input("Enter the number of your choice: "))
    
    topics = ["science", "technology", "history", "general"]
    
    if 1 <= topic_choice <= 4:
        selected_topic = topics[topic_choice - 1]
        print(f"\nRandom fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
