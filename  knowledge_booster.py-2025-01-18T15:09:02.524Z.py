import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': [
        {
            'fact': 'The human body has around 60,000 miles of blood vessels.',
            'quiz': {
                'question': 'How many miles of blood vessels are in the human body?',
                'options': ['30,000', '45,000', '60,000', '75,000'],
                'answer': '60,000'
            }
        },
        {
            'fact': 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'quiz': {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['It was the fashion in Renaissance Florence to shave them off', 'She lost them in an accident', 'The artist forgot to paint them', 'It's a part of the painting's mystery'],
                'answer': 'It was the fashion in Renaissance Florence to shave them off'
            }
        }
    ],
    'technology': [
        {
            'fact': 'The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.',
            'quiz': {
                'question': 'What was the first computer bug?',
                'options': ['A software error', 'A hardware malfunction', 'A real moth', 'A virus'],
                'answer': 'A real moth'
            }
        },
        {
            'fact': 'The term 'OK' originated in the 1830s as an abbreviation for 'all correct' in the Boston Morning Post.',
            'quiz': {
                'question': 'What is the origin of the term 'OK'?',
                'options': ['It was a popular slang term in the 1830s', 'It was an abbreviation for 'all correct' in the Boston Morning Post', 'It was a shorthand used by early computer programmers', 'It was a military acronym'],
                'answer': 'It was an abbreviation for 'all correct' in the Boston Morning Post'
            }
        }
    ],
    'history': [
        {
            'fact': 'The ancient Egyptians built the pyramids as tombs for their pharaohs. Each pyramid was a massive stone monument to the pharaoh's life.',
            'quiz': {
                'question': 'What were the ancient Egyptian pyramids built for?',
                'options': ['Religious ceremonies', 'As granaries to store food', 'As tombs for their pharaohs', 'As defensive structures'],
                'answer': 'As tombs for their pharaohs'
            }
        },
        {
            'fact': 'The Great Wall of China is the only man-made structure visible from space.',
            'quiz': {
                'question': 'Which of the following is true about the Great Wall of China?',
                'options': ['It is the longest wall in the world', 'It is the only man-made structure visible from space', 'It was built to keep out invaders', 'All of the above'],
                'answer': 'All of the above'
            }
        }
    ],
    'general': [
        {
            'fact': 'A group of flamingos is called a 'flamboyance'.',
            'quiz': {
                'question': 'What is a group of flamingos called?',
                'options': ['A flock', 'A colony', 'A flamboyance', 'A parade'],
                'answer': 'A flamboyance'
            }
        },
        {
            'fact': 'Bananas are slightly radioactive.',
            'quiz': {
                'question': 'Why are bananas slightly radioactive?',
                'options': ['They contain potassium-40, a radioactive isotope of potassium', 'They are grown near nuclear power plants', 'They are sprayed with radioactive pesticides', 'They absorb radiation from the sun'],
                'answer': 'They contain potassium-40, a radioactive isotope of potassium'
            }
        }
    ]
}

def get_random_fact_and_quiz(topic):
    """
    Retrieves a random fact and quiz question for the given topic.
    """
    topic_facts = topics[topic]
    random_index = random.randint(0, len(topic_facts) - 1)
    return topic_facts[random_index]

def run_quiz(fact, quiz):
    """
    Runs the quiz for the given fact and quiz question.
    """
    print(fact)
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if quiz['options'][int(user_answer) - 1] == quiz['answer']:
                print("Correct!")
                return
            else:
                print("Incorrect. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    """
    Runs the interactive knowledge-sharing script.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to get started:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter a topic (or 'quit' to exit): ").lower()
        if user_topic == 'quit':
            break
        if user_topic in topics:
            fact_and_quiz = get_random_fact_and_quiz(user_topic)
            run_quiz(fact_and_quiz['fact'], fact_and_quiz['quiz'])
            print("Great job!")
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()