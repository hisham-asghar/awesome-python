import random
import requests
import json

# Define the topics and their corresponding facts/quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The fastest gust of wind ever recorded on Earth was 253 mph (407 km/h) during Tropical Cyclone Olivia in 1996.',
            'The hottest planet in the Solar System is Venus, not Mercury.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 'Plasma'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Europa'],
                'answer': 'Titan'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first smartphone was the IBM Simon, released in 1992.',
            'The first digital camera was developed by Kodak in 1975 and weighed 8 pounds.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company is known for creating the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first web browser, created by Tim Berners-Lee?',
                'options': ['Mosaic', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching approximately 13,171 miles (21,196 km).',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first book printed in English was the Recuyell of the Historyes of Troye, printed by William Caxton in 1473.'
        ],
        'quizzes': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Mayans', 'Incas', 'Egyptians', 'Romans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['Kitty Hawk', 'Spirit of St. Louis', 'Concorde', 'Apollo 11'],
                'answer': 'Kitty Hawk'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'Bananas are slightly radioactive.',
            'The first person convicted of speeding was going 8 mph.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_random_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz['answer']}")

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()