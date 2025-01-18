import random
import requests
import json

def get_topic_menu():
    topics = {
        '1': 'Science',
        '2': 'Technology',
        '3': 'History',
        '4': 'General Knowledge',
    }
    return topics

def get_random_fact(topic):
    facts = {
        'Science': [
            'The human body contains enough iron to make a medium-sized nail.',
            'The first product to have a barcode was Wrigley's gum.',
            'A group of porcupines is called a prickle.'
        ],
        'Technology': [
            'The first computer mouse was made of wood.',
            'The first text message was sent on December 3, 1992.',
            'The first commercial jet flight took place in 1952.'
        ],
        'History': [
            'The Great Wall of China is the only man-made structure visible from space.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first president of the United States, George Washington, never lived in Washington, D.C.'
        ],
        'General Knowledge': [
            'Apples are more effective at waking you up in the morning than coffee.',
            'A group of pugs is called a grumble.',
            'The first product to have a barcode was Wrigley's gum.'
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    quiz = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'Which planet in our solar system is known as the Red Planet?', 'answers': ['Venus', 'Mars', 'Jupiter', 'Saturn'], 'correct': 1},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'answers': ['Photosynthesis', 'Respiration', 'Evaporation', 'Transpiration'], 'correct': 0}
        ],
        'Technology': [
            {'question': 'What is the name of the first commercially successful web browser?', 'answers': ['Internet Explorer', 'Mozilla Firefox', 'Netscape Navigator', 'Google Chrome'], 'correct': 2},
            {'question': 'Which company developed the first personal computer?', 'answers': ['Apple', 'Microsoft', 'IBM', 'HP'], 'correct': 2},
            {'question': 'What is the name of the programming language used to create the World Wide Web?', 'answers': ['Java', 'Python', 'HTML', 'C++'], 'correct': 2}
        ],
        'History': [
            {'question': 'In what year was the Declaration of Independence signed?', 'answers': ['1776', '1789', '1812', '1865'], 'correct': 0},
            {'question': 'Who was the first president of the United States?', 'answers': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'], 'correct': 2},
            {'question': 'Which ancient civilization is known for its pyramids?', 'answers': ['Roman', 'Greek', 'Egyptian', 'Mayan'], 'correct': 2}
        ],
        'General Knowledge': [
            {'question': 'What is the largest planet in our solar system?', 'answers': ['Earth', 'Mars', 'Jupiter', 'Saturn'], 'correct': 2},
            {'question': 'What is the currency used in Japan?', 'answers': ['Euro', 'Dollar', 'Yen', 'Peso'], 'correct': 2},
            {'question': 'Which of the following is not a primary color?', 'answers': ['Red', 'Blue', 'Green', 'Purple'], 'correct': 3}
        ]
    }
    return random.choice(quiz[topic])

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    topics = get_topic_menu()
    for key, value in topics.items():
        print(f'{key}. {value}')

    topic_choice = input('Enter your choice (1-4): ')
    if topic_choice in topics:
        selected_topic = topics[topic_choice]
        print(f'You have selected: {selected_topic}')
        print(get_random_fact(selected_topic))

        quiz_question = get_quiz_question(selected_topic)
        print(f'\nTest your knowledge with this quiz question:')
        print(quiz_question['question'])
        for i, answer in enumerate(quiz_question['answers']):
            print(f'{i+1}. {answer}')

        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == quiz_question['correct']:
            print('Correct! Well done.')
        else:
            print('Incorrect. Better luck next time.')
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()