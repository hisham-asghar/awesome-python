import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The hottest planet in the solar system is Venus, not Mercury.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that pulls objects towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called 'Creeper', was created in 1971 as an experiment.',
            'The world's first website was launched on August 6, 1991, and is still online today.',
            'The first commercial text message was sent on December 3, 1992, by Neil Papworth.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Google Chrome', 'Mozilla Firefox'],
                'answer': 'Netscape Navigator'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896.'
        ],
        'quiz': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplane', 'The Monoplane'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.',
            'The king of hearts is the only king without a mustache on a standard playing card.'
        ],
        'quiz': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Europa'],
                'answer': 'Titan'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz = topics[topic]['quiz']
    question = random.choice(quiz)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
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