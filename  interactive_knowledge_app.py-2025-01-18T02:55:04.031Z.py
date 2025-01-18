import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Diamonds are the hardest known natural material on Earth.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Hydrogen'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The world's first programmable computer was the ENIAC, which was completed in 1946.',
            'The first commercial smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the protocol used to transfer data over the internet?',
                'options': ['HTTP', 'FTP', 'SMTP', 'DHCP'],
                'answer': 'HTTP'
            },
            {
                'question': 'What is the name of the device used to connect multiple computers in a network?',
                'options': ['Router', 'Modem', 'Switch', 'Firewall'],
                'answer': 'Router'
            }
        ]
    },
    'history': {
        'facts': [
            'The Pyramids of Giza were built around 2560–2540 BC.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1776', '1945'],
                'answer': '1861'
            },
            {
                'question': 'What was the name of the ancient Greek philosopher who is considered the father of Western philosophy?',
                'options': ['Plato', 'Socrates', 'Aristotle', 'Pythagoras'],
                'answer': 'Socrates'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe.',
            'The largest moon in our solar system is Ganymede, a moon of Jupiter.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Pacific Ocean', 'Indian Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the currency used in Japan?',
                'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
                'answer': 'Yen'
            },
            {
                'question': 'What is the name of the largest continent on Earth?',
                'options': ['Asia', 'Africa', 'Europe', 'North America'],
                'answer': 'Asia'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Fetches a random fact from the selected topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Fetches a random quiz question and its options from the selected topic.
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
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if question['options'][int(user_answer)-1] == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Invalid input. Please try again.")

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print(f"Random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow let's test your knowledge!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()