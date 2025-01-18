import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'Bananas are slightly radioactive.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the process by which plants convert light energy into chemical energy?',
                'options': ['Photosynthesis', 'Respiration', 'Osmosis', 'Diffusion'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first text message was sent on December 3, 1992.',
            'The first commercial jet flight took place in 1952.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first web browser created by Tim Berners-Lee?',
                'options': ['Mosaic', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            }
        ]
    },
    'history': {
        'facts': [
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Great Wall of China was built over 2,000 years ago.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.'
        ],
        'quiz': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplane', 'The Monoplane'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'Honey is the only food that does not spoil.',
            'The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, expands and rises.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Io'],
                'answer': 'Titan'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}")

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("Now, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()