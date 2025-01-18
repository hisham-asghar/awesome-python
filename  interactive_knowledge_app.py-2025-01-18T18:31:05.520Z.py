import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first successful kidney transplant was performed in 1954.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Combustion', 'Evaporation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which element is the most abundant in the Earth\'s crust?',
                'options': ['Oxygen', 'Silicon', 'Aluminum', 'Iron'],
                'answer': 'Oxygen'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Magnetism', 'Electricity', 'Friction'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was unveiled in 1946 and weighed 30 tons.',
            'The first commercial smartphone, the IBM Simon, was released in 1992.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'JavaScript'],
                'answer': 'Python'
            },
            {
                'question': 'Which company developed the first commercially successful web browser?',
                'options': ['Microsoft', 'Google', 'Apple', 'Netscape'],
                'answer': 'Netscape'
            },
            {
                'question': 'What is the name of the process by which computers and other devices communicate with each other?',
                'options': ['Networking', 'Coding', 'Encryption', 'Rendering'],
                'answer': 'Networking'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Magna Carta was a landmark document that established the principle of limited government in England in 1215.',
            'The French Revolution began in 1789 with the Storming of the Bastille.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first permanent English settlement in North America?',
                'options': ['Jamestown', 'Plymouth Colony', 'Roanoke Colony', 'New Amsterdam'],
                'answer': 'Jamestown'
            },
            {
                'question': 'What was the name of the war that lasted from 1939 to 1945?',
                'options': ['World War I', 'World War II', 'Korean War', 'Vietnam War'],
                'answer': 'World War II'
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Romans', 'Mayans'],
                'answer': 'Greeks'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 18 feet tall.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'],
                'answer': 'Nile River'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Choose a topic to explore:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter the topic you want to explore: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print(f"Sorry, '{selected_topic}' is not a valid topic. Please try again.")

if __name__ == "__main__":
    main()