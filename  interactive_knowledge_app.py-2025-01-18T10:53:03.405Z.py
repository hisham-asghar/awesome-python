import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Cats have better low-light vision than humans, thanks to a reflective layer in their eyes called the tapetum lucidum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 1
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Condensation'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The world's first programmable computer was the ENIAC, which was completed in 1946.',
            'The first email was sent by Ray Tomlinson in 1971.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the software that allows you to browse the internet?',
                'options': ['Browser', 'Search engine', 'Operating system', 'Antivirus'],
                'answer': 0
            },
            {
                'question': 'Which of these is a type of computer memory?',
                'options': ['RAM', 'CPU', 'Motherboard', 'Keyboard'],
                'answer': 0
            },
            {
                'question': 'What is the name of the programming language used to create websites?',
                'options': ['Python', 'Java', 'C++', 'HTML'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first computer programmer was Ada Lovelace, a 19th-century mathematician.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 1
            },
            {
                'question': 'Which event marked the end of the Roman Empire?',
                'options': ['The fall of Constantinople', 'The French Revolution', 'The American Civil War', 'The Industrial Revolution'],
                'answer': 0
            },
            {
                'question': 'Which famous explorer is credited with discovering America?',
                'options': ['Christopher Columbus', 'Marco Polo', 'Vasco da Gama', 'Ferdinand Magellan'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 3
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Green', 'Purple'],
                'answer': 3
            },
            {
                'question': 'What is the largest mammal in the world?',
                'options': ['Elephant', 'Whale', 'Giraffe', 'Hippopotamus'],
                'answer': 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question['question'], quiz_question['options'], quiz_question['answer']

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print('Welcome to the Interactive Knowledge App!')
    print('Please select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General')

    topic_choice = input('Enter the number of the topic (1-4): ')

    if topic_choice == '1':
        topic = 'science'
    elif topic_choice == '2':
        topic = 'technology'
    elif topic_choice == '3':
        topic = 'history'
    elif topic_choice == '4':
        topic = 'general'
    else:
        print('Invalid choice. Exiting the app.')
        return

    print(f'\nYou selected the {topic.capitalize()} topic.')
    print(f'Here is a random fact: {get_random_fact(topic)}')

    print('\nTime for a quiz! Answer the following multiple-choice question:')
    question, options, answer = get_quiz_question(topic)
    print(question)
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')

    user_answer = input('Enter the number of your answer (1-4): ')
    if int(user_answer) == answer + 1:
        print('Correct! You've increased your knowledge.')
    else:
        print('Incorrect. Better luck next time.')

if __name__ == '__main__':
    main()