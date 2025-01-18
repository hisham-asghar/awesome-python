import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The first person to win the Nobel Prize in all six categories was Marie Curie.',
            'The fastest wind speed ever recorded on Earth was 253 mph during a typhoon in Australia.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To digest food', 'To produce oxygen'],
                'answer': 0
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn'],
                'answer': 1
            },
            {
                'question': 'Which scientist is famous for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called 'Creeper', was created in 1971.',
            'The first text message was sent on December 3, 1992.',
            'The internet was originally called ARPANET, created by the U.S. Department of Defense in 1969.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the first programmable computer?',
                'options': ['ENIAC', 'Apple I', 'IBM PC'],
                'answer': 0
            },
            {
                'question': 'What is the name of the company that created the first smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry'],
                'answer': 2
            },
            {
                'question': 'Which technology company was founded by Bill Gates and Paul Allen?',
                'options': ['Apple', 'Google', 'Microsoft'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Aztecs', 'Incas', 'Egyptians'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplane'],
                'answer': 0
            },
            {
                'question': 'Which event marked the start of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Fall of the Berlin Wall', 'Cuban Missile Crisis'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The largest known spider is the Goliath birdeater, which can have a leg span of up to 12 inches.',
            'The first country to give women the right to vote was New Zealand in 1893.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 2
            },
            {
                'question': 'Which is the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga'],
                'answer': 0
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB-'],
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
    
    user_answer = int(input("Enter your answer (1-3): "))
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
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()