import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Cats have fewer toes on their back paws than their front paws.'
        ],
        'quiz': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Water vapor'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first spam email was sent in 1978 by a marketing firm advertising a new computer.',
            'The world's first website was launched in 1991 and was about the World Wide Web project.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            },
            {
                'question': 'What is the name of the technology that allows devices to connect to the internet without a physical cable?',
                'options': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Fiber optic'],
                'answer': 'Wi-Fi'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1775', '1914'],
                'answer': '1861'
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Mesopotamia', 'Indus Valley', 'Aztec', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and elongates the structure.',
            'A group of flamingos is called a flamboyance.'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Which country is known as the \"Land of the Rising Sun\"?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
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
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question['options'][user_answer-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()