import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or a predefined database.
    """
    facts = {
        'science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A group of porcupines is called a prickle.'
        ],
        'technology': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The world's first text message was sent on December 3, 1992, and read "Merry Christmas".'
        ],
        'history': [
            'The Great Wall of China is the only man-made structure visible from space.',
            'The Aztec Empire was conquered by the Spanish in 1521.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'general': [
            'A group of flamingos is called a flamboyance.',
            'The world's largest desert is Antarctica.',
            'The shortest war in history was between Zanzibar and the United Kingdom in 1896, lasting between 38 and 45 minutes.'
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return 'Sorry, that topic is not available.'

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic, fetching questions and answers from a public API or a predefined database.
    """
    questions = {
        'science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'choices': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'choices': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            }
        ],
        'technology': [
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'choices': ['Internet Explorer', 'Netscape Navigator', 'Google Chrome', 'Mozilla Firefox'],
                'answer': 'Netscape Navigator'
            },
            {
                'question': 'Which company developed the first personal computer, the MITS Altair 8800?',
                'choices': ['Apple', 'IBM', 'Microsoft', 'MITS'],
                'answer': 'MITS'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'choices': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ],
        'history': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'choices': ['Mayans', 'Incas', 'Egyptians', 'Romans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'What year did the United States declare independence?',
                'choices': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 'George Washington'
            }
        ],
        'general': [
            {
                'question': 'What is the largest ocean on Earth?',
                'choices': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest mammal on Earth?',
                'choices': ['Elephant', 'Giraffe', 'Blue Whale', 'Hippopotamus'],
                'answer': 'Blue Whale'
            },
            {
                'question': 'What is the tallest building in the world?',
                'choices': ['Burj Khalifa', 'Shanghai Tower', 'Taipei 101', 'One World Trade Center'],
                'answer': 'Burj Khalifa'
            }
        ]
    }
    
    if topic in questions:
        question = random.choice(questions[topic])
        print(question['question'])
        for i, choice in enumerate(question['choices'], start=1):
            print(f"{i}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if question['choices'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
    else:
        print("Sorry, that topic is not available.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = input("Enter the number of the topic (1-4): ")
    
    if topic_choice == '1':
        topic = 'science'
    elif topic_choice == '2':
        topic = 'technology'
    elif topic_choice == '3':
        topic = 'history'
    elif topic_choice == '4':
        topic = 'general'
    else:
        print("Invalid choice. Exiting the program.")
        return
    
    print(f"You selected the {topic} topic.")
    
    print("Here's a random fact or concept:")
    print(get_random_fact(topic))
    
    print("Now, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == '__main__':
    main()