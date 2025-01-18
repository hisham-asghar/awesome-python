import random
import requests
import json

# Define the topics and their associated facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Diamonds are the hardest known natural material on Earth.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical formula for water?',
                'options': ['H2O', 'CO2', 'NaCl', 'O2'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Marie Curie', 'Charles Darwin'],
                'answer': 1
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Combustion', 'Evaporation'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946.',
            'The internet was created in 1969 by the U.S. Department of Defense.',
            'The smartphone was invented by IBM in 1992.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Google Chrome', 'Mozilla Firefox', 'Internet Explorer', 'Mosaic'],
                'answer': 3
            },
            {
                'question': 'What is the primary function of a computer processor (CPU)?',
                'options': ['To store data', 'To generate graphics', 'To execute instructions', 'To connect to the internet'],
                'answer': 2
            },
            {
                'question': 'What is the term used to describe the miniaturization of electronic components?',
                'options': ['Nanotechnology', 'Biotechnology', 'Automation', 'Digitization'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight was achieved by the Wright brothers in 1903.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful American space mission?',
                'options': ['Apollo 11', 'Sputnik 1', 'Mercury-Redstone 3', 'Gemini 3'],
                'answer': 2
            },
            {
                'question': 'Which event is considered the start of the American Civil War?',
                'options': ['The Battle of Gettysburg', 'The Emancipation Proclamation', 'The Assassination of Abraham Lincoln', 'The Attack on Fort Sumter'],
                'answer': 3
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 21,000 kilometers (13,000 miles).'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Dollar', 'Euro', 'Yen', 'Won'],
                'answer': 2
            },
            {
                'question': 'Who is considered the father of modern medicine?',
                'options': ['Hippocrates', 'Marie Curie', 'Louis Pasteur', 'Alexander Fleming'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    """Retrieve a random fact from the selected topic."""
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """Retrieve a random quiz question from the selected topic."""
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz['question'], quiz['options'], quiz['answer']

def run_quiz(topic):
    """Run a quiz for the selected topic."""
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question, options, answer = get_quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{num_questions}")

def main():
    """Main function to run the interactive knowledge app."""
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"You selected the {chosen_topic.capitalize()} topic.")
        print(get_random_fact(chosen_topic))
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()