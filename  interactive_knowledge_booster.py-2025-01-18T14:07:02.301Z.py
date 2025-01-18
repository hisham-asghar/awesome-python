import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'Diamonds are the hardest known natural material on Earth.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the nearest star to the Earth?',
                'options': ['Sirius', 'Proxima Centauri', 'Betelgeuse', 'Polaris'],
                'answer': 'Proxima Centauri'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The world's first programmable computer was the ENIAC, completed in 1946.',
            'The first commercial jet airliner was the de Havilland Comet, introduced in 1952.'
        ],
        'quiz_questions': [
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
                'question': 'What is the name of the first commercial web browser?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560–2540 BCE.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first successful manned space flight?',
                'options': ['Apollo 11', 'Sputnik 1', 'Vostok 1', 'Mercury-Redstone 3'],
                'answer': 'Vostok 1'
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 'Mesopotamia'
            },
            {
                'question': 'What was the name of the first successful powered flight?',
                'options': ['The Wright Flyer', 'Kitty Hawk', 'Orville and Wilbur', 'First in Flight'],
                'answer': 'The Wright Flyer'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
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

def get_random_quiz_question(topic):
    return random.choice(topics[topic]['quiz_questions'])

def run_quiz(topic):
    quiz_question = get_random_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question['options'][user_answer-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
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