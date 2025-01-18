Here is the raw Python code without any additional commentary:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.'
        ],
        'quiz': [
            {
                'question': 'Which of the following is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the name of the nearest star to Earth?',
                'options': ['Proxima Centauri', 'Sirius', 'Betelgeuse', 'Polaris'],
                'answer': 'Proxima Centauri'
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Brain\", was created in 1986.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The internet was originally called ARPANET, which was created in 1969.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the first programmable computer?',
                'options': ['ENIAC', 'UNIVAC', 'Z1', 'Babbage Difference Engine'],
                'answer': 'ENIAC'
            },
            {
                'question': 'Which company developed the first commercial web browser?',
                'options': ['Microsoft', 'Apple', 'Netscape', 'Google'],
                'answer': 'Netscape'
            },
            {
                'question': 'What is the name of the first social media platform?',
                'options': ['MySpace', 'Facebook', 'Twitter', 'Friendster'],
                'answer': 'Friendster'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The ancient Egyptians were the first civilization to invent the 365-day calendar.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Mayan', 'Egyptian'],
                'answer': 'Egyptian'
            },
            {
                'question': 'What was the name of the first successful voyage around the world?',
                'options': ['Christopher Columbus', 'Magellan', 'Vasco da Gama', 'Leif Erikson'],
                'answer': 'Magellan'
            },
            {
                'question': 'Which country was the first to industrialize?',
                'options': ['United States', 'United Kingdom', 'Germany', 'France'],
                'answer': 'United Kingdom'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest mammal is the giraffe, which can reach heights of up to 6 meters.',
            'The world's largest desert is the Sahara, covering an area of 3.6 million square miles.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    print('- Quit')

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def run_quiz(topic):
    quiz_questions = topics[topic]['quiz']
    score = 0
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input('Enter your answer (1-4): '))
        if question['options'][user_answer-1] == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The correct answer is:', question['answer'])
    print(f"Your final score is {score} out of {len(quiz_questions)}")

def main():
    while True:
        display_menu()
        user_choice = input('Enter your choice: ').lower()
        if user_choice == 'quit':
            print('Goodbye!')
            break
        elif user_choice in topics:
            print(get_random_fact(user_choice))
            run_quiz(user_choice)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()