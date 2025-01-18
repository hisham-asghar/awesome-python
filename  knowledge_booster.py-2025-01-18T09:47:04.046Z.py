import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2021 has 23,249,425 digits.',
            'The first digital computer, ENIAC, was completed in 1946 and weighed over 30 tons.'
        ],
        'quiz': [
            {
                'question': 'Which of the following is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The first iPhone was released in 2007 and had a 3.5-inch display.',
            'The first electronic computer, ENIAC, was Turing-complete and could be reprogrammed to solve 'a large class of numerical problems' through 'setting of function tables, plugging of function tables, and setting switches.''
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company developed the first commercially successful personal computer, the IBM PC, in 1981?',
                'options': ['Apple', 'Microsoft', 'IBM', 'Google'],
                'answer': 'IBM'
            },
            {
                'question': 'What is the name of the algorithm used to compress data in the ZIP file format?',
                'options': ['LZW', 'Huffman', 'Shannon-Fano', 'Arithmetic Coding'],
                'answer': 'LZW'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Roman Empire, at its height in the 2nd century AD, covered an area of over 5 million square kilometers.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mesopotamians', 'Chinese'],
                'answer': 'Mesopotamians'
            },
            {
                'question': 'What was the name of the first successful voyage around the world, completed by Ferdinand Magellan in 1522?',
                'options': ['The Voyages of Christopher Columbus', 'The Silk Road', 'The Circumnavigation of the Globe', 'The Age of Exploration'],
                'answer': 'The Circumnavigation of the Globe'
            },
            {
                'question': 'Which event is considered the start of the American Civil War?',
                'options': ['The Boston Massacre', 'The Battle of Gettysburg', 'The Emancipation Proclamation', 'The Attack on Fort Sumter'],
                'answer': 'The Attack on Fort Sumter'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2021 has 23,249,425 digits.',
            'The largest known prime number as of 2021 has 23,249,425 digits.',
            'The largest known prime number as of 2021 has 23,249,425 digits.'
        ],
        'quiz': [
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Yuan', 'Won', 'Yen', 'Peso'],
                'answer': 'Yen'
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
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()