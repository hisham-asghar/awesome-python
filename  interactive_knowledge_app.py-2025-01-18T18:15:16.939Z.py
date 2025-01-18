
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is famous for the theory of relativity?",
                "options": ["Isaac Newton", "Charles Darwin", "Albert Einstein", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Venus"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964.",
            "The term 'bug' in computer programming was coined in 1947.",
            "The first commercial computer, the UNIVAC I, was delivered in 1951."
        ],
        "quiz_questions": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Management Language", "Hyper Text Markup Learner", "Hyper Text Markup Launcher"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Internet Explorer", "Mozilla Firefox", "Google Chrome", "Netscape Navigator"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": "Ancient Greece"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYou selected: {selected_topic.capitalize()}")
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(random.choice(topics[selected_topic]["facts"]))

        print("\nTime for a quiz! Answer the following multiple-choice questions:")
        score = 0
        for question in topics[selected_topic]["quiz_questions"]:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")
            user_answer = input("Enter your answer (1-4): ")
            if question["options"][int(user_answer) - 1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", question["answer"])
        print(f"\nYour final score is: {score}/{len(topics[selected_topic]['quiz_questions'])}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    interactive_knowledge_app()
