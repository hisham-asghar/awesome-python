import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Rainbows are formed by the refraction and dispersion of sunlight through water droplets in the atmosphere.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which gas makes up the largest percentage of the Earth\'s atmosphere?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Magnetism', 'Friction', 'Electricity'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first digital computer, ENIAC, was completed in 1946 and weighed over 30 tons.',
            'The first commercial jet airliner, the De Havilland Comet, made its first flight in 1949.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'JavaScript'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone, released by Apple in 2007?',
                'options': ['BlackBerry', 'Nokia 3310', 'iPhone', 'Samsung Galaxy'],
                'answer': 'iPhone'
            },
            {
                'question': 'What is the name of the technology used to transmit data wirelessly between devices?',
                'options': ['Ethernet', 'Wi-Fi', 'Bluetooth', 'NFC'],
                'answer': 'Bluetooth'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Magna Carta, a landmark document in the history of democracy, was signed in 1215.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Ancient Egypt', 'Ancient Greece', 'Ancient China'],
                'answer': 'Ancient Greece'
            },
            {
                'question': 'What was the name of the first permanent English settlement in North America, founded in 1607?',
                'options': ['Jamestown', 'Plymouth Colony', 'Massachusetts Bay Colony', 'New Amsterdam'],
                'answer': 'Jamestown'
            },
            {
                'question': 'Which event marked the end of World War II in Europe?',
                'options': ['D-Day', 'The Battle of Stalingrad', 'The fall of Berlin', 'The atomic bombings of Hiroshima and Nagasaki'],
                'answer': 'The fall of Berlin'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest continent in the world?',
                'options': ['Asia', 'Africa', 'North America', 'Europe'],
                'answer': 'Asia'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the currency used in the United States?',
                'options': ['Euro', 'Pound', 'Yen', 'Dollar'],
                'answer': 'Dollar'
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
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Select a topic to get started:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your topic choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize(), ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()