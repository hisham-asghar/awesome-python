
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Diamonds are the hardest known natural material on Earth."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
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
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first successful commercial web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Safari"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": "Mesopotamia"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did the Berlin Wall fall?",
                "options": ["1989", "1991", "1995", "2001"],
                "answer": "1989"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion caused by the heating of the iron.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote the novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "Maya Angelou", "F. Scott Fitzgerald"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["African Elephant", "Blue Whale", "Sperm Whale", "Hippopotamus"],
                "answer": "Blue Whale"
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
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")

    topic_choice = input("Enter the number of the topic (1-4): ")

    topic_map = {
        "1": "science",
        "2": "technology",
        "3": "history",
        "4": "general"
    }

    if topic_choice in topic_map:
        selected_topic = topic_map[topic_choice]
        print(f"\nYou selected: {selected_topic.capitalize()}")

        print("\nHere's a random fact about the topic:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz_question = get_quiz_question(selected_topic)
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Enter the number of your answer: ")
        if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", quiz_question["answer"])
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
