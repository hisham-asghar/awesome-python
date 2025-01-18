import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'Bananas are slightly radioactive due to their potassium content.'
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
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Creeper\", was created in 1971 as an experiment.',
            'The first commercial smartphone was the IBM Simon, released in 1992.',
            'The world's first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Markup Lexicon', 'Hyper Textual Markup Language'],
                'answer': 'Hyper Text Markup Language'
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
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Egyptian', 'Mesopotamian'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event marked the start of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 'The assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and causes the structure to grow.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'Which country is known as the \"Land of the Rising Sun\"?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 'Japan'
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
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options'], start=1):
        print(f"{i}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question['options'][user_answer - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()