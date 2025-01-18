
import random
import requests
import json

# Define the topics and their respective facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Newton", "Einstein", "Galileo", "Darwin"],
                "answer": "Einstein"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Io", "Europa", "Ganymede"],
                "answer": "Titan"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The internet was originally called ARPANET, which was developed in the 1960s by the U.S. Department of Defense."
        ],
        "quizzes": [
            {
                "question": "What is the name of the operating system developed by Apple?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": "macOS"
            },
            {
                "question": "Which company is known for creating the popular search engine Google?",
                "options": ["Apple", "Microsoft", "Amazon", "Alphabet"],
                "answer": "Alphabet"
            },
            {
                "question": "What is the name of the programming language that is commonly used for web development?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": "JavaScript"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight by the Wright brothers took place in 1903.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for their advanced mathematics and astronomy?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Mayans"
            },
            {
                "question": "What was the name of the first successful American space mission?",
                "options": ["Apollo 11", "Sputnik 1", "Mercury-Redstone 3", "Gemini 3"],
                "answer": "Mercury-Redstone 3"
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["D-Day", "Pearl Harbor", "Hiroshima bombing", "VE Day"],
                "answer": "Hiroshima bombing"
            }
        ]
    },
    "general": {
        "facts": [
            "A group of flamingos is called a flamboyance.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet)."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": "Japan"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "North America", "Europe"],
                "answer": "Asia"
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    
    # Display the topic menu
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        # Display a random fact from the selected topic
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(random.choice(topics[selected_topic]["facts"]))
        
        # Run a quiz for the selected topic
        print(f"\nNow, let's test your knowledge with a {selected_topic.capitalize()} quiz!")
        quiz_questions = topics[selected_topic]["quizzes"]
        score = 0
        for quiz_question in quiz_questions:
            print(quiz_question["question"])
            for option in quiz_question["options"]:
                print(f"- {option}")
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == quiz_question["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"\nYour final score is {score} out of {len(quiz_questions)}.")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    interactive_knowledge_app()
