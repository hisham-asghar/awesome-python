import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Bees can fly higher than Mount Everest.'
        ],
        'quiz': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Hydrogen'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Marie Curie', 'Albert Einstein', 'Stephen Hawking'],
                'answer': 2
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Uranus'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first commercial text message was sent on December 3, 1992.',
            'The internet was originally called ARPANET, which stood for Advanced Research Projects Agency Network.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which company is known for creating the first personal computer?',
                'options': ['Apple', 'Microsoft', 'IBM', 'HP'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Internet Explorer', 'Mozilla Firefox', 'Google Chrome', 'Mosaic'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was stolen from the Louvre museum in Paris in 1911 and recovered two years later.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Egyptian', 'Mesopotamian'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first President of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'Which event marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A group of pugs is called a grumble.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics.keys():
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here\'s a random fact about {topic.capitalize()}:')
    print(f'- {fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge with a quiz!')
    score = 0
    for question in topics[topic]['quiz']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): ')) - 1
        if user_answer == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['options'][question['answer']])
    print(f'Your final score is {score} out of {len(topics[topic]["quiz"])}.')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()