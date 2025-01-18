import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Water is the only substance that exists naturally on Earth in three forms: solid, liquid, and gas.'
        ],
        'quiz': [
            {
                'question': 'What is the smallest known particle in the universe?',
                'options': ['Atom', 'Electron', 'Quark', 'Neutrino'],
                'answer': 2
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first digital computer, ENIAC, was completed in 1946 and occupied 1,800 square feet.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 0
            },
            {
                'question': 'What is the name of the first digital computer?',
                'options': ['ENIAC', 'UNIVAC', 'MARK I', 'COLOSSUS'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 2
            },
            {
                'question': 'Which event marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The attack on Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.',
            'A group of porcupines is called a prickle.'
        ],
        'quiz': [
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon', 'Nile', 'Mississippi', 'Yangtze'],
                'answer': 1
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    quiz_questions = topics[topic]['quiz']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
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