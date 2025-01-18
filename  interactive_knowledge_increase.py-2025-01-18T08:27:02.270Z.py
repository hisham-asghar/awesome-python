
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The human body contains around 60,000 miles of blood vessels.",
            "The first commercial jet flight took place in 1952 with the Boeing 707."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["23 million digits", "2 million digits", "1 million digits", "100,000 digits"],
                "answer": 0
            },
            {
                "question": "Approximately how many miles of blood vessels are in the human body?",
                "options": ["10,000 miles", "30,000 miles", "60,000 miles", "100,000 miles"],
                "answer": 2
            },
            {
                "question": "In what year did the first commercial jet flight take place?",
                "options": ["1940", "1952", "1962", "1972"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first commercial smartphone, the IBM Simon, was released in 1992.",
            "The world's first website was launched in 1991 and was about the World Wide Web project."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first computer virus?",
                "options": ["Creeper", "Melissa", "ILOVEYOU", "CIH"],
                "answer": 0
            },
            {
                "question": "In what year was the first commercial smartphone, the IBM Simon, released?",
                "options": ["1982", "1992", "2002", "2012"],
                "answer": 1
            },
            {
                "question": "In what year was the world's first website launched?",
                "options": ["1981", "1991", "2001", "2011"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight by the Wright brothers took place in 1903.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "Approximately how long is the Great Wall of China?",
                "options": ["5,000 miles", "10,000 miles", "13,000 miles", "20,000 miles"],
                "answer": 2
            },
            {
                "question": "In what year did the Wright brothers make the first successful powered flight?",
                "options": ["1893", "1903", "1913", "1923"],
                "answer": 1
            },
            {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["She lost them in an accident", "It was the fashion in Renaissance Florence to shave them off", "She was painted without eyebrows", "The artist forgot to paint them"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion caused by the heating of the iron.",
            "A group of porcupines is called a prickle.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), exceeding the limit of 2 mph (3 km/h)."
        ],
        "quiz_questions": [
            {
                "question": "How much taller can the Eiffel Tower get during the summer?",
                "options": ["5 cm", "10 cm", "15 cm", "20 cm"],
                "answer": 2
            },
            {
                "question": "What is a group of porcupines called?",
                "options": ["A quill", "A prickle", "A spike", "A quiver"],
                "answer": 1
            },
            {
                "question": "What was the speed limit and fine for the first person convicted of speeding in the UK?",
                "options": ["2 mph, 1 shilling fine", "5 mph, 5 shilling fine", "10 mph, 10 shilling fine", "15 mph, 15 shilling fine"],
                "answer": 0
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
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge increase script.
    """
    print("Welcome to the Interactive Knowledge Increase Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print("\nRandom fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
