
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains between 100-400 billion stars.",
            "Bees can fly higher than Mount Everest."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and used a ball to detect movement.",
            "The first commercial text message was sent on December 3, 1992.",
            "The world's first programmable computer was the ENIAC, which was completed in 1946."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "choices": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the first web browser, developed by Tim Berners-Lee?",
                "choices": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": "WorldWideWeb"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "choices": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Egyptians"
            },
            {
                "question": "What year did the American Civil War begin?",
                "choices": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "Who was the first president of the United States?",
                "choices": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general": {
        "facts": [
            "A group of flamingos is called a flamboyance.",
            "The world's largest desert is Antarctica, not the Sahara.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "choices": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "choices": ["African Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the rarest blood type?",
                "choices": ["O-", "A-", "B-", "AB-"],
                "answer": "AB-"
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

def get_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Runs the specified quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, choice in enumerate(quiz["choices"]):
        print(f"{i+1}. {choice}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz["choices"][int(user_answer) - 1] == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz["answer"])
    return score

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score is: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
