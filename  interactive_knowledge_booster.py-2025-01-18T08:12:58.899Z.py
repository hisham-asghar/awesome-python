
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

# Define the trivia questions and answers for each topic
trivia_data = {
    'Science': [
        {
            'question': 'What is the largest planet in our solar system?',
            'choices': ['Jupiter', 'Saturn', 'Neptune', 'Uranus'],
            'answer': 'Jupiter'
        },
        {
            'question': 'What is the process by which plants convert sunlight into energy?',
            'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
            'answer': 'Photosynthesis'
        },
        # Add more science trivia questions here
    ],
    'Technology': [
        {
            'question': 'What is the name of the first computer programmer?',
            'choices': ['Ada Lovelace', 'Charles Babbage', 'Alan Turing', 'Grace Hopper'],
            'answer': 'Ada Lovelace'
        },
        {
            'question': 'What is the name of the programming language created by Guido van Rossum?',
            'choices': ['Java', 'C++', 'Python', 'Ruby'],
            'answer': 'Python'
        },
        # Add more technology trivia questions here
    ],
    'History': [
        {
            'question': 'In what year did the American Civil War begin?',
            'choices': ['1861', '1865', '1775', '1812'],
            'answer': '1861'
        },
        {
            'question': 'Who was the first president of the United States?',
            'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
            'answer': 'George Washington'
        },
        # Add more history trivia questions here
    ],
    'General Knowledge': [
        {
            'question': 'What is the capital city of Australia?',
            'choices': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
            'answer': 'Canberra'
        },
        {
            'question': 'What is the largest ocean on Earth?',
            'choices': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
            'answer': 'Pacific Ocean'
        },
        # Add more general knowledge trivia questions here
    ]
}

def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')

def get_random_fact(topic):
    # Fetch a random fact or concept from a public API or predefined database
    # (This example uses a predefined database)
    facts = {
        'Science': 'The human body has around 60,000 miles of blood vessels.',
        'Technology': 'The first electronic computer, ENIAC, was completed in 1946.',
        'History': 'The Great Wall of China is the longest man-made structure in the world.',
        'General Knowledge': 'The tallest mammal is the giraffe.'
    }
    return facts[topic]

def run_quiz(topic):
    print(f'Welcome to the {topic} Quiz!')
    print('Answer the following multiple-choice questions:')

    # Select a random trivia question from the topic
    trivia_question = random.choice(trivia_data[topic])
    question = trivia_question['question']
    choices = trivia_question['choices']
    answer = trivia_question['answer']

    # Display the question and choices
    print(question)
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')

    # Get the user's answer
    user_answer = input('Enter your answer (1-4): ')

    # Check the user's answer and provide feedback
    if choices[int(user_answer)-1] == answer:
        print('Correct! You're a knowledge master!')
    else:
        print(f'Incorrect. The correct answer is {answer}.')

def main():
    display_menu()
    topic_choice = input('Enter the number of the topic you want to explore: ')

    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f'You've chosen {topic}. Here's a random fact:')
        print(get_random_fact(topic))
        print()
        run_quiz(topic)
    else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
