import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human brain has about 86 billion neurons.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Bioluminescence is the production and emission of light by a living organism.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which of these is a type of renewable energy?',
                'options': ['Coal', 'Oil', 'Nuclear', 'Solar'],
                'answer': 3
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Uranus'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was created in 1983 and was called the \"Brain\" virus.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym \"RAM\" stand for?',
                'options': ['Random Access Memory', 'Read-only Memory', 'Rapid Access Memory', 'Reconfigurable Array Memory'],
                'answer': 0
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Mozilla Firefox', 'Google Chrome', 'Microsoft Edge', 'Netscape Navigator'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BCE.',
            'The Roman Empire lasted for over 400 years, from 27 BCE to 476 CE.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Ancient Greece', 'Ancient Egypt', 'Ancient China'],
                'answer': 1
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 2
            },
            {
                'question': 'Which event marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest organ in the human body is the skin.',
            'The largest moon of Saturn is Titan, which is larger than the planet Mercury.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 3
            },
            {
                'question': 'Who wrote the famous novel \"To Kill a Mockingbird\"?',
                'options': ['Harper Lee', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Mark Twain'],
                'answer': 0
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
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer >= 1 and user_answer <= 4:
                if user_answer - 1 == question['answer']:
                    print("Correct!")
                    return
                else:
                    print("Incorrect. Please try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your choice: ").lower()
        if user_topic in topics:
            print(f"\nHere's a random fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(user_topic)
            print("\nGreat job! Would you like to explore another topic?")
            continue
        else:
            print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()