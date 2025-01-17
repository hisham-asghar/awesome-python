import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first successful kidney transplant was performed in 1954.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which element is the most abundant in the universe?',
                'options': ['Hydrogen', 'Helium', 'Oxygen', 'Carbon'],
                'answer': 'Hydrogen'
            },
            {
                'question': 'What is the name of the first artificial satellite launched into Earth\'s orbit?',
                'options': ['Sputnik 1', 'Explorer 1', 'Vanguard 1', 'Telstar 1'],
                'answer': 'Sputnik 1'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and cost $15.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The world\'s first website was launched on August 6, 1991.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Internet Explorer', 'Netscape Navigator', 'Mozilla Firefox', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first successful kidney transplant was performed in 1954 by Dr. Joseph Murray.'
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
                'question': 'What was the name of the first successful powered flight by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplaner', 'The Kitty Hawk'],
                'answer': 'The Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Who is the author of the Harry Potter book series?',
                'options': ['J.K. Rowling', 'Stephen King', 'J.R.R. Tolkien', 'Agatha Christie'],
                'answer': 'J.K. Rowling'
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
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    """
    Displays a menu for users to select a topic and interact with the knowledge-sharing script.
    """
    print("Welcome to the Interactive Knowledge Sharing Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize(), ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()