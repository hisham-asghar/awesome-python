import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Sharks have been around for over 400 million years, predating the dinosaurs.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the largest organ in the human body?',
                'choices': ['Liver', 'Skin', 'Heart', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'Which element has the chemical symbol H?',
                'choices': ['Hydrogen', 'Helium', 'Lithium', 'Sodium'],
                'answer': 'Hydrogen'
            },
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called "Brain," was created in 1986.',
            'The first commercial text message was sent in 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'choices': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the company that created the Android operating system?',
                'choices': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the technology that allows devices to connect to the internet wirelessly?',
                'choices': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Cellular'],
                'answer': 'Wi-Fi'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight was made by the Wright brothers in 1903.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quizzes': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'choices': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'choices': ['Mesopotamia', 'Aztec', 'Inca', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 18 feet tall.',
            'The largest ocean on Earth is the Pacific Ocean.',
            'The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles get further apart and the tower grows.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'choices': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'choices': ['Amazon', 'Nile', 'Mississippi', 'Yangtze'],
                'answer': 'Nile'
            },
            {
                'question': 'What is the name of the largest mammal on Earth?',
                'choices': ['Elephant', 'Whale', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Whale'
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz(topic):
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, choice in enumerate(quiz['choices']):
        print(f"{i+1}. {choice}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if quiz['choices'][int(user_answer)-1] == quiz['answer']:
                print("Correct!")
                return True
            else:
                print("Incorrect. Try again.")
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your choice: ").lower()
        if user_topic in topics:
            print(f"\nHere's a random fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            
            print("\nNow, let's test your knowledge with a quiz!")
            quiz = get_quiz(user_topic)
            if run_quiz(quiz):
                print("\nGreat job! You've increased your knowledge.")
            else:
                print("\nBetter luck next time!")
            
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()