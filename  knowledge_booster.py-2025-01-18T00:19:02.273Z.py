import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'Which of these is a renewable energy source?',
                'options': ['Coal', 'Oil', 'Solar', 'Nuclear'],
                'answer': 'Solar'
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Callisto', 'Ganymede', 'Europa'],
                'answer': 'Titan'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Brain\", was created in 1986.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The term \"computer bug\" was coined after a moth was found causing an error in the Harvard Mark II computer in 1947.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the first web browser, created by Tim Berners-Lee?',
                'options': ['Mosaic', 'Netscape', 'Internet Explorer', 'WorldWideWeb'],
                'answer': 'WorldWideWeb'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first book printed in English was the Recuyell of the Historyes of Troye, printed by William Caxton in 1473.'
        ],
        'quiz_questions': [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Aztec', 'Inca', 'Mayan', 'Egyptian'],
                'answer': 'Egyptian'
            }
        ]
    },
    'general': {
        'facts': [
            'The strongest muscle in the human body is the tongue.',
            'The largest known prime number as of 2022 has over 23 million digits.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 'Jupiter'
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
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nTime for a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()