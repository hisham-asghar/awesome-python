import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The largest known prime number has over 23 million digits.',
            'A single lightning bolt can reach temperatures of up to 30,000 degrees Celsius.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the force that attracts objects with mass?',
                'options': ['Friction', 'Gravity', 'Magnetism', 'Electricity'],
                'answer': 1
            },
            {
                'question': 'What is the chemical symbol for the element gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real moth trapped in a Harvard Mark II computer.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The term 'computer bug' was coined by Grace Hopper in 1947.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals?',
                'options': ['Modem', 'Router', 'Switch', 'Amplifier'],
                'answer': 0
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
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, which was the speed limit at the time.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the name of the first permanent English settlement in North America?',
                'options': ['Jamestown', 'Plymouth Colony', 'Massachusetts Bay Colony', 'New Amsterdam'],
                'answer': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'John Adams'],
                'answer': 2
            },
            {
                'question': 'What was the name of the ancient civilization that built the pyramids in Egypt?',
                'options': ['Mesopotamians', 'Incas', 'Mayans', 'Ancient Egyptians'],
                'answer': 3
            }
        ]
    },
    'general': {
        'facts': [
            'The first product to have a barcode was Wrigley's gum.',
            'A group of porcupines is called a prickle.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Pacific Ocean', 'Indian Ocean'],
                'answer': 2
            },
            {
                'question': 'What is the largest mammal on Earth?',
                'options': ['African Elephant', 'Blue Whale', 'Sperm Whale', 'Hippopotamus'],
                'answer': 1
            },
            {
                'question': 'What is the tallest building in the world?',
                'options': ['Burj Khalifa', 'Shanghai Tower', 'Abraj Al-Bait Clock Tower', 'One World Trade Center'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['options'][question['answer']])

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()