import random
import requests
import json

# Define the topics and their respective facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'A single bolt of lightning can reach temperatures of up to 54,000°F (30,000°C).'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Stephen Hawking'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Uranus'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the company that created the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BC, making them over 4,500 years old.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quizzes': [
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'In what year did World War II end?',
                'options': ['1945', '1939', '1918', '1955'],
                'answer': '1945'
            },
            {
                'question': 'What was the name of the ancient civilization that built the Colosseum in Rome?',
                'options': ['Aztec', 'Inca', 'Greek', 'Roman'],
                'answer': 'Roman'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.',
            'The fastest land animal is the cheetah, which can reach speeds of up to 75 mph (120 km/h).'
        ],
        'quizzes': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon', 'Nile', 'Mississippi', 'Yangtze'],
                'answer': 'Nile'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_random_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if quiz['options'][int(user_answer)-1] == quiz['answer']:
                print("Correct!")
                return True
            else:
                print("Incorrect. Try again.")
        else:
            print("Invalid input. Please try again.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your choice: ").lower()
        if user_topic in topics:
            print(f"\nHere's a random fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            
            print("\nNow, let's test your knowledge with a quiz!")
            quiz = get_random_quiz(user_topic)
            if run_quiz(quiz):
                print("\nGreat job! You got the answer right.")
            else:
                print("\nOops, better luck next time.")
            
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()