
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

# Define the facts and quiz questions for each topic
facts_and_quizzes = {
    'Science': [
        {
            'fact': 'The human body has over 600 muscles.',
            'quiz': {
                'question': 'How many muscles are there in the human body?',
                'options': ['400', '600', '800', '1000'],
                'answer': '600'
            }
        },
        {
            'fact': 'The Earth is the only planet in our solar system with liquid water on its surface.',
            'quiz': {
                'question': 'Which planet in our solar system has liquid water on its surface?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Earth'],
                'answer': 'Earth'
            }
        },
        # Add more science facts and quizzes here
    ],
    'Technology': [
        {
            'fact': 'The first computer virus was created in 1983 and was called 'Brain'.',
            'quiz': {
                'question': 'What was the name of the first computer virus?',
                'options': ['Melissa', 'Stuxnet', 'WannaCry', 'Brain'],
                'answer': 'Brain'
            }
        },
        {
            'fact': 'The world's first programmable computer was the ENIAC, which was completed in 1946.',
            'quiz': {
                'question': 'What was the name of the world's first programmable computer?',
                'options': ['UNIVAC', 'ENIAC', 'MARK I', 'COLOSSUS'],
                'answer': 'ENIAC'
            }
        },
        # Add more technology facts and quizzes here
    ],
    'History': [
        {
            'fact': 'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'quiz': {
                'question': 'What is the approximate length of the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            }
        },
        {
            'fact': 'The Mona Lisa was stolen from the Louvre Museum in Paris in 1911 and was missing for two years.',
            'quiz': {
                'question': 'In what year was the Mona Lisa stolen from the Louvre Museum?',
                'options': ['1901', '1911', '1921', '1931'],
                'answer': '1911'
            }
        },
        # Add more history facts and quizzes here
    ],
    'General Knowledge': [
        {
            'fact': 'The largest organ in the human body is the skin.',
            'quiz': {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Lungs', 'Skin'],
                'answer': 'Skin'
            }
        },
        {
            'fact': 'The tallest mammal in the world is the giraffe.',
            'quiz': {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Rhinoceros', 'Giraffe', 'Hippopotamus'],
                'answer': 'Giraffe'
            }
        },
        # Add more general knowledge facts and quizzes here
    ]
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

def get_random_fact_and_quiz(topic):
    fact_and_quiz = random.choice(facts_and_quizzes[topic])
    return fact_and_quiz

def run_quiz(fact_and_quiz):
    print(f"Fun Fact: {fact_and_quiz['fact']}")
    print(f"Quiz Question: {fact_and_quiz['quiz']['question']}")
    for option in fact_and_quiz['quiz']['options']:
        print(f"- {option}")

    user_answer = input("Enter your answer: ")
    if user_answer.lower() == fact_and_quiz['quiz']['answer'].lower():
        print("Correct! Well done.")
    else:
        print("Incorrect. Better luck next time.")

def main():
    display_menu()
    topic_id = input("Enter the topic number: ")

    if topic_id in topics:
        topic = topics[topic_id]
        fact_and_quiz = get_random_fact_and_quiz(topic)
        run_quiz(fact_and_quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
