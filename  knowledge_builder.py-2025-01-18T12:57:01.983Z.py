import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The Milky Way galaxy contains over 200 billion stars.',
            'The largest known prime number has over 23 million digits.'
        ],
        'quiz': [
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
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial microprocessor, the Intel 4004, was released in 1971.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Android', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the digital currency that uses blockchain technology?',
                'options': ['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple'],
                'answer': 'Bitcoin'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Magna Carta, a landmark document in English history, was signed in 1215.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz': [
            {
                'question': 'What year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful vaccine developed by Edward Jenner?',
                'options': ['Smallpox', 'Polio', 'Measles', 'Influenza'],
                'answer': 'Smallpox'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The largest ocean on Earth is the Pacific Ocean.',
            'The longest river in the world is the Nile River.'
        ],
        'quiz': [
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the name of the largest continent on Earth?',
                'options': ['Asia', 'Africa', 'Europe', 'North America'],
                'answer': 'Asia'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
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
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question['question'], quiz_question['options']

def check_answer(topic, answer):
    """
    Checks if the user's answer is correct for the current quiz question.
    """
    quiz_question = random.choice(topics[topic]['quiz'])
    return answer == quiz_question['answer']

def main():
    """
    Runs the interactive knowledge-building script.
    """
    print('Welcome to the Knowledge Builder!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    user_topic = input('Enter your choice: ').lower()
    if user_topic not in topics:
        print('Invalid topic. Please try again.')
        return

    print(f'You have chosen the {user_topic.capitalize()} topic.')
    print(f'Here is a random fact: {get_random_fact(user_topic)}')

    print('Now, let\'s test your knowledge with a quiz!')
    question, options = get_quiz_question(user_topic)
    print(question)
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')

    user_answer = input('Enter your answer (1-4): ')
    if check_answer(user_topic, options[int(user_answer)-1]):
        print('Correct! You've increased your knowledge.')
    else:
        print('Incorrect. Better luck next time.')

if __name__ == '__main__':
    main()