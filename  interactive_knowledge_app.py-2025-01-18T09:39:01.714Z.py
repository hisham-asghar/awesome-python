import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first successful kidney transplant was performed in 1954.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 1
            },
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Centrifugal force', 'Electromagnetic force', 'Nuclear force'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first mobile phone call was made in 1973 by Martin Cooper of Motorola.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language that was designed to be easy to read and write?',
                'options': ['Java', 'Python', 'C++', 'Ruby'],
                'answer': 1
            },
            {
                'question': 'Which company is known for developing the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the process by which data is transmitted over the internet?',
                'options': ['Encoding', 'Compression', 'Encryption', 'Packet switching'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.',
            'The first successful powered flight took place in 1903 by the Wright brothers.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'India'],
                'answer': 2
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'Which event is considered the start of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest building in the world is the Burj Khalifa in Dubai, standing at 828 meters (2,717 feet).',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean'],
                'answer': 2
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Fetches a random quiz question from the specified topic.
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
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()