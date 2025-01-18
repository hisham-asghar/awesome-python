import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'choices': ['Titan', 'Ganymede', 'Callisto', 'Io'],
                'answer': 0
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'choices': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 1
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Creeper\", was created in 1971.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The largest hard drive ever made had a capacity of 60 terabytes.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'choices': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'Which company is known for creating the Android operating system?',
                'choices': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first successful web browser?',
                'choices': ['Mosaic', 'Netscape Navigator', 'Internet Explorer', 'Safari'],
                'answer': 1
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was stolen from the Louvre museum in Paris in 1911 and recovered two years later.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'choices': ['Aztecs', 'Incas', 'Egyptians', 'Mayans'],
                'answer': 2
            },
            {
                'question': 'Who was the first president of the United States?',
                'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'James Madison'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'choices': ['The Flyer', 'The Kitty Hawk', 'The Wright Flyer', 'The Aeroplane'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has over 23 million digits.',
            'The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).',
            'The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis, a type of lung disease.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'choices': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'choices': ['A', 'B', 'AB', 'O'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'choices': ['Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, choice in enumerate(quiz['choices']):
        print(f"{i+1}. {choice}")
    
    while True:
        try:
            user_answer = int(input('Enter your answer (1-4): '))
            if user_answer >= 1 and user_answer <= 4:
                if user_answer - 1 == quiz['answer']:
                    print('Correct!')
                    return True
                else:
                    print('Incorrect. Try again.')
            else:
                print('Invalid input. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4.')

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    
    while True:
        user_topic = input('Enter your choice: ').lower()
        if user_topic in topics:
            print(f'Random fact about {user_topic.capitalize()}: {get_random_fact(user_topic)}')
            quiz = get_quiz(user_topic)
            if run_quiz(quiz):
                print('Congratulations! You got the answer right.')
            else:
                print('Better luck next time.')
            break
        else:
            print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()