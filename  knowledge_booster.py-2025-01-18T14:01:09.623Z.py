Here is the raw Python code extracted from the JSON:

```python
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been around for over 400 million years, predating the dinosaurs."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The world's first website was launched on August 6, 1991, and was about the World Wide Web project itself.",
            "The first commercial text message was sent on December 3, 1992, by Neil Papworth."
        ],
        "quizzes": [
            {
                "question": "What is the name of the operating system developed by Apple?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": "macOS"
            },
            {
                "question": "Which company is known for creating the popular search engine Google?",
                "options": ["Apple", "Microsoft", "Amazon", "Alphabet"],
                "answer": "Alphabet"
            },
            {
                "question": "What is the name of the programming language that is widely used for web development?",
                "options": ["Java", "C++", "Python", "PHP"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first computer programmer was a woman named Ada Lovelace, who lived in the 19th century."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Greek", "Roman", "Egyptian", "Aztec"],
                "answer": "Egyptian"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1914", "1918"],
                "answer": "1945"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general": {
        "facts": [
            "The strongest muscle in the human body is the tongue.",
            "The largest organ in the human body is the skin.",
            "The shortest sentence in the English language is 'I am.'"
        ],
        "quizzes": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Green", "Purple"],
                "answer": "Purple"
            }
        ]
    }
}

def run_knowledge_app():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You selected the '{selected_topic.capitalize()}' topic.")
        print("Here's a random fact:")
        print(random.choice(topics[selected_topic]["facts"]))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz_question = random.choice(topics[selected_topic]["quizzes"])
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of your answer: ")
        if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    run_knowledge_app()
