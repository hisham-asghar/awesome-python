import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'The Earth is the only planet in our solar system with liquid water on its surface.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest known prime number?',
                'options': ['23 million digits', '100,000 digits', '1 million digits', '10 million digits'],
                'answer': '23 million digits'
            },
            {
                'question': 'How many miles of blood vessels are in the human body?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '100,000 miles'],
                'answer': '60,000 miles'
            },
            {
                'question': 'Which planet in our solar system has liquid water on its surface?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Earth'],
                'answer': 'Earth'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.',
            'The world's first text message was sent on December 3, 1992, and said "Merry Christmas".',
            'The first commercial smartphone, the IBM Simon, was released in 1993.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the first computer bug?',
                'options': ['A software error', 'A hardware malfunction', 'A real moth', 'A programming mistake'],
                'answer': 'A real moth'
            },
            {
                'question': 'When was the world's first text message sent?',
                'options': ['1990', '1992', '1995', '2000'],
                'answer': '1992'
            },
            {
                'question': 'Which company released the first commercial smartphone?',
                'options': ['Apple', 'Samsung', 'Nokia', 'IBM'],
                'answer': 'IBM'
            }
        ]
    },
    'history': {
        'facts': [
            'The first Olympic games were held in 776 BC in Olympia, Greece.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'When were the first Olympic games held?',
                'options': ['500 BC', '776 BC', '1000 BC', '1200 BC'],
                'answer': '776 BC'
            },
            {
                'question': 'How long is the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            },
            {
                'question': 'Why does the Mona Lisa have no eyebrows?',
                'options': ['It was damaged over time', 'It was a fashion trend in Renaissance Florence', 'The artist forgot to paint them', 'It was intentionally left out'],
                'answer': 'It was a fashion trend in Renaissance Florence'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and causes the structure to be taller.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'How much taller can the Eiffel Tower get during summer?',
                'options': ['5 cm', '10 cm', '15 cm', '20 cm'],
                'answer': '15 cm'
            },
            {
                'question': 'What is a group of porcupines called?',
                'options': ['A quill', 'A spike', 'A prickle', 'A cluster'],
                'answer': 'A prickle'
            },
            {
                'question': 'What was the first product to have a barcode?',
                'options': ['Coca-Cola', 'Bread', 'Wrigley's gum', 'Milk'],
                'answer': 'Wrigley's gum'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    return random.choice(topics[topic]['facts'])

def run_quiz(topic):
    """
    Runs a quiz with multiple-choice questions for the given topic.
    """
    score = 0
    quiz_questions = topics[topic]['quiz_questions']
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_questions)}.")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()