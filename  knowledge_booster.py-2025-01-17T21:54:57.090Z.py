
import random
import requests
import json

# List of available topics
topics = ['Science', 'Technology', 'History', 'General Knowledge']

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic}')
    choice = int(input('Enter your choice (1-4): '))
    return choice

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    # Fetch data from a public API or predefined database
    # For this example, we'll use a simple dictionary
    facts = {
        'Science': 'The human body has around 60,000 miles of blood vessels.',
        'Technology': 'The first computer mouse was invented in 1964 by Douglas Engelbart.',
        'History': 'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
        'General Knowledge': 'A group of flamingos is called a flamboyance.'
    }
    return facts[topic]

# Function to display the random fact or concept
def display_fact(topic):
    fact = get_random_fact(topic)
    print(f'Did you know? {fact}')

# Function to display the quiz and get the user's answer
def take_quiz(topic):
    # Fetch quiz questions and answers from a public API or predefined database
    # For this example, we'll use a simple dictionary
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 0},
            {'question': 'What is the largest planet in our solar system?', 'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'], 'answer': 2}
        ],
        'Technology': [
            {'question': 'Which company created the first personal computer?', 'options': ['Apple', 'IBM', 'Microsoft', 'Commodore'], 'answer': 1},
            {'question': 'What is the name of the programming language created by Guido van Rossum?', 'options': ['Java', 'C++', 'Python', 'Ruby'], 'answer': 2}
        ],
        'History': [
            {'question': 'Which ancient civilization built the pyramids?', 'options': ['Aztecs', 'Incas', 'Egyptians', 'Romans'], 'answer': 2},
            {'question': 'In what year did World War II end?', 'options': ['1945', '1939', '1941', '1950'], 'answer': 0}
        ],
        'General Knowledge': [
            {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'], 'answer': 1},
            {'question': 'What is the capital city of Australia?', 'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'answer': 3}
        ]
    }

    # Select a random quiz from the chosen topic
    quiz = random.choice(quizzes[topic])

    # Display the quiz question and options
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = int(input('Enter your answer (1-4): '))

    # Check if the user's answer is correct
    if user_answer - 1 == quiz['answer']:
        print('Correct! You're awesome.')
    else:
        print('Oops, that's not the right answer. Better luck next time!')

# Main program loop
while True:
    choice = display_menu()
    topic = topics[choice - 1]
    display_fact(topic)
    take_quiz(topic)
    again = input('Would you like to try another topic? (y/n) ')
    if again.lower() != 'y':
        break

print('Thank you for using the Interactive Knowledge Booster. Have a great day!')
