import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'A teaspoon of neutron star material would weigh about 1 billion tons on Earth.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Neptune', 'Uranus'],
                'answer': 0
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'What is the chemical symbol for the element gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called 'Creeper', was created in 1971 as an experiment.',
            'The first commercially available personal computer was the Altair 8800, released in 1975.',
            'The world's first text message was sent on December 3, 1992, and it read "Merry Christmas".'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the operating system developed by Apple Inc.?',
                'options': ['Windows', 'Linux', 'macOS', 'Android'],
                'answer': 2
            },
            {
                'question': 'What is the name of the device used to connect a computer to the internet?',
                'options': ['Monitor', 'Keyboard', 'Mouse', 'Modem'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz_questions': [
            {
                'question': 'In what year did the United States declare its independence?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Theodore Roosevelt'],
                'answer': 2
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['Mesopotamian', 'Sumerian', 'Mayan', 'Egyptian'],
                'answer': 3
            }
        ]
    },
    'general': {
        'facts': [
            'A group of flamingos is called a 'flamboyance'.',
            'The word 'sandwich' is named after the 4th Earl of Sandwich, who is credited with inventing it.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was doing 8 mph, the speed limit was 2 mph.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Nile River', 'Amazon River', 'Mississippi River', 'Yangtze River'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", quiz_question['options'][quiz_question['answer']])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
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