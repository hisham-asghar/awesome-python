
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number as of 2022 has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Charles Darwin", "Albert Einstein", "Marie Curie"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called the 'Brain' virus.",
            "The first commercial internet service provider (ISP) was launched in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Manipulation Language", "Hypertext Markup Linking", "Hypertext Markup Loader"],
                "answer": "Hypertext Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mozilla Firefox", "Google Chrome", "Internet Explorer", "Netscape Navigator"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.",
            "The first successful powered flight took place in 1903 by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for their pyramids?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Egyptians"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1955", "1918"],
                "answer": "1945"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the largest continent in the world?",
                "options": ["Asia", "Africa", "Europe", "North America"],
                "answer": "Asia"
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
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
