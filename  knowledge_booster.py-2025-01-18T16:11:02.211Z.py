import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'Bananas are slightly radioactive.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.'
        ],
        'quiz': [
            {
                'question': 'What is the primary function of the human heart?',
                'options': ['to pump blood', 'to produce oxygen', 'to filter waste'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['solid', 'liquid', 'plasma', 'energy'],
                'answer': 3
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was made of wood.',
            'The first commercial text message was sent on December 3, 1992.',
            'The first programmable computer was the ENIAC, which was completed in 1946.'
        ],
        'quiz': [
            {
                'question': 'What does "HTTP" stand for?',
                'options': ['Hyper Text Transfer Protocol', 'High-speed Transmission Technology Protocol', 'Hyperlink Transfer Procedure'],
                'answer': 0
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 2
            },
            {
                'question': 'What is the primary function of a computer's CPU?',
                'options': ['to store data', 'to display images', 'to process information', 'to generate electricity'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight was made by the Wright brothers in 1903.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'Benjamin Franklin'],
                'answer': 2
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Egyptian', 'Mayan'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'A group of flamingos is called a 'flamboyance'.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'There are more possible iterations of a game of chess than there are atoms in the observable universe.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 1
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 3
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['options'][quiz_question['answer']])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()