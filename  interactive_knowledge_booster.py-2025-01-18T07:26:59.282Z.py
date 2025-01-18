import random
import requests
import json

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General Knowledge')
    print('5. Quit')

def get_random_fact(topic):
    facts = {
        'Science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Sharks have been around for over 400 million years, predating the dinosaurs.'
        ],
        'Technology': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'History': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza were built over a period of 20 years, with an estimated 100,000 workers.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.'
        ],
        'General Knowledge': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 20 feet tall.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ]
    }
    return random.choice(facts[topic])

def run_quiz(topic):
    quiz_questions = {
        'Science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            }
        ],
        'Technology': [
            {
                'question': 'What year was the first mobile phone call made?',
                'options': ['1973', '1983', '1993', '2003'],
                'answer': '1973'
            },
            {
                'question': 'What is the name of the first electronic computer?',
                'options': ['ENIAC', 'UNIVAC', 'MARK I', 'COLOSSUS'],
                'answer': 'ENIAC'
            }
        ],
        'History': [
            {
                'question': 'In what year were the first Olympic Games held?',
                'options': ['776 BC', '500 BC', '200 BC', '100 AD'],
                'answer': '776 BC'
            },
            {
                'question': 'How many years did it take to build the Pyramids of Giza?',
                'options': ['10 years', '20 years', '50 years', '100 years'],
                'answer': '20 years'
            }
        ],
        'General Knowledge': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Brain', 'Heart', 'Liver', 'Skin'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic', 'Indian', 'Arctic', 'Pacific'],
                'answer': 'Pacific'
            }
        ]
    }

    score = 0
    for question in quiz_questions[topic]:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')
        user_answer = input('Enter your answer (1-4): ')
        if question['options'][int(user_answer) - 1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f'Your final score is {score} out of {len(quiz_questions[topic])}.')

def main():
    while True:
        display_menu()
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            print(get_random_fact('Science'))
            run_quiz('Science')
        elif choice == '2':
            print(get_random_fact('Technology'))
            run_quiz('Technology')
        elif choice == '3':
            print(get_random_fact('History'))
            run_quiz('History')
        elif choice == '4':
            print(get_random_fact('General Knowledge'))
            run_quiz('General Knowledge')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()