
import random
import requests
import json

# Define topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define facts and quizzes for each topic
facts = {
    'Science': [
        "The human body has around 60,000 miles of blood vessels.",
        "The first successful kidney transplant was performed in 1954.",
        "The largest known prime number as of 2022 has 23 million digits."
    ],
    'Technology': [
        "The first electronic computer, ENIAC, was completed in 1946.",
        "The first smartphone was the IBM Simon, released in 1992.",
        "The World Wide Web was invented by Tim Berners-Lee in 1989."
    ],
    'History': [
        "The Great Wall of China is the longest man-made structure in the world.",
        "The Colosseum in Rome was completed in 80 AD and could hold up to 80,000 spectators.",
        "The first successful powered flight was made by the Wright brothers in 1903."
    ],
    'General Knowledge': [
        "The largest organ in the human body is the skin.",
        "The tallest mammal is the giraffe.",
        "The largest ocean on Earth is the Pacific Ocean."
    ]
}

quizzes = {
    'Science': [
        {
            'question': "What is the chemical symbol for gold?",
            'options': ['Au', 'Ag', 'Cu', 'Fe'],
            'answer': 'Au'
        },
        {
            'question': "What is the process by which plants convert sunlight into energy?",
            'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
            'answer': 'Photosynthesis'
        },
        {
            'question': "What is the name of the largest planet in our solar system?",
            'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
            'answer': 'Jupiter'
        }
    ],
    'Technology': [
        {
            'question': "What is the name of the programming language created by Guido van Rossum?",
            'options': ['Java', 'C++', 'Python', 'Ruby'],
            'answer': 'Python'
        },
        {
            'question': "What is the name of the first commercially successful web browser?",
            'options': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
            'answer': 'Netscape Navigator'
        },
        {
            'question': "What is the name of the company that developed the Android operating system?",
            'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
            'answer': 'Google'
        }
    ],
    'History': [
        {
            'question': "What year was the United States Declaration of Independence signed?",
            'options': ['1776', '1789', '1812', '1865'],
            'answer': '1776'
        },
        {
            'question': "Who was the first president of the United States?",
            'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
            'answer': 'George Washington'
        },
        {
            'question': "What was the name of the first successful powered flight made by the Wright brothers?",
            'options': ['Kitty Hawk', 'Spirit of St. Louis', 'Flyer I', 'Red Baron'],
            'answer': 'Flyer I'
        }
    ],
    'General Knowledge': [
        {
            'question': "What is the largest planet in our solar system?",
            'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
            'answer': 'Jupiter'
        },
        {
            'question': "What is the name of the tallest mountain in the world?",
            'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
            'answer': 'Mount Everest'
        },
        {
            'question': "What is the name of the largest ocean on Earth?",
            'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
            'answer': 'Pacific Ocean'
        }
    ]
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

def display_fact(topic):
    fact = random.choice(facts[topic])
    print(f"Here's an interesting fact about {topic.lower()}:\n{fact}")

def run_quiz(topic):
    quiz = quizzes[topic]
    score = 0
    for q in quiz:
        print(q['question'])
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if q['options'][int(user_answer) - 1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz)}.")

def main():
    display_menu()
    topic_choice = input("Enter the number of the topic you want to explore: ")
    if topic_choice in topics:
        topic = topics[topic_choice]
        display_fact(topic)
        run_quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
