
import random
import json
import requests

# Define a dictionary of topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the first satellite launched into orbit?",
                "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Telstar 1"],
                "answer": "Sputnik 1"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial jet airliner, the de Havilland Comet, was introduced in 1952.",
            "The World Wide Web was created by Tim Berners-Lee in 1989."
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
                "question": "What is the name of the first electronic computer, developed in the 1940s?",
                "options": ["ENIAC", "UNIVAC", "IBM 701", "MARK I"],
                "answer": "ENIAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomical knowledge?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": "Ancient Greece"
            },
            {
                "question": "What was the name of the first successful European expedition to circumnavigate the globe?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "James Cook"],
                "answer": "Ferdinand Magellan"
            },
            {
                "question": "Which event is considered the starting point of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Sinking of the Lusitania", "German invasion of Poland", "Battle of the Somme"],
                "answer": "Assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, exceeding the 2 mph speed limit."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who is the author of the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "Maya Angelou"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    return random.choice(topics[topic]["quiz_questions"])

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    """
    Main function that runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"You selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
