import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'A group of flamingos is called a 'flamboyance'.'
        ],
        'quizzes': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To filter waste', 'To produce oxygen'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Plasma', 'Energy'],
                'answer': 3
            },
            {
                'question': 'What is the name of the process where water changes from a liquid to a gas?',
                'options': ['Condensation', 'Evaporation', 'Precipitation', 'Sublimation'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Mozilla', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 3
            },
            {
                'question': 'What is the name of the device that converts digital signals to analog signals?',
                'options': ['Modem', 'Router', 'Switch', 'Transducer'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight was made by the Wright brothers in 1903.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and engineering?',
                'options': ['Egyptians', 'Greeks', 'Romans', 'Mayans'],
                'answer': 1
            },
            {
                'question': 'What was the name of the first successful European settlement in North America?',
                'options': ['Jamestown', 'Plymouth Colony', 'St. Augustine', 'Quebec'],
                'answer': 0
            },
            {
                'question': 'Which event is considered the start of the American Civil War?',
                'options': ['Battle of Gettysburg', 'Assassination of Abraham Lincoln', 'Attack on Fort Sumter', 'Emancipation Proclamation'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'A group of flamingos is called a 'flamboyance'.',
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            },
            {
                'question': 'What is the name of the largest continent in the world?',
                'options': ['North America', 'South America', 'Asia', 'Africa'],
                'answer': 2
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
                'answer': 1
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz(topic):
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Enter your answer (0-3): "))
            if answer == quiz['answer']:
                print("Correct!")
                return True
            else:
                print("Incorrect. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 3.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to get started:")
    
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        selected_topic = input("Enter a topic (or 'quit' to exit): ").lower()
        if selected_topic == 'quit':
            break
        
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            
            print("\nNow, let's test your knowledge with a quiz!")
            quiz = get_quiz(selected_topic)
            if run_quiz(quiz):
                print("Great job! You've increased your knowledge.")
            else:
                print("Better luck next time!")
        else:
            print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()