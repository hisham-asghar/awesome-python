
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or predefined data.
    """
    facts = {
        "science": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The human body contains enough iron to make a small nail.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first domain name ever registered was Symbolics.com on March 15, 1985.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and the structure grows.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, which was the speed limit at the time."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "Apples are more effective at waking you up in the morning than coffee.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, that topic is not available. Please select from science, technology, history, or general."

def quiz(topic):
    """
    Provides a multiple-choice quiz on the selected topic, using trivia data from a public API or predefined questions.
    """
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Neptune", "Uranus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ],
        "technology": [
            {
                "question": "What does 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Central Power Unit", "Computer Processing Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the first commercial web browser?",
                "options": ["Apple", "Microsoft", "Netscape", "Google"],
                "answer": "Netscape"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ],
        "history": [
            {
                "question": "In what year was the Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who is considered the father of modern computing?",
                "options": ["Charles Babbage", "Alan Turing", "Steve Jobs", "Bill Gates"],
                "answer": "Charles Babbage"
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Egyptians", "Romans"],
                "answer": "Egyptians"
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": "Giraffe"
            }
        ]
    }
    
    if topic in quiz_data:
        question = random.choice(quiz_data[topic])
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = input("Enter the number of your answer: ")
        if question["options"][int(user_answer)-1] == question["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    else:
        print("Sorry, that topic is not available. Please select from science, technology, history, or general.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = input("Enter the number of your choice: ")
    
    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Please try again.")
        return
    
    print("\nHere's a random fact or concept about", topic + ":")
    print(get_random_fact(topic))
    
    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
