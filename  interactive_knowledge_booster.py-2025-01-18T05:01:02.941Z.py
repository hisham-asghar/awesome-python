import random
import requests
import json

# Dictionary to store topics and their corresponding facts and questions
topics = {
    'science': {
        'facts': [
            'The human body has more than 600 muscles.',
            'The Earth is the only planet in our solar system with liquid water on its surface.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'questions': [
            {
                'question': 'What is the primary function of the human heart?',
                'options': ['A. To pump blood', 'B. To regulate breathing', 'C. To digest food', 'D. To produce energy'],
                'answer': 'A'
            },
            {
                'question': 'Which of the following is not a state of matter?',
                'options': ['A. Solid', 'B. Liquid', 'C. Gas', 'D. Plasma'],
                'answer': 'C'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['A. Photosynthesis', 'B. Respiration', 'C. Evaporation', 'D. Combustion'],
                'answer': 'A'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The first commercial email service was launched in 1971 by Ray Tomlinson.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['A. Java', 'B. C++', 'C. Python', 'D. Ruby'],
                'answer': 'C'
            },
            {
                'question': 'Which technology company was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne?',
                'options': ['A. Microsoft', 'B. Google', 'C. Amazon', 'D. Apple'],
                'answer': 'D'
            },
            {
                'question': 'What is the name of the process by which computers and other electronic devices communicate with each other?',
                'options': ['A. Networking', 'B. Coding', 'C. Programming', 'D. Encryption'],
                'answer': 'A'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in ancient Greece in 776 BC.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'questions': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['A. Abraham Lincoln', 'B. Thomas Jefferson', 'C. George Washington', 'D. John Adams'],
                'answer': 'C'
            },
            {
                'question': 'In what year did the Berlin Wall fall?',
                'options': ['A. 1989', 'B. 1991', 'C. 1995', 'D. 2001'],
                'answer': 'A'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['A. Mesopotamians', 'B. Mayans', 'C. Incas', 'D. Egyptians'],
                'answer': 'D'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest mammal in the world is the giraffe.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'questions': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
                'answer': 'D'
            },
            {
                'question': 'Which of the following is not a primary color?',
                'options': ['A. Red', 'B. Blue', 'C. Yellow', 'D. Green'],
                'answer': 'D'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['A. Titan', 'B. Ganymede', 'C. Callisto', 'D. Io'],
                'answer': 'A'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_random_quiz_question(topic):
    question = random.choice(topics[topic]['questions'])
    return question

def run_quiz(topic):
    question = get_random_quiz_question(topic)
    print(question['question'])
    for option in question['options']:
        print(option)
    user_answer = input('Enter your answer (A, B, C, or D): ')
    if user_answer.upper() == question['answer']:
        print('Correct!')
    else:
        print('Incorrect. The correct answer is', question['answer'])

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    selected_topic = input('Enter your choice: ').lower()
    if selected_topic in topics:
        print(f'Random fact about {selected_topic.capitalize()}:')
        print(get_random_fact(selected_topic))
        print(f'Now, let\'s test your {selected_topic.capitalize()} knowledge with a quiz!')
        run_quiz(selected_topic)
    else:
        print('Invalid topic. Please try again.')

if __name__ == '__main__':
    main()