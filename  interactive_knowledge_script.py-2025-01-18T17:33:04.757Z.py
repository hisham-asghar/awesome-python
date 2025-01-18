Here is the raw Python code without any additional commentary:

import random
import requests
import json

topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The hottest planet in the Solar System is Venus, not Mercury."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the first satellite launched into Earth's orbit?",
                "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Vostok 1"],
                "answer": "Sputnik 1"
            },
            {
                "question": "What is the name of the theory that explains the evolution of species through natural selection?",
                "options": ["Heliocentric theory", "Big Bang theory", "Germ theory", "Theory of Evolution"],
                "answer": "Theory of Evolution"
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Electromagnetism", "Strong nuclear force", "Weak nuclear force"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": "macOS"
            },
            {
                "question": "What is the name of the company that developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": "BlackBerry"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Magna Carta was a charter agreed to by King John of England in 1215, which limited the power of the monarch."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the war that lasted from 1939 to 1945?",
                "options": ["World War I", "Civil War", "Vietnam War", "World War II"],
                "answer": "World War II"
            },
            {
                "question": "What is the name of the ancient civilization that built the Colosseum in Rome?",
                "options": ["Greek", "Egyptian", "Roman", "Mesopotamian"],
                "answer": "Roman"
            },
            {
                "question": "What is the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles get agitated and thus expand, causing the tower to grow in height.",
            "A group of flamingos is called a flamboyance."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"],
                "answer": "Nile River"
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yuan", "Euro", "Yen", "Dollar"],
                "answer": "Yen"
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if user_answer.isdigit() and int(user_answer) >= 1 and int(user_answer) <= len(question["options"]):
        if question["options"][int(user_answer)-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Invalid input. Please try again.")

def main():
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()