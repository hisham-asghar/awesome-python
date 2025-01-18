import random
import requests
import json

# Topics and their corresponding fact and quiz data
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'Bananas are slightly radioactive.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.'
        ],
        'quizzes': [
            {
                'question': 'Which of these is NOT a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma', 'Emotion'],
                'answer': 'Emotion'
            },
            {
                'question': 'What is the symbol for the element gold on the periodic table?',
                'options': ['Au', 'Ag', 'Cu', 'Fe', 'Hg'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis', 'Diffusion'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first hard disk drive was 5MB and the size of a large washing machine.',
            'The first text message was sent on December 3, 1992, and it said "Merry Christmas".'
        ],
        'quizzes': [
            {
                'question': 'What does "HTTP" stand for?',
                'options': ['Hyper Text Transfer Protocol', 'High-speed Transmission Technology Protocol', 'Hybrid Telecommunication Transmission Protocol', 'Hyperlink Transfer Protocol'],
                'answer': 'Hyper Text Transfer Protocol'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was doing 8 mph in a 2 mph zone.'
        ],
        'quizzes': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Mayans', 'Incas', 'Aztecs', 'Egyptians'],
                'answer': 'Egyptians'
            },
            {
                'question': 'Who is considered the father of modern computer science?',
                'options': ['Alan Turing', 'Bill Gates', 'Steve Jobs', 'Ada Lovelace'],
                'answer': 'Alan Turing'
            }
        ]
    },
    'general': {
        'facts': [
            'A group of porcupines is called a prickle.',
            'Apples are more effective at waking you up in the morning than coffee.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Moose'],
                'answer': 'Giraffe'
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

def get_quiz(topic):
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()