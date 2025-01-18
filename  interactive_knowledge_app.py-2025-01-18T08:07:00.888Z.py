
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which organ in the human body produces insulin?",
                "options": ["Liver", "Pancreas", "Kidney", "Heart"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercially available personal computer was the Apple II, released in 1977.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": 3
            },
            {
                "question": "What is the name of the first successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Google Chrome"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": 2
            },
            {
                "question": "In which year did World War II end?",
                "options": ["1945", "1939", "1918", "1950"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The largest ocean on Earth is the Pacific Ocean.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and rises."
        ],
        "quiz": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the largest continent in the world?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    # Display the menu of topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic.capitalize()}")

    # Get the user's topic choice
    choice = int(input("Enter the number of the topic: "))
    selected_topic = list(topics.keys())[choice - 1]

    # Display a random fact from the selected topic
    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(random.choice(topics[selected_topic]["facts"]))

    # Run the quiz for the selected topic
    print(f"\nNow, let's test your knowledge with a quiz on {selected_topic.capitalize()}!")
    score = 0
    for question in topics[selected_topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer == question["answer"] + 1:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(topics[selected_topic]['quiz'])}")

if __name__ == "__main__":
    interactive_knowledge_app()
