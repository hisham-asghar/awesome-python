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

# Function to display a random fact or concept from the selected topic
def display_random_fact(topic):
    facts = {
        'Science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'Bees can fly higher than the tallest building.'
        ],
        'Technology': [
            'The first computer mouse was invented in 1964 and cost $25.',
            'The first text message was sent on December 3, 1992, and it said \"Merry Christmas\".',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'History': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h) - the speed limit was 2 mph (3 km/h).'
        ],
        'General Knowledge': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ]
    }
    
    # Fetch a random fact from the selected topic
    random_fact = random.choice(facts[topic])
    print(f'Random fact about {topic}: {random_fact}')

# Function to display the quiz and check user's answers
def quiz(topic):
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'How many planets are in our solar system?', 'answers': ['8', '9', '10', '12'], 'correct': 0},
            {'question': 'Which scientist is known for the theory of relativity?', 'answers': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'], 'correct': 1}
        ],
        'Technology': [
            {'question': 'What was the first commercially successful smartphone?', 'answers': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'], 'correct': 1},
            {'question': 'What is the name of the programming language created by Guido van Rossum?', 'answers': ['Java', 'C++', 'Python', 'Ruby'], 'correct': 2},
            {'question': 'Which company developed the first graphical user interface (GUI)?', 'answers': ['Microsoft', 'Apple', 'IBM', 'Xerox'], 'correct': 3}
        ],
        'History': [
            {'question': 'In what year did World War II end?', 'answers': ['1945', '1939', '1941', '1947'], 'correct': 0},
            {'question': 'Who was the first president of the United States?', 'answers': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'James Madison'], 'correct': 1},
            {'question': 'Which ancient civilization built the pyramids?', 'answers': ['Romans', 'Greeks', 'Egyptians', 'Mayans'], 'correct': 2}
        ],
        'General Knowledge': [
            {'question': 'What is the largest ocean on Earth?', 'answers': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'], 'correct': 3},
            {'question': 'Which country is known as the Land of the Rising Sun?', 'answers': ['China', 'Japan', 'South Korea', 'North Korea'], 'correct': 1},
            {'question': 'What is the tallest mammal in the world?', 'answers': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'], 'correct': 1}
        ]
    }
    
    # Select a random quiz from the selected topic
    selected_quiz = random.choice(quizzes[topic])
    
    # Display the quiz question and options
    print(f'Quiz question: {selected_quiz["question"]}')
    for i, answer in enumerate(selected_quiz['answers']):
        print(f'{i+1}. {answer}')
    
    # Get user's answer
    user_answer = int(input('Enter your answer (1-4): '))
    
    # Check if the user's answer is correct
    if user_answer - 1 == selected_quiz['correct']:
        print('Correct!')
    else:
        print('Incorrect. The correct answer is:', selected_quiz['answers'][selected_quiz['correct']])

# Main program loop
while True:
    # Display the menu of topics
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    print('5. Exit')
    
    # Get user's topic selection
    choice = input('Enter your choice (1-5): ')
    
    # Handle user's choice
    if choice == '5':
        print('Thank you for using the Interactive Knowledge Booster. Goodbye!')
        break
    elif choice in topics:
        topic = topics[choice]
        print(f'You selected: {topic}')
        display_random_fact(topic)
        quiz(topic)
    else:
        print('Invalid choice. Please try again.')