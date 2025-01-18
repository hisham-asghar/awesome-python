
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    return input('Enter your choice (1-4): ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == '1':
        # Fetch a random science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '2':
        # Fetch a random technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '3':
        # Fetch a random history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    else:
        return 'Invalid topic selected.'

# Function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    if topic == '1':
        # Science quiz
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            # Add more science quiz questions here
        ]
    elif topic == '2':
        # Technology quiz
        questions = [
            {
                'question': 'What is the primary function of a computer processor (CPU)?',
                'options': ['Storage', 'Input/Output', 'Processing', 'Networking'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Internet Explorer', 'Netscape Navigator', 'Google Chrome', 'Mozilla Firefox'],
                'answer': 1
            },
            # Add more technology quiz questions here
        ]
    elif topic == '3':
        # History quiz
        questions = [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Chinese'],
                'answer': 2
            },
            {
                'question': 'What year did World War II end?',
                'options': ['1945', '1939', '1941', '1950'],
                'answer': 0
            },
            # Add more history quiz questions here
        ]
    elif topic == '4':
        # General knowledge quiz
        questions = [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 3
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            # Add more general knowledge quiz questions here
        ]
    else:
        return 'Invalid topic selected.'

    # Display the quiz questions and get the user's answers
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == question['answer']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect.')
    print(f'Your score: {score}/{len(questions)}')

# Main function to run the interactive knowledge booster
def main():
    while True:
        topic_choice = display_menu()
        if topic_choice in topics:
            print(f"\nHere's a random fact about {topics[topic_choice]}:")
            print(get_random_fact(topic_choice))
            print("\nNow, let's test your knowledge!")
            quiz(topic_choice)
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
