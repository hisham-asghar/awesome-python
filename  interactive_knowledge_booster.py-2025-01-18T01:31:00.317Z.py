
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

# Function to display the menu and get user input
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f'{key}. {value}')
    return input('Enter the number of your chosen topic: ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == '1':
        # Fetch a random science fact using an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '2':
        # Fetch a random technology fact using an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '3':
        # Fetch a random history fact using an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact using an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    else:
        return 'Invalid topic selection.'

# Function to display the quiz and get user answers
def take_quiz(topic):
    if topic == '1':
        # Fetch science quiz questions and answers from a predefined database or API
        quiz_data = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system is known as the "Red Planet"?',
                'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
                'answer': 'Mars'
            },
            # Add more science quiz questions here
        ]
    elif topic == '2':
        # Fetch technology quiz questions and answers from a predefined database or API
        quiz_data = [
            {
                'question': 'What does "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Charge Processing Unit', 'Chip Processing Unit'],
                'answer': 'Central Processing Unit'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            # Add more technology quiz questions here
        ]
    elif topic == '3':
        # Fetch history quiz questions and answers from a predefined database or API
        quiz_data = [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            # Add more history quiz questions here
        ]
    elif topic == '4':
        # Fetch general knowledge quiz questions and answers from a predefined database or API
        quiz_data = [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'India', 'Korea'],
                'answer': 'Japan'
            },
            # Add more general knowledge quiz questions here
        ]
    else:
        return 'Invalid topic selection.'

    # Shuffle the quiz questions
    random.shuffle(quiz_data)

    # Display the quiz and get user answers
    score = 0
    for question in quiz_data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter the number of your answer: ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_data)}.")

# Main function to run the interactive knowledge booster
def main():
    topic = display_menu()
    print(get_random_fact(topic))
    take_quiz(topic)

if __name__ == "__main__":
    main()
