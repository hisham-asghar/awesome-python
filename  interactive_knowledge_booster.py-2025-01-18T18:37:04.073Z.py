
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or predefined database.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of flamingos is called a flamboyance."
        ],
        "technology": [
            "The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.",
            "The first commercial computer, the UNIVAC I, was delivered to the US Census Bureau in 1951.",
            "The first text message was sent on December 3, 1992, by Neil Papworth, a 22-year-old test engineer."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "The King of Hearts is the only king without a mustache on a standard playing card."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, that topic is not available. Please choose from science, technology, history, or general knowledge."

def quiz(topic):
    """
    Provides a multiple-choice quiz to test the user's knowledge on the selected topic.
    """
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "Altair 8800"],
                "answer": 1
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Mesopotamia", "Aztec", "Egyptian", "Roman"],
                "answer": 2
            },
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which Renaissance artist is famous for painting the Mona Lisa?",
                "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Donatello"],
                "answer": 2
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            }
        ]
    }
    
    if topic in quizzes:
        quiz_data = random.choice(quizzes[topic])
        print(quiz_data["question"])
        for i, option in enumerate(quiz_data["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == quiz_data["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", quiz_data["options"][quiz_data["answer"]])
    else:
        print("Sorry, that topic is not available. Please choose from science, technology, history, or general knowledge.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general"]
    
    if 1 <= topic_choice <= 4:
        selected_topic = topics[topic_choice - 1]
        print("\nHere's a random fact or concept about", selected_topic.upper() + ":")
        print(get_random_fact(selected_topic))
        
        print("\nNow let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
