import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'Bananas are slightly radioactive.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'Which element is the most abundant in the universe?',
                'options': ['Hydrogen', 'Helium', 'Oxygen', 'Carbon'],
                'answer': 'Hydrogen'
            },
            {
                'question': 'What is the process called when water changes from a liquid to a gas?',
                'options': ['Evaporation', 'Condensation', 'Sublimation', 'Precipitation'],
                'answer': 'Evaporation'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was called "The Creeper" and was created in 1971.',
            'The first text message was sent on December 3, 1992, and said "Merry Christmas".',
            'The first commercial smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What does "HTTP" stand for?',
                'options': ['Hyper Text Transfer Protocol', 'High-speed Transmission Technology Protocol', 'Hyperlink Transfer Protocol', 'Hyper Transmission Telecommunications Protocol'],
                'answer': 'Hyper Text Transfer Protocol'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Internet Explorer', 'Google Chrome', 'Mozilla Firefox', 'Mosaic'],
                'answer': 'Mosaic'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The first known written language was Sumerian cuneiform.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz': [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Franklin D. Roosevelt'],
                'answer': 'George Washington'
            },
            {
                'question': 'What year was the first successful powered flight by the Wright brothers?',
                'options': ['1903', '1912', '1919', '1928'],
                'answer': '1903'
            }
        ]
    },
    'general': {
        'facts': [
            'The first product to have a barcode was Wrigley's gum.',
            'Apples are more effective at waking you up in the morning than coffee.',
            'The first person convicted of speeding was going 8 mph.'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and options from the specified topic.
    """
    quiz = topics[topic]['quiz']
    question = random.choice(quiz)
    return question['question'], question['options'], question['answer']

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print('Welcome to the Interactive Knowledge App!')

    while True:
        print('\nSelect a topic:')
        for topic in topics:
            print(f'- {topic.capitalize()}')
        print('- Quit')

        user_input = input('Enter your choice: ').lower()

        if user_input == 'quit':
            print('Goodbye!')
            break

        if user_input in topics:
            print('\nHere is a random fact about', user_input.capitalize() + ':')
            print(get_random_fact(user_input))

            print('\nNow, let\'s test your knowledge with a quiz!')
            question, options, answer = get_quiz_question(user_input)
            print(question)
            for i, option in enumerate(options):
                print(f'{i+1}. {option}')

            user_answer = input('Enter your answer (1-4): ')
            if options[int(user_answer) - 1] == answer:
                print('Correct!')
            else:
                print('Incorrect. The correct answer is:', answer)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()