import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To filter waste', 'To produce insulin', 'To regulate body temperature'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 2
            },
            {
                'question': 'What is the symbol for the element gold on the periodic table?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The first digital camera was developed by Kodak in 1975 and could store 23 images.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Constant Power Usage', 'Central Program Unit'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a common type of computer storage device?',
                'options': ['Hard Disk Drive', 'Solid-State Drive', 'Floppy Disk', 'Holographic Disk'],
                'answer': 3
            },
            {
                'question': 'What is the purpose of a computer's graphics processing unit (GPU)?',
                'options': ['To process video and graphics', 'To manage computer memory', 'To control input/output devices', 'To execute mathematical calculations'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mesopotamian'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful powered flight?',
                'options': ['The Wright Flyer', 'The Kitty Hawk', 'The Biplane', 'The Glider'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The first person to circumnavigate the globe was the Portuguese explorer Ferdinand Magellan.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def quiz(topic):
    """
    Presents a quiz with multiple-choice questions for the selected topic.
    """
    score = 0
    quiz_questions = topics[topic]['quiz_questions']
    
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"Your final score is {score} out of {len(quiz_questions)}.")

def main():
    """
    Displays a menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic.capitalize()}: {get_random_fact(selected_topic)}")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()