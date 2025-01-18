import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Bees can fly higher than Mount Everest.'
        ],
        'quizzes': [
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 3
            },
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Friction', 'Centrifugal force', 'Electromagnetic force'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was called \"Brain\" and was created in 1986.',
            'The first mobile phone call was made on April 3, 1973 by Martin Cooper of Motorola.',
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which of these is not a type of computer memory?',
                'options': ['RAM', 'ROM', 'CPU', 'SSD'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first web browser created by Tim Berners-Lee?',
                'options': ['Mosaic', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first moon landing was on July 20, 1969, when Neil Armstrong and Buzz Aldrin landed on the moon.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mayan'],
                'answer': 2
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'Benjamin Franklin'],
                'answer': 1
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['Spirit of St. Louis', 'Flyer I', 'Wright Flyer', 'Kitty Hawk'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quizzes': [
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
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
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

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz['answer']:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    Runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your topic choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()