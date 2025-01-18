import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest known prime number?',
                'options': ['Mersenne prime', 'Fermat prime', 'Gaussian prime', 'Fibonacci prime'],
                'answer': 'Mersenne prime'
            },
            {
                'question': 'Which planet in the solar system has the highest surface temperature?',
                'options': ['Mercury', 'Venus', 'Mars', 'Jupiter'],
                'answer': 'Venus'
            },
            {
                'question': 'Approximately how many miles of blood vessels are in the human body?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '90,000 miles'],
                'answer': '60,000 miles'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real moth found trapped in a Harvard Mark II computer.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first email was sent by Ray Tomlinson in 1971, and the first email subject line was "QWERTYUIOP".'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first commercial computer?',
                'options': ['ENIAC', 'UNIVAC I', 'IBM 701', 'Apple I'],
                'answer': 'UNIVAC I'
            },
            {
                'question': 'What was the first email subject line?',
                'options': ['Hello', 'Test', 'QWERTYUIOP', 'Greetings'],
                'answer': 'QWERTYUIOP'
            },
            {
                'question': 'What was the first computer bug?',
                'options': ['A moth', 'A spider', 'A virus', 'A worm'],
                'answer': 'A moth'
            }
        ]
    },
    'history': {
        'facts': [
            'The Colosseum in Rome was built in the 1st century AD and could hold up to 80,000 spectators.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight by the Wright brothers took place in 1903 and lasted 12 seconds.'
        ],
        'quiz': [
            {
                'question': 'How many spectators could the Colosseum in Rome hold?',
                'options': ['20,000', '40,000', '60,000', '80,000'],
                'answer': '80,000'
            },
            {
                'question': 'How long did the first successful powered flight by the Wright brothers last?',
                'options': ['6 seconds', '9 seconds', '12 seconds', '15 seconds'],
                'answer': '12 seconds'
            },
            {
                'question': 'What is the approximate length of the Great Wall of China?',
                'options': ['5,000 miles', '8,000 miles', '10,000 miles', '13,000 miles'],
                'answer': '13,000 miles'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2021 has over 23 million digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A group of porcupines is called a prickle.'
        ],
        'quiz': [
            {
                'question': 'How many digits does the largest known prime number have?',
                'options': ['10 million', '15 million', '20 million', '23 million'],
                'answer': '23 million'
            },
            {
                'question': 'What was the fashion in Renaissance Florence regarding eyebrows?',
                'options': ['To shave them off', 'To pluck them', 'To dye them', 'To accentuate them'],
                'answer': 'To shave them off'
            },
            {
                'question': 'What is a group of porcupines called?',
                'options': ['A quill', 'A spike', 'A prickle', 'A quiver'],
                'answer': 'A prickle'
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
    print(f"Question: {quiz_question['question']}")
    for i, option in enumerate(quiz_question['options'], start=1):
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question['options'][user_answer - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()