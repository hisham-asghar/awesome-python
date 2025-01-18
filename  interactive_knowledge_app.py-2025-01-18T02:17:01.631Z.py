import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'The hottest planet in the Solar System is Venus, not Mercury.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the unit used to measure the strength of an earthquake?',
                'options': ['Richter scale', 'Celsius scale', 'Fahrenheit scale', 'Kelvin scale'],
                'answer': 'Richter scale'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The first digital computer, the ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the technology used to store and transmit data in a decentralized manner?',
                'options': ['Blockchain', 'Cloud computing', 'Artificial Intelligence', 'Virtual Reality'],
                'answer': 'Blockchain'
            },
            {
                'question': 'What is the name of the device used to input data into a computer?',
                'options': ['Keyboard', 'Monitor', 'Printer', 'Mouse'],
                'answer': 'Mouse'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers in 1903?',
                'options': ['The Flyer', 'The Kitty Hawk', 'The Biplane', 'The Glider'],
                'answer': 'The Flyer'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['Mesopotamian', 'Sumerian', 'Phoenician', 'Egyptian'],
                'answer': 'Egyptian'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 18 feet tall.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the currency used in the United States?',
                'options': ['Euro', 'Pound', 'Yen', 'Dollar'],
                'answer': 'Dollar'
            },
            {
                'question': 'What is the name of the largest continent on Earth?',
                'options': ['Africa', 'Asia', 'Europe', 'North America'],
                'answer': 'Asia'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    question = random.choice(topics[topic]['quiz_questions'])
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if question['options'][user_answer-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

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
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()