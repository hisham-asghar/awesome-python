
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Honey is the only food that does not spoil."
        ],
        "quiz_questions": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce insulin"],
                "answer": 0
            },
            {
                "question": "What is the name of the closest star to the Earth?",
                "options": ["Sirius", "Proxima Centauri", "Andromeda"],
                "answer": 1
            },
            {
                "question": "Which gas makes up the majority of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the first commercially successful graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson"],
                "answer": 1
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1955"],
                "answer": 0
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Ancient Egypt"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest river in the world by volume?",
                "options": ["Amazon", "Nile", "Mississippi"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Fetches a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Fetches a random quiz question from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-3): ")) - 1
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Exiting.")
        return

    print(f"You selected: {selected_topic.capitalize()}")
    print(get_random_fact(selected_topic))
    print()
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
