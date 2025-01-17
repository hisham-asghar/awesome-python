
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the chosen topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first product to have a barcode was Wrigley's gum.",
            "A group of flamingos is called a flamboyance."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 and cost $15,000.",
            "The first digital camera was developed by Kodak in 1975.",
            "The first text message was sent in 1992 and said 'Merry Christmas'."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first recorded use of the word 'OK' was in 1839.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provide a multiple-choice quiz on the chosen topic."""
    questions = {
        "science": [
            {"question": "What is the chemical symbol for gold?", "choices": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
            {"question": "Which planet in our solar system has the most moons?", "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": 0},
            {"question": "What is the process of converting water into water vapor called?", "choices": ["Evaporation", "Condensation", "Precipitation", "Transpiration"], "answer": 0}
        ],
        "technology": [
            {"question": "What is the name of the first commercially available personal computer?", "choices": ["Apple I", "IBM PC", "Commodore 64", "Altair 8800"], "answer": 3},
            {"question": "Which company developed the first graphical user interface (GUI)?", "choices": ["Microsoft", "Apple", "Xerox", "IBM"], "answer": 2},
            {"question": "What is the name of the programming language created by Guido van Rossum?", "choices": ["Java", "C++", "Python", "Ruby"], "answer": 2}
        ],
        "history": [
            {"question": "In what year did the American Civil War begin?", "choices": ["1861", "1865", "1775", "1914"], "answer": 0},
            {"question": "Who was the first president of the United States?", "choices": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"], "answer": 2},
            {"question": "Which ancient civilization is known for building the Pyramids?", "choices": ["Mesopotamia", "Indus Valley", "Egypt", "Aztec"], "answer": 2}
        ],
        "general": [
            {"question": "What is the largest organ in the human body?", "choices": ["Heart", "Liver", "Skin", "Brain"], "answer": 2},
            {"question": "What is the largest ocean on Earth?", "choices": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 0},
            {"question": "Which country is known as the 'Land of the Rising Sun'?", "choices": ["China", "Japan", "India", "South Korea"], "answer": 1}
        ]
    }
    question = random.choice(questions[topic])
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["choices"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Choose a topic:")
    topics = ["Science", "Technology", "History", "General Knowledge"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    topic_choice = int(input("Enter your choice (1-4): "))
    topic = topics[topic_choice - 1].lower()
    
    print("\nHere's a random fact or concept about", topics[topic_choice - 1] + ":")
    print(get_random_fact(topic))
    
    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
