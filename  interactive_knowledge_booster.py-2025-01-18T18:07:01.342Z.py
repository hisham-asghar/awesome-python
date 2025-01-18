
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first programmable computer was created in 1936 by Alan Turing.",
            "The largest known prime number as of 2022 has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first smartphone was the IBM Simon, released in 1992.",
            "The world's first website was launched on August 6, 1991, by Tim Berners-Lee."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first successful digital computer?",
                "options": ["ENIAC", "UNIVAC I", "IBM 701", "Apple I"],
                "answer": "ENIAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization built the Colosseum in Rome?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Romans"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1941", "1950"],
                "answer": "1945"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.",
            "The Mona Lisa, painted by Leonardo da Vinci, is on permanent display at the Louvre Museum in Paris."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
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
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize(), ":")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
