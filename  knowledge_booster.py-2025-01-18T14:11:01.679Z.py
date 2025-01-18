import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has 206 bones.',
            'The largest planet in our solar system is Jupiter.',
            'Water boils at 100 degrees Celsius (212 degrees Fahrenheit).'
        ],
        'quiz_questions': [
            {
                'question': 'Which of the following is a renewable energy source?',
                'options': ['Coal', 'Oil', 'Solar', 'Nuclear'],
                'answer': 'Solar'
            },
            {
                'question': 'What is the name of the force that pulls objects towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            },
            {
                'question': 'Which organ in the human body produces insulin?',
                'options': ['Heart', 'Liver', 'Pancreas', 'Kidney'],
                'answer': 'Pancreas'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus was created in 1983.',
            'The internet was originally called ARPANET and was created by the US Department of Defense.',
            'The first mobile phone call was made in 1973 by Martin Cooper of Motorola.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company created the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Google Chrome', 'Mozilla Firefox', 'Microsoft Edge', 'Mosaic'],
                'answer': 'Mosaic'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2500 BC.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Chinese'],
                'answer': 'Mayans'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event marked the end of World War II?',
                'options': ['D-Day', 'Pearl Harbor', 'Hiroshima and Nagasaki bombings', 'V-E Day'],
                'answer': 'Hiroshima and Nagasaki bombings'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has over 23 million digits.',
            'The tallest mammal in the world is the giraffe.',
            'The largest ocean on Earth is the Pacific Ocean.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest continent in the world by land area?',
                'options': ['Asia', 'Africa', 'North America', 'South America'],
                'answer': 'Asia'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Io'],
                'answer': 'Titan'
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
    question = random.choice(topics[topic]['quiz_questions'])
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

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

if __name__ == '__main__':
    main()