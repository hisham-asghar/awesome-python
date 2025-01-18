
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The sun is about 93 million miles away from the Earth.",
            "Diamonds are made of carbon that has been subjected to extreme heat and pressure."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "choices": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first successful computer virus?",
                "choices": ["Stuxnet", "WannaCry", "Melissa", "Morris"],
                "answer": "Morris"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz_questions": [
            {
                "question": "Who was the first president of the United States?",
                "choices": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "choices": ["The Flyer", "The Wright Flyer", "The Kitty Hawk", "The Airplane"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "What was the name of the ancient civilization that built the Machu Picchu ruins?",
                "choices": ["Aztec", "Inca", "Maya", "Olmec"],
                "answer": "Inca"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "A group of flamingos is called a flamboyance.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "choices": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "choices": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "choices": ["Titan", "Ganymede", "Callisto", "Io"],
                "answer": "Titan"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its choices from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question["question"], question["choices"], question["answer"]

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question, choices, answer = get_quiz_question(topic)
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.strip() == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")
    print(f"Your final score is {score} out of {num_questions}.")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYou selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
