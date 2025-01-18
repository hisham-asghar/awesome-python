import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has 206 bones.',
            'The largest planet in our solar system is Jupiter.',
            'Photosynthesis is the process by which plants convert sunlight into energy.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Zn'],
                'answer': 'Au'
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 'Plasma'
            },
            {
                'question': 'What is the largest bone in the human body?',
                'options': ['Femur', 'Tibia', 'Humerus', 'Skull'],
                'answer': 'Femur'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was created in 1983.',
            'The internet was initially developed as a military communication network.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz': [
            {
                'question': 'What does "RAM" stand for?',
                'options': ['Random Access Memory', 'Rapid Access Memory', 'Read-only Access Memory', 'Reflective Access Memory'],
                'answer': 'Random Access Memory'
            },
            {
                'question': 'Which company developed the first commercial web browser?',
                'options': ['Microsoft', 'Apple', 'Netscape', 'Google'],
                'answer': 'Netscape'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China was built over 2,000 years ago.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Gutenberg Bible, the first printed book in the West, was published in 1455.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Mayans', 'Incas', 'Egyptians', 'Romans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'In what year did World War II end?',
                'options': ['1945', '1939', '1918', '1950'],
                'answer': '1945'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'Which planet in our solar system is known as the \"Red Planet\"?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 'Mars'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    """
    Main function that runs the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()