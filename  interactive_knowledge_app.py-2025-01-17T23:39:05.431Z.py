import random
import requests
from datetime import datetime

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first successful kidney transplant was performed in 1954.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
                'answer': 1
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called "Creeper," was created in 1971.',
            'The first commercial smartphone, the IBM Simon, was released in 1992.',
            'The first programmable computer, the ENIAC, was completed in 1946.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language that is commonly used for web development?',
                'options': ['Java', 'Python', 'C++', 'JavaScript'],
                'answer': 3
            },
            {
                'question': 'What is the name of the technology that allows devices to connect to the internet wirelessly?',
                'options': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Infrared'],
                'answer': 1
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals for transmission over telephone lines?',
                'options': ['Modem', 'Router', 'Switch', 'Hub'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the ancient civilization that built the pyramids in Egypt?',
                'options': ['Aztec', 'Mayan', 'Roman', 'Egyptian'],
                'answer': 3
            },
            {
                'question': 'What is the name of the event that marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            },
            {
                'question': 'What is the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has over 23 million digits.',
            'The tallest mammal is the giraffe, which can grow up to 18 feet tall.',
            'The Mona Lisa has no eyebrows, as it was the fashion in Renaissance-era Italy to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'],
                'answer': 1
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['options'][quiz_question['answer']])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()