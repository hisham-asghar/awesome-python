import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'Cats have fewer toes on their back paws than their front paws.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Mitosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first text message was sent on December 3, 1992, and it said "Merry Christmas".',
            'The first commercial smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first programmable computer?',
                'options': ['ENIAC', 'UNIVAC', 'Babbage', 'Turing'],
                'answer': 'ENIAC'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
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
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The Pyramids of Giza in Egypt were built around 2560–2540 BC.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first English colony in North America?',
                'options': ['Jamestown', 'Plymouth', 'Roanoke', 'New Amsterdam'],
                'answer': 'Jamestown'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the event that started World War I?',
                'options': ['The Assassination of Archduke Franz Ferdinand', 'The Invasion of Poland', 'The Bombing of Pearl Harbor', 'The Cuban Missile Crisis'],
                'answer': 'The Assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2023 has 23,249,425 digits.',
            'The world's largest desert is Antarctica, which is a desert because it receives very little precipitation.',
            'The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis, a type of lung disease.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Blue Whale'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the smallest country in the world by land area?',
                'options': ['Vatican City', 'Monaco', 'Nauru', 'Tuvalu'],
                'answer': 'Vatican City'
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    quiz = topics[topic]['quiz']
    question = random.choice(quiz)
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if question['options'][user_answer-1] == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['answer'])

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