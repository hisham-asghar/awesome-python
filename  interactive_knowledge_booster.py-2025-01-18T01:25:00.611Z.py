
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number has over 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest known prime number?",
                "options": ["Mersenne Prime", "Fermat Prime", "Euclid Prime", "Lehmer Prime"],
                "answer": 0
            },
            {
                "question": "Which of these is not a fundamental force in physics?",
                "options": ["Gravity", "Electromagnetism", "Strong Nuclear Force", "Weak Interaction"],
                "answer": 3
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first website was launched on August 6, 1991."
        ],
        "quiz": [
            {
                "question": "What was the name of the first commercial computer?",
                "options": ["ENIAC", "UNIVAC I", "IBM 701", "MARK I"],
                "answer": 1
            },
            {
                "question": "Who is credited with inventing the first computer mouse?",
                "options": ["Steve Jobs", "Bill Gates", "Douglas Engelbart", "Ada Lovelace"],
                "answer": 2
            },
            {
                "question": "In what year was the first website launched?",
                "options": ["1989", "1991", "1993", "1995"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization built the Great Pyramid of Giza?",
                "options": ["Mesopotamians", "Egyptians", "Mayans", "Incas"],
                "answer": 1
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Vincent van Gogh"],
                "answer": 2
            },
            {
                "question": "Who made the first successful powered flight?",
                "options": ["Wilbur and Orville Wright", "Charles Lindbergh", "Amelia Earhart", "Neil Armstrong"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, when thermal expansion causes the iron to expand.",
            "A group of flamingos is called a flamboyance.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "What is the name of a group of flamingos?",
                "options": ["Flock", "Herd", "Flamboyance", "Gaggle"],
                "answer": 2
            },
            {
                "question": "What was the first product to have a barcode?",
                "options": ["Coca-Cola", "Heinz Ketchup", "Wrigley's Gum", "Tide Detergent"],
                "answer": 2
            },
            {
                "question": "How much taller can the Eiffel Tower be during the summer?",
                "options": ["5 cm", "10 cm", "15 cm", "20 cm"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print(f"Here's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
