import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first synthetic plastic was created in 1907 and called Bakelite.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'options': ['Respiration', 'Photosynthesis', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first spam email was sent in 1978 by a marketing representative of Digital Equipment Corporation.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first web browser, developed at CERN in 1990?',
                'options': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            },
            {
                'question': 'What is the name of the company that created the first commercially successful personal computer?',
                'options': ['Apple', 'IBM', 'Microsoft', 'Commodore'],
                'answer': 'IBM'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.'
        ],
        'quiz': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1787', '1789', '1812'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Spruce Goose', 'The Concorde', 'The Apollo'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The Mona Lisa has no visible eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first product to have a barcode was Wrigley's gum.',
            'Apples are more effective at waking you up in the morning than coffee.'
        ],
        'quiz': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'India', 'Korea'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the given topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Returns a random quiz question from the given topic.
    """
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}")

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
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()