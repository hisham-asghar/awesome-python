
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    1: 'Science',
    2: 'Technology',
    3: 'History',
    4: 'General Knowledge'
}

topic_api_endpoints = {
    'Science': 'https://api.api-ninjas.com/v1/facts?category=science',
    'Technology': 'https://api.api-ninjas.com/v1/facts?category=technology',
    'History': 'https://api.api-ninjas.com/v1/facts?category=history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Function to display the menu and get user's topic choice
def display_menu():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            if choice in topics:
                return topics[choice]
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_endpoint = topic_api_endpoints[topic]
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    headers = {'X-Api-Key': api_key}
    
    try:
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()
        facts = response.json()
        return random.choice(facts)['fact']
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return 'Sorry, unable to fetch a fact at this time.'

# Function to display a multiple-choice quiz
def display_quiz(topic):
    # Define the quiz questions and answers for the selected topic
    quiz_data = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'What is the largest planet in our solar system?', 'answers': ['Mars', 'Jupiter', 'Saturn', 'Neptune'], 'correct': 1},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'answers': ['Respiration', 'Photosynthesis', 'Evaporation', 'Combustion'], 'correct': 1}
        ],
        'Technology': [
            {'question': 'What is the name of the first computer programmer?', 'answers': ['Alan Turing', 'Charles Babbage', 'Ada Lovelace', 'Steve Jobs'], 'correct': 2},
            {'question': 'What is the primary function of a web browser?', 'answers': ['To send emails', 'To play games', 'To display websites', 'To write code'], 'correct': 2},
            {'question': 'What is the name of the first commercially successful smartphone?', 'answers': ['iPhone', 'Blackberry', 'Nokia 3310', 'Motorola Razr'], 'correct': 0}
        ],
        'History': [
            {'question': 'What year did the American Civil War begin?', 'answers': ['1861', '1865', '1776', '1945'], 'correct': 0},
            {'question': 'Who was the first president of the United States?', 'answers': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'], 'correct': 1},
            {'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?', 'answers': ['Incas', 'Mayans', 'Aztecs', 'Egyptians'], 'correct': 3}
        ],
        'General Knowledge': [
            {'question': 'What is the largest ocean on Earth?', 'answers': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'], 'correct': 3},
            {'question': 'What is the capital city of Australia?', 'answers': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'correct': 3},
            {'question': 'What is the name of the longest river in the world?', 'answers': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'], 'correct': 1}
        ]
    }
    
    # Select a random set of 3 questions from the quiz data for the selected topic
    quiz_questions = random.sample(quiz_data[topic], 3)
    
    # Display the quiz questions and get user's answers
    score = 0
    for question in quiz_questions:
        print(question['question'])
        for i, answer in enumerate(question['answers']):
            print(f"{i+1}. {answer}")
        
        while True:
            try:
                user_answer = int(input('Enter your answer (1-4): '))
                if user_answer >= 1 and user_answer <= 4:
                    if user_answer - 1 == question['correct']:
                        print('Correct!')
                        score += 1
                    else:
                        print('Incorrect. The correct answer is:', question['answers'][question['correct']])
                    break
                else:
                    print('Invalid choice. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')
    
    print(f'Your final score is {score} out of 3.')

# Main program loop
while True:
    selected_topic = display_menu()
    print(f'\nRandom fact about {selected_topic.lower()}:')
    print(get_random_fact(selected_topic))
    
    print('\nNow let\'s test your knowledge with a quiz!')
    display_quiz(selected_topic)
    
    again = input('\nDo you want to try another topic? (y/n) ').lower()
    if again != 'y':
        break

print('\nThank you for using the Interactive Knowledge Booster. Have a great day!')
