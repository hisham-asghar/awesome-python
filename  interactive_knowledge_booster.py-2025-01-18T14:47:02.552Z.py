
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The fastest land animal is the cheetah, which can reach speeds of up to 75 mph.",
            "Diamonds are the hardest known natural material on Earth."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense.",
            "The first mobile phone call was made by Martin Cooper of Motorola in 1973."
        ],
        "quiz_questions": [
            {
                "question": "What does the acronym 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Central Power Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": "BlackBerry"
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
            "The ancient Egyptians were the first civilization to invent the 365-day calendar.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Mesopotamia", "Indus Valley", "Ancient Greece", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Venus", "Jupiter", "Mars", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
            }
        ]
    }
}

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    # Get the user's topic choice
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        # Display a random fact from the chosen topic
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(random.choice(topics[chosen_topic]["facts"]))
        
        # Run the quiz for the chosen topic
        print(f"\nNow, let's test your {chosen_topic.capitalize()} knowledge with a quiz!")
        quiz_questions = topics[chosen_topic]["quiz_questions"]
        score = 0
        for question in quiz_questions:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")
            user_answer = input("Enter the number of your answer: ")
            if question["options"][int(user_answer) - 1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"\nYour final score is {score} out of {len(quiz_questions)}.")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
