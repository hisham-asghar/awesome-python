import random
import requests
import json

# Define topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first confirmed meteorite impact in the United States occurred in 1807 in Weston, Connecticut.',
            'The largest known prime number as of 2022 has 23,249,425 digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            },
            {
                'question': 'What is the chemical symbol for the element gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Combustion'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial microprocessor, the Intel 4004, was released in 1971.',
            'The first smartphone, the IBM Simon, was introduced in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the company that developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first web browser, created by Tim Berners-Lee?',
                'options': ['Mosaic', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Magna Carta, a landmark document in the history of democracy, was signed in 1215 in England.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz_questions': [
            {
                'question': 'What year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful voyage around the world?',
                'options': ['The Odyssey', 'The Voyage of the Beagle', 'The Magellan Expedition', 'The Lewis and Clark Expedition'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23,249,425 digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was going 8 mph.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean in the world?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the tallest mountain in the world?',
                'options': ['Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            },
            {
                'question': 'What is the largest mammal in the world?',
                'options': ['African Elephant', 'Blue Whale', 'Sperm Whale', 'Asian Elephant'],
                'answer': 1
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
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['options'][quiz_question['answer']])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
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