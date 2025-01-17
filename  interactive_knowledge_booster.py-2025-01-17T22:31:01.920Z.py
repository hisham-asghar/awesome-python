import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Bees have five eyes: two compound eyes and three simple eyes.'
        ],
        'quiz': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is known for his theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Neptune'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The world's first programmable computer was the ENIAC, completed in 1946.',
            'The internet was initially called ARPANET, and it was created by the U.S. Department of Defense.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company developed the first commercial graphical user interface (GUI) for personal computers?',
                'options': ['Apple', 'Microsoft', 'IBM', 'Xerox'],
                'answer': 'Xerox'
            },
            {
                'question': 'What is the name of the device that converts digital information into analog signals for transmission over telephone lines?',
                'options': ['Modem', 'Router', 'Ethernet', 'Firewall'],
                'answer': 'Modem'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 'Greece'
            },
            {
                'question': 'What was the name of the famous explorer who discovered America?',
                'options': ['Christopher Columbus', 'Vasco da Gama', 'Marco Polo', 'Ferdinand Magellan'],
                'answer': 'Christopher Columbus'
            },
            {
                'question': 'Which war lasted from 1939 to 1945 and involved most of the world's nations?',
                'options': ['World War I', 'World War II', 'Vietnam War', 'Korean War'],
                'answer': 'World War II'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe.',
            'The largest moon in our solar system is Ganymede, which orbits Jupiter.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'],
                'answer': 'Nile River'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
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
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}")

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

if __name__ == '__main__':
    main()