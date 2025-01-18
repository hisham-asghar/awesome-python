
import random
import requests
import json

# Define the topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Diamonds are the hardest known natural material on Earth."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the primary function of the human heart?",
                "options": ["Pumping blood", "Breathing", "Digesting food", "Storing memories"],
                "answer": "Pumping blood"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called 'Brain'.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "High-Tech Multimedia Language", "Hyperlink Text Markup Language", "Hyper Text Machine Language"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "What is the primary function of a web browser?",
                "options": ["Sending emails", "Playing music", "Browsing the internet", "Editing documents"],
                "answer": "Browsing the internet"
            },
            {
                "question": "Which company developed the first commercially successful personal computer?",
                "options": ["Apple", "Microsoft", "IBM", "Google"],
                "answer": "IBM"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560-2540 BC, making them over 4,500 years old.",
            "The Roman Empire lasted for over 1,000 years, from 27 BC to 476 AD."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematical and astronomical knowledge?",
                "options": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": "Mayans"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "In which year did World War II end?",
                "options": ["1939", "1945", "1950", "1955"],
                "answer": "1945"
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (19.7 feet) tall.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The largest organ in the human body is the skin."
        ],
        "quizzes": [
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Everest"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz(topic):
    """
    Retrieves a random quiz from the selected topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's answer.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    return user_answer.strip()

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nLet's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        user_answer = run_quiz(quiz)
        
        if user_answer == quiz["answer"]:
            print("Correct! You're a knowledge master.")
        else:
            print(f"Oops, the correct answer is: {quiz['answer']}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
