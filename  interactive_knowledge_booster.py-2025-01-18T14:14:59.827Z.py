import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has 206 bones.',
            'The largest known prime number has over 23 million digits.',
            'The first successful kidney transplant was performed in 1954.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964.',
            'The internet was originally called ARPANET, created by the U.S. Department of Defense.',
            'The first digital camera was developed in 1975 by Kodak.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Compact Processor Unit', 'Central Power Unit'],
                'answer': 'Central Processing Unit'
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
            'The Great Wall of China is the longest man-made structure in the world.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.'
        ],
        'quiz_questions': [
            {
                'question': 'In what year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Maya', 'Egyptian'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest ocean on Earth is the Pacific Ocean.',
            'The tallest mammal in the world is the giraffe.',
            'The largest continent in the world is Asia.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.strip() == str(question['options'].index(question['answer']) + 1):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()