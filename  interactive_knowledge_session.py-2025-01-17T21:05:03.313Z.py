import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest organ in the human body is the skin.',
            'The hottest planet in the solar system is Venus.'
        ],
        'quiz': [
            {
                'question': 'What is the main component of the sun?',
                'options': ['Hydrogen', 'Helium', 'Carbon', 'Oxygen'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 3
            },
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Condensation'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964.',
            'The first email was sent in 1971.',
            'The World Wide Web was invented in 1989.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially available personal computer?',
                'options': ['Apple I', 'IBM PC', 'Commodore 64', 'Atari 800'],
                'answer': 1
            },
            {
                'question': 'What is the name of the technology that allows devices to connect to the internet wirelessly?',
                'options': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Cellular'],
                'answer': 1
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world.',
            'The Pyramids of Giza are the oldest and largest of the three major pyramids located in Giza, Egypt.',
            'The Eiffel Tower was built in 1889 for the Paris World's Fair.'
        ],
        'quiz': [
            {
                'question': 'In what year did Christopher Columbus discover America?',
                'options': ['1492', '1776', '1620', '1865'],
                'answer': 0
            },
            {
                'question': 'What was the name of the first successful powered flight by the Wright brothers?',
                'options': ['The Flyer', 'The Kitty Hawk', 'The Wright Flyer', 'The Aeroplane'],
                'answer': 2
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'India'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The tallest mammal is the giraffe.',
            'The largest known snowflake was 15 inches wide.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
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
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz = topics[topic]['quiz']
    question = random.choice(quiz)
    return question

def run_quiz(topic):
    """
    Runs the quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['options'][question['answer']])

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()