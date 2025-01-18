import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2023 has over 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Io', 'Europa'],
                'answer': 'Titan'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Creeper\", was created in 1971.',
            'The first commercially available personal computer was the Altair 8800, released in 1975.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quizzes': [
            {
                'question': 'What does \"RAM\" stand for in computer terminology?',
                'options': ['Random Access Memory', 'Rapid Analog Memory', 'Robust Automated Mechanism', 'Reconfigurable Analog Matrix'],
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
            'The first successful powered flight by the Wright brothers took place in 1903.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for the construction of the pyramids?',
                'options': ['Mesopotamia', 'Aztec', 'Inca', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            },
            {
                'question': 'In what year did World War II end?',
                'options': ['1945', '1939', '1941', '1918'],
                'answer': '1945'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
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
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz(topic):
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if quiz['options'][int(user_answer)-1] == quiz['answer']:
            print("Correct!")
            return True
        else:
            print("Incorrect. The correct answer is:", quiz['answer'])
            return False
    else:
        print("Invalid input. Please try again.")
        return run_quiz(quiz)

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        if run_quiz(quiz):
            print("Congratulations, you got the answer right!")
        else:
            print("Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()