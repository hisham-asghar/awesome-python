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
        'quiz_questions': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To digest food', 'To produce hormones'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Plasma', 'Emotion'],
                'answer': 3
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Magnetism', 'Friction', 'Electromagnetism'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was created in 1983 and was called the 'Brain' virus.',
            'The first commercially available personal computer was the Altair 8800, released in 1975.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the process by which a computer executes instructions?',
                'options': ['Computation', 'Execution', 'Processing', 'Calculation'],
                'answer': 2
            },
            {
                'question': 'Which of these is not a type of computer memory?',
                'options': ['RAM', 'ROM', 'GPU', 'SSD'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
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
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mesopotamian'],
                'answer': 2
            },
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': 0
            },
            {
                'question': 'Which explorer is credited with discovering America?',
                'options': ['Christopher Columbus', 'Magellan', 'Vasco da Gama', 'Marco Polo'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'A group of flamingos is called a 'flamboyance'.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and the tower grows in height.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mammal?',
                'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 1
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 1
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz_questions'])
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
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