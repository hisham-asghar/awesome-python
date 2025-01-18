
import random
import requests
import json

def get_topic_menu():
    return {
        '1': 'Science',
        '2': 'Technology',
        '3': 'History',
        '4': 'General Knowledge',
        '5': 'Exit'
    }

def get_random_fact(topic):
    facts = {
        'Science': [
            'The human body contains enough iron to make a medium-sized nail.',
            'The first product to have a barcode was Wrigley's gum.',
            'Cats have fewer toes on their back paws than their front paws.'
        ],
        'Technology': [
            'The first computer mouse was made of wood.',
            'The first text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'History': [
            'The Great Wall of China is the only man-made structure visible from space.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'General Knowledge': [
            'A group of porcupines is called a prickle.',
            'Apples are more effective at waking you up in the morning than coffee.',
            'The first novel ever written was The Tale of Genji, by Japanese author Murasaki Shikibu, in the 11th century.'
        ]
    }
    return random.choice(facts[topic])

def get_quiz_questions(topic):
    quiz_questions = {
        'Science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ],
        'Technology': [
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Internet Explorer', 'Google Chrome', 'Mozilla Firefox', 'Mosaic'],
                'answer': 'Mosaic'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first successful mobile phone call made in 1973?',
                'options': ['iPhone', 'Android', 'Motorola DynaTAC 8000x', 'Nokia 3310'],
                'answer': 'Motorola DynaTAC 8000x'
            }
        ],
        'History': [
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'In what year did the Berlin Wall fall?',
                'options': ['1989', '1991', '1993', '1995'],
                'answer': '1989'
            },
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Aztecs', 'Incas', 'Mayans', 'Egyptians'],
                'answer': 'Egyptians'
            }
        ],
        'General Knowledge': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            }
        ]
    }
    return random.sample(quiz_questions[topic], 3)

def run_quiz(quiz_questions):
    score = 0
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_questions)}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        topic_menu = get_topic_menu()
        for key, value in topic_menu.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break
        elif choice in topic_menu:
            topic = topic_menu[choice]
            print(f"\nRandom fact about {topic}: {get_random_fact(topic)}")
            quiz_questions = get_quiz_questions(topic)
            run_quiz(quiz_questions)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
