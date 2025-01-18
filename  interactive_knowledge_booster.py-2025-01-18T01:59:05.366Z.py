
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first commercial jet flight took place in 1952 with the de Havilland Comet."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is famous for developing the theory of relativity?",
                "options": ["Isaac Newton", "Charles Darwin", "Albert Einstein", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the first successful powered, controlled, and sustained airplane flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spruce Goose", "The Concorde"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "Z1", "Analytical Engine"],
                "answer": "ENIAC"
            },
            {
                "question": "Which company developed the first commercial web browser?",
                "options": ["Microsoft", "Apple", "Google", "Netscape"],
                "answer": "Netscape"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Magna Carta was signed in 1215, limiting the power of the English monarch.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The first moon landing was on July 20, 1969, with the Apollo 11 mission."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Mesopotamia", "Aztec", "Ancient Greece", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            },
            {
                "question": "What was the name of the first successful European expedition to circumnavigate the globe?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Jacques Cartier"],
                "answer": "Ferdinand Magellan"
            },
            {
                "question": "Which event is considered the start of the American Civil War?",
                "options": ["Battle of Gettysburg", "Emancipation Proclamation", "Assassination of Abraham Lincoln", "Battle of Fort Sumter"],
                "answer": "Battle of Fort Sumter"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "A 'jiffy' is an actual unit of time, equal to one-hundredth of a second."
        ],
        "quiz_questions": [
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
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if question["options"][int(user_answer)-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Invalid input. Please try again.")

def main():
    """
    Displays a menu, allows the user to select a topic, and provides a random fact and a quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
