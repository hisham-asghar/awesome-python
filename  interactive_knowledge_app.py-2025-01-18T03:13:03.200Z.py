import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'Honey is the only food that does not spoil.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which organ in the human body produces insulin?',
                'options': ['Liver', 'Pancreas', 'Kidney', 'Heart'],
                'answer': 'Pancreas'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was unveiled in 1946 and weighed 30 tons.',
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The world's first text message was sent on December 3, 1992.'
        ],
        'quizzes': [
            {
                'question': 'What does the acronym "RAM" stand for?',
                'options': ['Random Access Memory', 'Rapid Access Memory', 'Reconfigurable Array Memory', 'Redundant Array of Memories'],
                'answer': 'Random Access Memory'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
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
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560–2540 BC.',
            'The Gutenberg Bible, printed in 1455, was the first major book printed in the West using movable metal type.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'China'],
                'answer': 'Mesopotamia'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers in 1903?',
                'options': ['Flyer I', 'Spirit of St. Louis', 'Concorde', 'Sputnik'],
                'answer': 'Flyer I'
            },
            {
                'question': 'Which event marked the end of World War II in Europe?',
                'options': ['D-Day', 'VE Day', 'VJ Day', 'Battle of Stalingrad'],
                'answer': 'VE Day'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest desert in the world is the Sahara Desert, covering an area of 3.6 million square miles.',
            'The largest organ in the human body is the skin.',
            'The tallest mammal in the world is the giraffe, which can grow up to 18 feet tall.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
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
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the selected topic.
    """
    return random.choice(topics[topic]['quizzes'])

def run_quiz(quiz):
    """
    Runs the interactive quiz for the user.
    """
    score = 0
    print(f"Question: {quiz['question']}")
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz['answer'])
    return score

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    while True:
        print("\nPlease select a topic:")
        for topic in topics.keys():
            print(f"- {topic.capitalize()}")
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic not in topics:
            print("Invalid topic. Please try again.")
            continue

        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nLet's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score}/1")

        play_again = input("\nWould you like to try another topic? (y/n) ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()