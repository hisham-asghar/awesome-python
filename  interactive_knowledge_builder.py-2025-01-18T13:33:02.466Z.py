import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'The first successful kidney transplant was performed in 1954.'
        ],
        'quiz': [
            {
                'question': 'What is the primary function of the human heart?',
                'options': ['a) To pump blood', 'b) To filter waste', 'c) To generate electricity', 'd) To produce hormones'],
                'answer': 'a'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['a) Mars', 'b) Saturn', 'c) Jupiter', 'd) Neptune'],
                'answer': 'c'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['a) Photosynthesis', 'b) Respiration', 'c) Transpiration', 'd) Evaporation'],
                'answer': 'a'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first programmable computer was the ENIAC, which was completed in 1946.',
            'The world's first text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the operating system developed by Apple?',
                'options': ['a) Windows', 'b) Linux', 'c) macOS', 'd) Android'],
                'answer': 'c'
            },
            {
                'question': 'What is the primary function of a computer's CPU?',
                'options': ['a) To store data', 'b) To generate graphics', 'c) To process information', 'd) To connect to the internet'],
                'answer': 'c'
            },
            {
                'question': 'What is the name of the protocol used for sending and receiving emails?',
                'options': ['a) HTTP', 'b) SMTP', 'c) FTP', 'd) TCP/IP'],
                'answer': 'b'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first successful powered flight, which took place in 1903?',
                'options': ['a) The Wright Flyer', 'b) The Kitty Hawk', 'c) The Biplane', 'd) The Glider'],
                'answer': 'a'
            },
            {
                'question': 'What was the name of the Roman emperor who ruled from 27 BC to 14 AD?',
                'options': ['a) Julius Caesar', 'b) Augustus', 'c) Nero', 'd) Caligula'],
                'answer': 'b'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['a) Mesopotamian', 'b) Sumerian', 'c) Phoenician', 'd) Pharaonic'],
                'answer': 'd'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2023 has 23 million digits.',
            'The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).',
            'The first person to circumnavigate the globe was Ferdinand Magellan.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['a) Atlantic Ocean', 'b) Indian Ocean', 'c) Arctic Ocean', 'd) Pacific Ocean'],
                'answer': 'd'
            },
            {
                'question': 'What is the name of the currency used in Japan?',
                'options': ['a) Euro', 'b) Dollar', 'c) Yen', 'd) Peso'],
                'answer': 'c'
            },
            {
                'question': 'What is the name of the largest land mammal?',
                'options': ['a) Elephant', 'b) Rhinoceros', 'c) Hippopotamus', 'd) Giraffe'],
                'answer': 'a'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_questions = topics[topic]['quiz']
    question = random.choice(quiz_questions)
    return question

def main():
    """
    Runs the interactive knowledge-building script.
    """
    print('Welcome to the Interactive Knowledge Builder!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'\nHere is a random fact about {selected_topic.capitalize()}:')
        print(get_random_fact(selected_topic))

        print('\nNow, let\'s test your knowledge with a quiz question!')
        quiz_question = get_quiz_question(selected_topic)
        print(quiz_question['question'])
        for option in quiz_question['options']:
            print(option)

        user_answer = input('Enter your answer (a, b, c, or d): ').lower()
        if user_answer == quiz_question['answer']:
            print('Correct! You've increased your knowledge.')
        else:
            print('Incorrect. The correct answer is:', quiz_question['options'][ord(quiz_question['answer']) - ord('a')])
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()