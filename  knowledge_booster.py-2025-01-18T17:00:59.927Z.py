
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

# Function to display the menu and get user's choice
def display_menu():
    print('Welcome to the Knowledge Booster!')
    print('Please select a topic:')
    for topic_id, topic_name in topics.items():
        print(f'{topic_id}. {topic_name}')
    return input('Enter your choice (1-4): ')

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # You can use public APIs or a predefined database to fetch the facts
    facts = {
        'Science': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'Sharks have been on Earth for over 400 million years.'
        ],
        'Technology': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first email was sent in 1971 by Ray Tomlinson.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'History': [
            'The Great Wall of China is the longest man-made structure in the world.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'General Knowledge': [
            'The largest organ in the human body is the skin.',
            'The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off.',
            'The largest desert in the world is Antarctica, not the Sahara.'
        ]
    }
    return random.choice(facts[topic])

# Function to display the quiz and get the user's answer
def quiz(topic):
    # You can use public APIs or a predefined database to fetch the quiz questions and answers
    quizzes = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 'Au'},
            {'question': 'Which planet in our solar system is known as the "Red Planet"?', 'options': ['Mars', 'Jupiter', 'Saturn', 'Venus'], 'answer': 'Mars'},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'options': ['Respiration', 'Photosynthesis', 'Transpiration', 'Evaporation'], 'answer': 'Photosynthesis'}
        ],
        'Technology': [
            {'question': 'What is the name of the first programmable computer?', 'options': ['ENIAC', 'Apple II', 'IBM PC', 'Commodore 64'], 'answer': 'ENIAC'},
            {'question': 'Which company developed the first commercial web browser?', 'options': ['Microsoft', 'Apple', 'Netscape', 'Google'], 'answer': 'Netscape'},
            {'question': 'What is the name of the programming language used to create websites?', 'options': ['Java', 'Python', 'C++', 'HTML'], 'answer': 'HTML'}
        ],
        'History': [
            {'question': 'In what year did the American Civil War begin?', 'options': ['1861', '1865', '1775', '1914'], 'answer': '1861'},
            {'question': 'Which ancient civilization is known for building the Pyramids?', 'options': ['Aztecs', 'Incas', 'Egyptians', 'Greeks'], 'answer': 'Egyptians'},
            {'question': 'What was the name of the first successful powered flight?', 'options': ['Apollo 11', 'Sputnik 1', 'Wright Flyer', 'Concorde'], 'answer': 'Wright Flyer'}
        ],
        'General Knowledge': [
            {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'], 'answer': 'Pacific Ocean'},
            {'question': 'What is the tallest mammal in the world?', 'options': ['Elephant', 'Giraffe', 'Rhinoceros', 'Hippopotamus'], 'answer': 'Giraffe'},
            {'question': 'What is the capital city of Australia?', 'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'answer': 'Canberra'}
        ]
    }
    quiz_data = random.choice(quizzes[topic])
    print(f"Question: {quiz_data['question']}")
    for index, option in enumerate(quiz_data['options'], start=1):
        print(f"{index}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_data['options'][int(user_answer) - 1] == quiz_data['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_data['answer'])

# Main function to run the script
def main():
    while True:
        topic_choice = display_menu()
        if topic_choice in topics:
            topic = topics[topic_choice]
            print(f"\nHere's a random fact about {topic}:")
            print(get_random_fact(topic))
            print("\nNow, let's test your knowledge with a quiz!")
            quiz(topic)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
