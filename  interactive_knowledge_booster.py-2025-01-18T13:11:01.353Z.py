import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Diamonds are made of carbon that has been subjected to extreme heat and pressure.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Fe', 'Cu'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The world's first programmable computer was the ENIAC, which was completed in 1946.',
            'The first commercial jet airliner was the de Havilland Comet, which entered service in 1952.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the operating system developed by Apple Inc.?',
                'options': ['Windows', 'Linux', 'macOS', 'Android'],
                'answer': 'macOS'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Internet Explorer', 'Mozilla Firefox', 'Google Chrome', 'Mosaic'],
                'answer': 'Mosaic'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.',
            'The ancient Egyptian civilization lasted for over 3,000 years, from around 3100 BC to 30 BC.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian queen who was known for her beauty and power?',
                'options': ['Nefertiti', 'Cleopatra', 'Hatshepsut', 'Neferkare'],
                'answer': 'Cleopatra'
            },
            {
                'question': 'What was the name of the ancient Greek philosopher who is considered the father of Western philosophy?',
                'options': ['Plato', 'Aristotle', 'Socrates', 'Pythagoras'],
                'answer': 'Socrates'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe.',
            'The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and raises the structure.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean in the world?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the currency used in Japan?',
                'options': ['Yuan', 'Euro', 'Yen', 'Dollar'],
                'answer': 'Yen'
            },
            {
                'question': 'What is the name of the largest mammal in the world?',
                'options': ['Elephant', 'Whale', 'Hippopotamus', 'Giraffe'],
                'answer': 'Whale'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()