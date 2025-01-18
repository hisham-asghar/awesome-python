import random
import requests
import json

def get_fact(topic):
    """Fetches a random fact or concept from the selected topic."""
    facts = {
        'science': [
            'The Milky Way galaxy contains over 200 billion stars.',
            'Diamonds are made from compressed carbon that was formed millions of years ago.',
            'The human body is made up of approximately 60% water.'
        ],
        'technology': [
            'The first programmable computer was the ENIAC, which was completed in 1946.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.',
            'Quantum computers have the potential to solve certain problems much faster than classical computers.'
        ],
        'history': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from the 1st century BC to the 5th century AD.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'general': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 21,000 kilometers (13,000 miles).'
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provides a multiple-choice quiz on the selected topic."""
    quizzes = {
        'science': [
            {
                'question': 'What is the chemical symbol for gold?',
                'choices': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system is known as the 'Red Planet'?',
                'choices': ['Mars', 'Jupiter', 'Saturn', 'Venus'],
                'answer': 'Mars'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ],
        'technology': [
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'choices': ['Internet Explorer', 'Netscape Navigator', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            },
            {
                'question': 'Which company developed the first personal computer, the Apple I?',
                'choices': ['IBM', 'Microsoft', 'Apple', 'HP'],
                'answer': 'Apple'
            },
            {
                'question': 'What is the name of the programming language that was designed to be easy to read and write?',
                'choices': ['C++', 'Java', 'Python', 'JavaScript'],
                'answer': 'Python'
            }
        ],
        'history': [
            {
                'question': 'In what year did the United States declare its independence?',
                'choices': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Which ancient civilization is known for its impressive pyramids and advanced mathematics?',
                'choices': ['Greek', 'Roman', 'Egyptian', 'Mayan'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'choices': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            }
        ],
        'general': [
            {
                'question': 'What is the largest planet in our solar system?',
                'choices': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'Which country is known as the 'Land of the Rising Sun'?',
                'choices': ['China', 'Japan', 'India', 'South Korea'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the largest organ in the human body?',
                'choices': ['Heart', 'Liver', 'Lungs', 'Skin'],
                'answer': 'Skin'
            }
        ]
    }
    quiz_data = random.choice(quizzes[topic])
    print(quiz_data['question'])
    for i, choice in enumerate(quiz_data['choices']):
        print(f"{i+1}. {choice}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_data['choices'][int(user_answer)-1] == quiz_data['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_data['answer']}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    topics = ['Science', 'Technology', 'History', 'General']
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    topic_choice = int(input("Enter your choice (1-4): ")) - 1
    chosen_topic = topics[topic_choice].lower()

    print(f"\nHere's a random fact about {topics[topic_choice]}:")
    print(get_fact(chosen_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz(chosen_topic)

if __name__ == "__main__":
    main()