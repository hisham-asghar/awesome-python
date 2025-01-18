import random
import requests
import json

def get_random_fact(topic):
    """
    Fetch a random fact or concept for the given topic using a public API or predefined data.
    """
    # Implement API calls or use predefined data to fetch a random fact
    facts = {
        'science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A single cloud can weigh more than 1 million pounds.'
        ],
        'technology': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The word 'computer' was originally used to describe a person who performed calculations or computations.'
        ],
        'history': [
            'The Great Wall of China is the only man-made structure visible from space.',
            'The Pyramids of Giza are the only remaining Wonder of the Ancient World.',
            'The first emperor of the unified China was Qin Shi Huang, who reigned from 221 to 210 BC.'
        ],
        'general': [
            'Apples are more effective at waking you up in the morning than coffee.',
            'A group of porcupines is called a prickle.',
            'Fingernails grow nearly 4 times faster than toenails.'
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return 'Sorry, I don't have any facts for that topic.'

def quiz(topic):
    """
    Provide a multiple-choice quiz for the given topic.
    """
    # Implement quiz questions and answers for the given topic
    quizzes = {
        'science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 0
            }
        ],
        'technology': [
            {
                'question': 'What does the acronym "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Computerized Processing Unit', 'Central Power Unit'],
                'answer': 0
            },
            {
                'question': 'Who is considered the father of the World Wide Web?',
                'options': ['Bill Gates', 'Steve Jobs', 'Tim Berners-Lee', 'Mark Zuckerberg'],
                'answer': 2
            }
        ],
        'history': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': 0
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Mesopotamia', 'Indus Valley', 'Aztec', 'Ancient Egypt'],
                'answer': 3
            }
        ],
        'general': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 2
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['O-', 'A+', 'B-', 'AB-'],
                'answer': 3
            }
        ]
    }
    
    if topic in quizzes:
        quiz_data = random.choice(quizzes[topic])
        print(quiz_data['question'])
        for i, option in enumerate(quiz_data['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == quiz_data['answer']:
            print('Correct!')
        else:
            print('Incorrect. Better luck next time!')
    else:
        print(f'Sorry, I don't have any quizzes for the {topic} topic.')

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Select a topic to get started:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General')
    
    topic_choice = int(input('Enter your choice (1-4): '))
    
    topics = ['science', 'technology', 'history', 'general']
    selected_topic = topics[topic_choice - 1]
    
    print(f'\nRandom fact about {selected_topic.title()}:')
    print(get_random_fact(selected_topic))
    
    print(f'\nNow, let's test your knowledge with a {selected_topic.title()} quiz!')
    quiz(selected_topic)

if __name__ == '__main__':
    main()