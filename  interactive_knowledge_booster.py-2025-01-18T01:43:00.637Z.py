
import random
import requests
import json

# Define the available topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define the facts and quizzes for each topic
facts_and_quizzes = {
    'Science': [
        {
            'fact': 'The human body has around 60,000 miles of blood vessels.',
            'quiz': {
                'question': 'How many miles of blood vessels are in the human body?',
                'options': ['30,000', '60,000', '90,000', '120,000'],
                'answer': '60,000'
            }
        },
        {
            'fact': 'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'quiz': {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['She was born without them', 'It was the fashion in Renaissance Florence to shave them off', 'She lost them in an accident', 'The painter forgot to paint them'],
                'answer': 'It was the fashion in Renaissance Florence to shave them off'
            }
        }
    ],
    'Technology': [
        {
            'fact': 'The first electronic computer, ENIAC, was the size of a large room and weighed 30 tons.',
            'quiz': {
                'question': 'What was the size and weight of the first electronic computer, ENIAC?',
                'options': ['Small desktop, 10 lbs', 'Laptop-sized, 5 lbs', 'Room-sized, 30 tons', 'Car-sized, 1 ton'],
                'answer': 'Room-sized, 30 tons'
            }
        },
        {
            'fact': 'The first commercial computer program was written by Ada Lovelace in 1842 for the Analytical Engine, a general-purpose computer designed by Charles Babbage.',
            'quiz': {
                'question': 'Who wrote the first commercial computer program?',
                'options': ['Charles Babbage', 'Ada Lovelace', 'Alan Turing', 'Bill Gates'],
                'answer': 'Ada Lovelace'
            }
        }
    ],
    'History': [
        {
            'fact': 'The Great Wall of China is the only man-made structure visible from space.',
            'quiz': {
                'question': 'Which man-made structure is the only one visible from space?',
                'options': ['The Pyramids of Giza', 'The Eiffel Tower', 'The Great Wall of China', 'The Statue of Liberty'],
                'answer': 'The Great Wall of China'
            }
        },
        {
            'fact': 'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, which was 5 mph over the legal limit of the time.',
            'quiz': {
                'question': 'What was the first person convicted of speeding fined for?',
                'options': ['Driving at 8 mph in a 5 mph zone', 'Driving at 10 mph in a 5 mph zone', 'Driving at 15 mph in a 10 mph zone', 'Driving at 20 mph in a 15 mph zone'],
                'answer': 'Driving at 8 mph in a 5 mph zone'
            }
        }
    ],
    'General Knowledge': [
        {
            'fact': 'The first product to have a barcode was Wrigley's gum.',
            'quiz': {
                'question': 'What was the first product to have a barcode?',
                'options': ['Coca-Cola', 'Bread', 'Wrigley's gum', 'Eggs'],
                'answer': 'Wrigley's gum'
            }
        },
        {
            'fact': 'The King of Hearts is the only king without a mustache on a standard playing card.',
            'quiz': {
                'question': 'Which king on a standard playing card is the only one without a mustache?',
                'options': ['King of Diamonds', 'King of Clubs', 'King of Hearts', 'King of Spades'],
                'answer': 'King of Hearts'
            }
        }
    ]
}

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')

    for key, value in topics.items():
        print(f'{key}. {value}')

    topic_choice = input('Enter the number of the topic you want to explore: ')

    if topic_choice in topics:
        selected_topic = topics[topic_choice]
        print(f'You have chosen the topic of {selected_topic}.')

        # Fetch a random fact and quiz for the selected topic
        fact_and_quiz = random.choice(facts_and_quizzes[selected_topic])
        fact = fact_and_quiz['fact']
        quiz = fact_and_quiz['quiz']

        print(f'\nFact: {fact}')
        print(f'\nQuiz: {quiz["question"]}')

        for i, option in enumerate(quiz['options'], start=1):
            print(f'{i}. {option}')

        user_answer = input('Enter the number of your answer: ')

        if user_answer == quiz['answer']:
            print('Correct! You've increased your knowledge.')
        else:
            print('Incorrect. The correct answer is:', quiz['answer'])

    else:
        print('Invalid topic choice. Please try again.')

if __name__ == '__main__':
    main()
