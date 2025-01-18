import random
import json
import requests

# Define the topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23,249,425 digits.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.'
        ],
        'quiz_questions': [
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
                'question': 'What is the name of the process where water changes from a liquid to a gas?',
                'options': ['Evaporation', 'Condensation', 'Precipitation', 'Transpiration'],
                'answer': 'Evaporation'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym "RAM" stand for?',
                'options': ['Random Access Memory', 'Rapid Access Memory', 'Read-only Access Memory', 'Reactive Access Memory'],
                'answer': 'Random Access Memory'
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Greeks', 'Romans', 'Egyptians', 'Mayans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'What was the name of the first successful voyage around the world?',
                'options': ['The Magellan Expedition', 'The Columbus Voyage', 'The Vasco da Gama Expedition', 'The Leif Erikson Voyage'],
                'answer': 'The Magellan Expedition'
            },
            {
                'question': 'Which century did the American Civil War take place in?',
                'options': ['18th century', '19th century', '20th century', '21st century'],
                'answer': '19th century'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has 23,249,425 digits.',
            'The first commercial airline flight took place on January 1, 1914.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Who is credited with inventing the telephone?',
                'options': ['Thomas Edison', 'Alexander Graham Bell', 'Nikola Tesla', 'Marie Curie'],
                'answer': 'Alexander Graham Bell'
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
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter the number of your answer: "))
    if quiz_question['options'][user_answer-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}.")

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
    
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