
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Markup Lexicon", "Hyper Text Markup Lingo"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the programming language used to create Python?",
                "options": ["C", "Java", "C++", "C#"],
                "answer": "C"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Titanic, the largest ship afloat at the time, sank on its maiden voyage in 1912."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematical and astronomical knowledge?",
                "options": ["Egyptians", "Greeks", "Mayans", "Babylonians"],
                "answer": "Babylonians"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
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
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "Maya Angelou", "F. Scott Fitzgerald"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
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
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs the quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if question["options"][int(user_answer)-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Invalid input. Please try again.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"\nFact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
