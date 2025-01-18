Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Function to display a random fact or concept from the chosen topic
def display_fact(topic):
    if topic == '1':  # Science
        response = requests.get('https://api.api-ninjas.com/v1/science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        print(f'Random Science Fact: {data[0]["fact"]}')
    elif topic == '2':  # Technology
        response = requests.get('https://api.api-ninjas.com/v1/technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        print(f'Random Technology Fact: {data[0]["fact"]}')
    elif topic == '3':  # History
        response = requests.get('https://api.api-ninjas.com/v1/historicalevents', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        print(f'Random Historical Event: {data[0]["event"]}')
    elif topic == '4':  # General Knowledge
        response = requests.get('https://api.api-ninjas.com/v1/trivia', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        print(f'Random General Knowledge Fact: {data[0]["question"]}')
    else:
        print('Invalid topic selection.')

# Function to run the interactive quiz
def run_quiz(topic):
    if topic == '1':  # Science
        questions = [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'What is the largest planet in our solar system?', 'answers': ['Earth', 'Mars', 'Jupiter', 'Saturn'], 'correct': 2},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'answers': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'], 'correct': 0}
        ]
    elif topic == '2':  # Technology
        questions = [
            {'question': 'What is the primary function of a computer processor (CPU)?', 'answers': ['Storage', 'Input', 'Processing', 'Output'], 'correct': 2},
            {'question': 'What is the purpose of a web browser?', 'answers': ['Sending emails', 'Playing music', 'Accessing websites', 'Editing documents'], 'correct': 2},
            {'question': 'What is the name of the first commercially successful smartphone?', 'answers': ['iPhone', 'Android', 'Blackberry', 'Nokia'], 'correct': 0}
        ]
    elif topic == '3':  # History
        questions = [
            {'question': 'Which ancient civilization is known for building the pyramids?', 'answers': ['Mesopotamia', 'Indus Valley', 'Egypt', 'China'], 'correct': 2},
            {'question': 'In what year did World War II end?', 'answers': ['1945', '1939', '1918', '1955'], 'correct': 0},
            {'question': 'Who was the first president of the United States?', 'answers': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'], 'correct': 2}
        ]
    elif topic == '4':  # General Knowledge
        questions = [
            {'question': 'What is the capital city of Australia?', 'answers': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'correct': 3},
            {'question': 'What is the largest ocean on Earth?', 'answers': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'], 'correct': 3},
            {'question': 'Which planet in our solar system is known as the "Red Planet"?', 'answers': ['Venus', 'Mars', 'Jupiter', 'Saturn'], 'correct': 1}
        ]
    else:
        print('Invalid topic selection.')
        return

    score = 0
    for question in questions:
        print(question['question'])
        for i, answer in enumerate(question['answers']):
            print(f"{i+1}. {answer}")
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == question['correct']:
            print('Correct!')
            score += 1
        else:
            print('Incorrect.')
    print(f'Your final score is {score} out of {len(questions)}.')

# Main program loop
while True:
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic = input('Enter the number of the topic (or "q" to quit): ')
    if topic.lower() == 'q':
        break
    if topic in topics:
        display_fact(topic)
        run_quiz(topic)
    else:
        print('Invalid topic selection. Please try again.')