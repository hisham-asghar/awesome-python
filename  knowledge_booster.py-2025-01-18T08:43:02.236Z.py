import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first product to have a barcode was Wrigley's gum.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 0
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['Solid', 'Liquid', 'Gas', 'Plasma'],
                'answer': 2
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.',
            'The first text message was sent on December 3, 1992, and said "Merry Christmas".',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'High-Tech Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Markup Lingua'],
                'answer': 0
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Mozilla Firefox', 'Google Chrome', 'Microsoft Internet Explorer', 'Netscape Navigator'],
                'answer': 3
            },
            {
                'question': 'What is the name of the programming language used to build websites?',
                'options': ['Java', 'Python', 'C++', 'JavaScript'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The first known written language was Sumerian cuneiform, developed in Mesopotamia around 3500 BC.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Aztecs', 'Romans', 'Egyptians', 'Greeks'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['Kitty Hawk', 'Spirit of St. Louis', 'Wright Flyer', 'Concorde'],
                'answer': 2
            },
            {
                'question': 'Which event marked the end of World War II?',
                'options': ['D-Day', 'Pearl Harbor', 'Hiroshima and Nagasaki bombings', 'Fall of Berlin'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.',
            'A group of flamingos is called a flamboyance.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 2
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Moose', 'Rhinoceros'],
                'answer': 1
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
    print("Select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize(), ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()