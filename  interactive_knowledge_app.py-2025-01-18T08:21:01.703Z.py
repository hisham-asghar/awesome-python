import random
import requests
import json

# Define the topics and their associated facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'A single lightning bolt contains enough energy to toast 100,000 pieces of bread.'
        ],
        'quizzes': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'choices': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'choices': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 3
            },
            {
                'question': 'What is the largest organ in the human body?',
                'choices': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 2
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and cost around $25.',
            'The first commercial text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'choices': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'choices': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 0
            },
            {
                'question': 'What is the name of the technology that allows devices to connect to the internet wirelessly?',
                'choices': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Cellular'],
                'answer': 1
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quizzes': [
            {
                'question': 'What was the name of the first successful computer?',
                'choices': ['ENIAC', 'Apple I', 'IBM PC', 'Commodore 64'],
                'answer': 0
            },
            {
                'question': 'What was the name of the first successful vaccine?',
                'choices': ['Polio', 'Smallpox', 'Measles', 'Influenza'],
                'answer': 1
            },
            {
                'question': 'What was the name of the first successful moon landing?',
                'choices': ['Apollo 8', 'Apollo 11', 'Sputnik 1', 'Gemini 3'],
                'answer': 1
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2023 has 23 million digits.',
            'The highest point on Earth is Mount Everest, at 29,032 feet (8,849 meters) above sea level.',
            'The tallest mammal is the giraffe, which can grow up to 18 feet (5.5 meters) tall.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'choices': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the largest continent on Earth?',
                'choices': ['Asia', 'Africa', 'North America', 'South America'],
                'answer': 0
            },
            {
                'question': 'What is the rarest blood type?',
                'choices': ['A', 'B', 'AB', 'O'],
                'answer': 2
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
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz['question'])
    for i, choice in enumerate(quiz['choices']):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz['answer']:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nFact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nLet's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()