import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The hottest planet in the Solar System is Venus, not Mercury.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest known prime number as of 2022?',
                'options': ['23 million digits', '23 billion digits', '23 thousand digits', '23 hundred digits'],
                'answer': '23 million digits'
            },
            {
                'question': 'Which planet in the Solar System is the hottest?',
                'options': ['Mercury', 'Venus', 'Mars', 'Jupiter'],
                'answer': 'Venus'
            },
            {
                'question': 'Approximately how many miles of blood vessels are in the human body?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '90,000 miles'],
                'answer': '60,000 miles'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial microprocessor, the Intel 4004, was released in 1971.',
            'The world's first smartphone, the IBM Simon, was introduced in 1992.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first electronic computer, completed in 1946?',
                'options': ['UNIVAC', 'ENIAC', 'MARK I', 'COLOSSUS'],
                'answer': 'ENIAC'
            },
            {
                'question': 'What was the name of the first commercial microprocessor, released in 1971?',
                'options': ['Intel 4004', 'Intel 8080', 'Motorola 6800', 'Zilog Z80'],
                'answer': 'Intel 4004'
            },
            {
                'question': 'What was the name of the world's first smartphone, introduced in 1992?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 9000 Communicator', 'IBM Simon'],
                'answer': 'IBM Simon'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC, and are the oldest and largest of the three pyramids.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.'
        ],
        'quiz': [
            {
                'question': 'Approximately how long is the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            },
            {
                'question': 'Around what year were the Pyramids of Giza in Egypt built?',
                'options': ['2000 BC', '2500 BC', '3000 BC', '3500 BC'],
                'answer': '2560-2540 BC'
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'options': ['Michelangelo', 'Raphael', 'Leonardo da Vinci', 'Vincent van Gogh'],
                'answer': 'Leonardo da Vinci'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known snowflake was 15 inches wide and 8 inches thick, observed in Montana in 1887.',
            'The first commercial airline flight took place on January 1, 1914, and lasted 23 minutes.',
            'The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion causing the iron to expand.'
        ],
        'quiz': [
            {
                'question': 'What were the dimensions of the largest known snowflake?',
                'options': ['10 inches wide, 5 inches thick', '12 inches wide, 6 inches thick', '15 inches wide, 8 inches thick', '20 inches wide, 10 inches thick'],
                'answer': '15 inches wide, 8 inches thick'
            },
            {
                'question': 'How long did the first commercial airline flight last?',
                'options': ['10 minutes', '15 minutes', '20 minutes', '23 minutes'],
                'answer': '23 minutes'
            },
            {
                'question': 'How much taller can the Eiffel Tower get during the summer?',
                'options': ['5 cm', '10 cm', '15 cm', '20 cm'],
                'answer': '15 cm'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and answer from the specified topic.
    """
    quiz_item = random.choice(topics[topic]['quiz'])
    return quiz_item['question'], quiz_item['options'], quiz_item['answer']

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    score = 0
    for i in range(3):
        question, options, answer = get_quiz_question(topic)
        print(f'Question {i+1}: {question}')
        for j, option in enumerate(options):
            print(f'{j+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if options[int(user_answer)-1] == answer:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect. The correct answer is: {answer}')
        print()
    print(f'Your final score: {score}/3')

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print('Welcome to the Interactive Knowledge App!')
    while True:
        print('\nSelect a topic:')
        for topic in topics:
            print(f'- {topic.capitalize()}')
        selected_topic = input('Enter your choice: ').lower()
        if selected_topic in topics:
            print(f'\nHere's a random fact about {selected_topic.capitalize()}:')
            print(get_random_fact(selected_topic))
            print('\nNow, let's test your knowledge with a quiz!')
            run_quiz(selected_topic)
        else:
            print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()