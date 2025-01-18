import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "technology": [
            "The first commercial computer, UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The 'Qwerty' keyboard layout was designed to slow down typists to prevent jamming on early typewriters.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first wireless microphone was used by Elvis Presley in 1956.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, I don't have any facts for that topic."

def get_quiz_question(topic):
    """
    Fetches a multiple-choice quiz question and its answers from a public API or predefined database for the given topic.
    """
    quiz_questions = {
        "science": {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Cu", "Fe"],
            "answer": 0
        },
        "technology": {
            "question": "What is the name of the first commercially available personal computer?",
            "options": ["Apple II", "Commodore 64", "IBM PC", "Altair 8800"],
            "answer": 3
        },
        "history": {
            "question": "In what year did the United States declare independence?",
            "options": ["1776", "1783", "1787", "1791"],
            "answer": 0
        },
        "general": {
            "question": "What is the largest planet in our solar system?",
            "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
            "answer": 1
        }
    }
    
    if topic in quiz_questions:
        return quiz_questions[topic]
    else:
        return None

def main():
    """
    The main function that runs the interactive knowledge-boosting script.
    """
    print("Welcome to the Interactive Knowledge Booster!\n")
    
    while True:
        print("Please select a topic:")
        print("1. Science")
        print("2. Technology")
        print("3. History")
        print("4. General Knowledge")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            topic = "science"
        elif choice == "2":
            topic = "technology"
        elif choice == "3":
            topic = "history"
        elif choice == "4":
            topic = "general"
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print("\nRandom fact about", topic, ":", get_random_fact(topic))
        
        quiz_data = get_quiz_question(topic)
        if quiz_data:
            print("\nTest your knowledge with this multiple-choice question:")
            print(quiz_data["question"])
            for i, option in enumerate(quiz_data["options"]):
                print(f"{i+1}. {option}")
            
            user_answer = input("Enter your answer (1-4): ")
            if int(user_answer) == quiz_data["answer"]:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is", quiz_data["options"][quiz_data["answer"]])
        else:
            print("Sorry, I don't have a quiz question for that topic.")
        
        print("\n")

if __name__ == "__main__":
    main()