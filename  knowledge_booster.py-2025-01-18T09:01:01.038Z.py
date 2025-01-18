import random
import requests
import json

# Define topics and their corresponding facts/quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'choices': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'choices': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'choices': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first domain name registered was Symbolics.com in 1985.',
            'The average person types 38 words per minute.'
        ],
        'quizzes': [
            {
                'question': 'What does "HTML" stand for?',
                'choices': ['Hyper Text Markup Language', 'Hyper Text Management Language', 'Hyper Text Modeling Language', 'Hyper Text Markup Logistics'],
                'answer': 'Hyper Text Markup Language'
            },
            {
                'question': 'Which company developed the Android operating system?',
                'choices': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first commercially available personal computer?',
                'choices': ['Apple I', 'IBM PC', 'Commodore 64', 'ENIAC'],
                'answer': 'Apple I'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'choices': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 'Mesopotamia'
            },
            {
                'question': 'Who was the first president of the United States?',
                'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event marked the start of World War I?',
                'choices': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 'The assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'choices': ['Mars', 'Saturn', 'Jupiter', 'Uranus'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Which of these is not a primary color?',
                'choices': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 'Green'
            },
            {
                'question': 'What is the rarest blood type?',
                'choices': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')
    return input('Enter your choice: ').lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f'Here is a random fact about {topic.capitalize()}:\n{fact}')

def run_quiz(topic):
    print(f'Let\'s test your {topic.capitalize()} knowledge!')
    score = 0
    for quiz in topics[topic]['quizzes']:
        print(quiz['question'])
        for i, choice in enumerate(quiz['choices']):
            print(f'{i+1}. {choice}')
        user_answer = input('Enter your answer (1-4): ')
        if quiz['choices'][int(user_answer)-1] == quiz['answer']:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect. The correct answer is: {quiz["answer"]}')
    print(f'Your final score is {score} out of {len(topics[topic]["quizzes"])}.')

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == '__main__':
    main()