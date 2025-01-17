
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and raises the structure.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'.",
            "The first commercial smartphone, the IBM Simon, was introduced in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What does 'RAM' stand for?",
                "options": ["Random Access Memory", "Rapid Access Memory", "Read Access Memory", "Robust Access Memory"],
                "answer": "Random Access Memory"
            },
            {
                "question": "Which company developed the first graphical user interface (GUI) for personal computers?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
                "answer": "Xerox"
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
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "In what year did World War I begin?",
                "options": ["1914", "1939", "1941", "1945"],
                "answer": "1914"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Airplane", "The Glider"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and raises the structure.",
            "A single cloud can weigh more than 1 million pounds.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
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

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_interactive_quiz():
    """
    Runs an interactive quiz for the user, allowing them to select a topic and answer multiple-choice questions.
    """
    print("Welcome to the Interactive Knowledge Quiz!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nYour selected topic is: {selected_topic.capitalize()}")
    print(get_random_fact(selected_topic))
    print("\nLet's test your knowledge with a quiz!")

    score = 0
    for _ in range(3):
        quiz_question = get_quiz_question(selected_topic)
        print(f"\n{quiz_question['question']}")
        for i, option in enumerate(quiz_question['options']):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of your answer: ")
        if user_answer.isdigit() and int(user_answer) > 0 and int(user_answer) <= len(quiz_question['options']):
            if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", quiz_question['answer'])
        else:
            print("Invalid input. Please try again.")

    print(f"\nYour final score is: {score}/3")

if __name__ == "__main__":
    run_interactive_quiz()
