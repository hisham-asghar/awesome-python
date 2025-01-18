
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The first confirmed meteorite impact in recorded history was in 1490 in the village of Ensisheim, France.",
            "The Mariana Trench is the deepest part of the world's oceans, reaching a maximum depth of approximately 10,994 meters (36,070 feet)."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The world's first programmable computer, the ENIAC, was completed in 1946 and weighed over 30 tons."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hyper Transmission Markup Language", "Hypertext Machine Language", "Hypertext Modeling Language"],
                "answer": "Hypertext Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
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
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Mayans", "Egyptians"],
                "answer": "Egyptians"
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Vasco da Gama Expedition", "The Leif Erikson Voyage"],
                "answer": "The Magellan Expedition"
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "The Battle of Stalingrad", "The Fall of Berlin", "The Atomic Bombings of Hiroshima and Nagasaki"],
                "answer": "The Fall of Berlin"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and the tower grows in height.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), which was the speed limit of the time."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "Which famous physicist developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    return random.choice(topics[topic]["quizzes"])

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
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
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic.capitalize()}")
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic not in topics:
            print("Invalid topic. Please try again.")
            continue

        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))

        print("\nNow let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")

        continue_app = input("\nDo you want to try another topic? (y/n) ").lower()
        if continue_app != "y":
            print("Thank you for using the Interactive Knowledge App!")
            break

if __name__ == "__main__":
    main()
