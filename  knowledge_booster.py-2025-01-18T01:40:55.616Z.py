
import random
import requests
import json

# List of available topics
topics = ['Science', 'Technology', 'History', 'General Knowledge']

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for i, topic in enumerate(topics):
        print(f'{i+1}. {topic}')
    
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            if 1 <= choice <= len(topics):
                return choice - 1
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_index):
    # Fetch data from a public API or a predefined database
    if topic_index == 0:  # Science
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic_index == 1:  # Technology
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic_index == 2:  # History
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY'})
    else:  # General Knowledge
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY'})
    
    if response.status_code == 200:
        facts = response.json()
        return random.choice(facts)['fact']
    else:
        return 'Error fetching data.'

# Function to display a random fact or concept and a multiple-choice quiz
def run_quiz(topic_index):
    # Fetch a random fact or concept
    fact = get_random_fact(topic_index)
    print(f'Random fact or concept about {topics[topic_index]}:')
    print(fact)
    print()
    
    # Generate a multiple-choice quiz
    questions = [
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['Mars', 'Jupiter', 'Saturn', 'Earth'],
            'answer': 1
        },
        {
            'question': 'What is the capital city of France?',
            'options': ['London', 'Berlin', 'Paris', 'Rome'],
            'answer': 2
        },
        {
            'question': 'Which of these is not a programming language?',
            'options': ['Python', 'Java', 'C++', 'Excel'],
            'answer': 3
        }
    ]
    
    # Display the quiz questions
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                user_answer = int(input('Enter your answer (1-4): '))
                if 1 <= user_answer <= len(question['options']):
                    if user_answer - 1 == question['answer']:
                        print('Correct!')
                    else:
                        print('Incorrect. Better luck next time!')
                    break
                else:
                    print('Invalid choice. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')

# Main function
def main():
    topic_choice = display_menu()
    run_quiz(topic_choice)

if __name__ == '__main__':
    main()
