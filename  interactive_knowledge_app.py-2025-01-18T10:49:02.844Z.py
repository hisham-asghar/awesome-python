import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The first programmable computer was created in the 1830s by Charles Babbage.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for formulating the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 1
            },
            {
                'question': 'What is the name of the force that holds the planets in their orbits around the Sun?',
                'options': ['Gravity', 'Electromagnetic force', 'Strong nuclear force', 'Weak nuclear force'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The internet was originally called ARPANET and was created by the US Department of Defense in 1969.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language that was designed by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which company developed the first commercially successful graphical user interface (GUI)?',
                'options': ['Apple', 'Microsoft', 'IBM', 'Xerox'],
                'answer': 3
            },
            {
                'question': 'What is the name of the technology that allows devices to communicate wirelessly?',
                'options': ['Wi-Fi', 'Bluetooth', 'Cellular', 'All of the above'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the ancient Greek philosopher who is considered the father of western philosophy?',
                'options': ['Plato', 'Aristotle', 'Socrates', 'Pythagoras'],
                'answer': 2
            },
            {
                'question': 'Which event marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            },
            {
                'question': 'What is the name of the ancient Egyptian queen who was known for her beauty and power?',
                'options': ['Nefertiti', 'Cleopatra', 'Hatshepsut', 'Neferkare'],
                'answer': 1
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'Which country is known as the Land of the Rising Sun?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 1
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Neptune'],
                'answer': 1
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
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['options'][question['answer']])

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()