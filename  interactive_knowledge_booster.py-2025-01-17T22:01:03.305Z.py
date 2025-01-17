import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first digital computer was the ENIAC, which was completed in 1946.',
            'The Milky Way galaxy contains approximately 200 billion stars.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which of these is not a fundamental force in nature?',
                'options': ['Gravity', 'Electromagnetism', 'Strong nuclear force', 'Weak nuclear force', 'Centrifugal force'],
                'answer': 'Centrifugal force'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first mobile phone call was made by Martin Cooper of Motorola in 1973.',
            'The internet was originally called ARPANET, and was created in 1969 by the U.S. Department of Defense.',
            'The first computer mouse was invented by Douglas Engelbart in 1964.'
        ],
        'quiz': [
            {
                'question': 'What does "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Management Language', 'Hyperlink Text Management Language'],
                'answer': 'Hyper Text Markup Language'
            },
            {
                'question': 'Which of these is not a common programming language?',
                'options': ['Python', 'Java', 'C++', 'Photoshop'],
                'answer': 'Photoshop'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Motorola Razr', 'Nokia 3310'],
                'answer': 'BlackBerry'
            }
        ]
    },
    'history': {
        'facts': [
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.',
            'The Great Wall of China was built over a period of 2,000 years, from the 3rd century BC to the 17th century AD.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mayan'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What event marked the end of World War II?',
                'options': ['D-Day', 'The Battle of Stalingrad', 'The bombing of Hiroshima and Nagasaki', 'The fall of Berlin'],
                'answer': 'The bombing of Hiroshima and Nagasaki'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
                'answer': 'Yen'
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Yellow', 'Green'],
                'answer': 'Green'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question['options'][user_answer-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()