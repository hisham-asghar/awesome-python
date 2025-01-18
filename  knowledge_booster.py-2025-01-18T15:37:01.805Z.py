import random
import requests
import json

# Define topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Marie Curie', 'Stephen Hawking'],
                'answer': 1
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quizzes': [
            {
                'question': 'What does "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'High-Tech Multimedia Language', 'Hyper Text Machine Language', 'Hyper Textual Markup Language'],
                'answer': 0
            },
            {
                'question': 'Which company developed the first commercially successful graphical user interface (GUI)?',
                'options': ['Apple', 'Microsoft', 'Xerox', 'IBM'],
                'answer': 2
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamian', 'Egyptian', 'Greek', 'Chinese'],
                'answer': 2
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'Which event marked the end of World War II?',
                'options': ['D-Day', 'Pearl Harbor', 'Hiroshima and Nagasaki bombings', 'V-E Day'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
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
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    while True:
        try:
            user_answer = int(input('Enter your answer (1-4): '))
            if 1 <= user_answer <= 4:
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
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input('Enter your topic choice: ').lower()
        if user_topic in topics:
            break
        else:
            print('Invalid topic. Please try again.')
    
    print(f"\nHere's a random fact about {user_topic.capitalize()}:")
    print(get_random_fact(user_topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz = get_quiz(user_topic)
    if run_quiz(quiz):
        print("Congratulations, you got it right!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()