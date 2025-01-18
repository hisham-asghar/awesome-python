import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Cats have fewer toes on their back paws than their front paws.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the force that keeps planets in orbit around the Sun?',
                'options': ['Gravity', 'Magnetism', 'Friction', 'Centrifugal force'],
                'answer': 0
            },
            {
                'question': 'Which of the following is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 3
            },
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Water vapor'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real bug (a moth) trapped in a Harvard Mark II computer.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The world\'s first text message was sent on December 3, 1992, and said "Merry Christmas".'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first computer programmer?',
                'options': ['Ada Lovelace', 'Alan Turing', 'Charles Babbage', 'Grace Hopper'],
                'answer': 0
            },
            {
                'question': 'What is the name of the software that controls the basic functions of a computer?',
                'options': ['Firmware', 'Operating system', 'Drivers', 'Utilities'],
                'answer': 1
            },
            {
                'question': 'Which of the following is not a type of computer memory?',
                'options': ['RAM', 'ROM', 'CPU', 'SSD'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first electric traffic light was installed in Cleveland, Ohio, in 1914.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 1
            },
            {
                'question': 'Which event marked the beginning of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Invasion of Poland', 'Attack on Pearl Harbor', 'Cuban Missile Crisis'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The largest known snowflake was 15 inches wide, found in Montana in 1887.',
            'The longest word in the English language is "pneumonoultramicroscopicsilicovolcanoconiosis".'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 0
            },
            {
                'question': 'What is the name of the tallest mammal on Earth?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 1
            },
            {
                'question': 'Which of the following is not a primary color?',
                'options': ['Red', 'Blue', 'Green', 'Yellow'],
                'answer': 2
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def check_answer(topic, question_index, user_answer):
    correct_answer = topics[topic]['quiz'][question_index]['answer']
    return user_answer == correct_answer

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic in topics:
        print(f'\nHere is a random fact about {selected_topic.capitalize()}:')
        print(get_random_fact(selected_topic))

        print('\nTime for a quiz! Answer the following multiple-choice questions:')
        score = 0
        for _ in range(3):
            quiz_question = get_quiz_question(selected_topic)
            print(f"\nQuestion: {quiz_question['question']}")
            for i, option in enumerate(quiz_question['options']):
                print(f"{i+1}. {option}")
            user_answer = int(input('Enter your answer (1-4): ')) - 1
            if check_answer(selected_topic, _, user_answer):
                print('Correct!')
                score += 1
            else:
                print('Incorrect. Better luck next time!')
        print(f'\nYour final score is {score} out of 3.')
    else:
        print(f'Sorry, "{selected_topic.capitalize()}" is not a valid topic. Please try again.')

if __name__ == '__main__':
    main()