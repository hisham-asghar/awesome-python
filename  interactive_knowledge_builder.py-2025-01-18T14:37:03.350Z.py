import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Honey is the only food that does not spoil.'
        ],
        'quiz_questions': [
            {
                'question': 'Which of these is the smallest particle of an element?',
                'options': ['Atom', 'Molecule', 'Proton', 'Electron'],
                'answer': 'Atom'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that holds the planets in orbit around the Sun?',
                'options': ['Gravity', 'Friction', 'Centrifugal force', 'Electromagnetic force'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and cost $15 to build.',
            'The first text message was sent in 1992 and said "Merry Christmas".',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first web browser, created by Tim Berners-Lee?',
                'options': ['Google Chrome', 'Mozilla Firefox', 'Internet Explorer', 'Mosaic'],
                'answer': 'Mosaic'
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals for transmission over telephone lines?',
                'options': ['Modem', 'Router', 'Printer', 'Scanner'],
                'answer': 'Modem'
            }
        ]
    },
    'history': {
        'facts': [
            'The first known written language was Sumerian cuneiform, developed around 3500 BC.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560–2540 BC.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first dynasty that ruled ancient Egypt?',
                'options': ['Ptolemaic Dynasty', 'Abbasid Dynasty', 'Umayyad Dynasty', 'Archaic Period'],
                'answer': 'Archaic Period'
            },
            {
                'question': 'What was the name of the ancient Greek philosopher who developed the concept of the atom?',
                'options': ['Plato', 'Aristotle', 'Socrates', 'Democritus'],
                'answer': 'Democritus'
            },
            {
                'question': 'What was the name of the first successful powered flight, carried out by the Wright brothers in 1903?',
                'options': ['Glider', 'Biplane', 'Monoplane', 'Flyer'],
                'answer': 'Flyer'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest desert in the world is the Sahara, covering an area of 3.6 million square miles.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the currency used in Japan?',
                'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
                'answer': 'Yen'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()