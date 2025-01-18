import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The human body has around 60,000 miles of blood vessels.',
            'The first successful kidney transplant was performed in 1954.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest known prime number as of 2022?',
                'options': ['23 million digits', '100,000 digits', '1 million digits', '10 million digits'],
                'answer': '23 million digits'
            },
            {
                'question': 'Approximately how many miles of blood vessels does the human body have?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '100,000 miles'],
                'answer': '60,000 miles'
            },
            {
                'question': 'In what year was the first successful kidney transplant performed?',
                'options': ['1954', '1964', '1974', '1984'],
                'answer': '1954'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial microprocessor, the Intel 4004, was released in 1971.',
            'The first smartphone, the IBM Simon, was released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What was the weight of the first electronic computer, ENIAC?',
                'options': ['10 tons', '20 tons', '30 tons', '40 tons'],
                'answer': '30 tons'
            },
            {
                'question': 'In what year was the first commercial microprocessor, the Intel 4004, released?',
                'options': ['1961', '1971', '1981', '1991'],
                'answer': '1971'
            },
            {
                'question': 'What was the name of the first smartphone, released in 1992?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 9000 Communicator', 'IBM Simon'],
                'answer': 'IBM Simon'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Pyramids of Giza in Egypt were built around 2560-2540 BCE.',
            'The first successful powered flight by the Wright brothers took place in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'Approximately how long is the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            },
            {
                'question': 'Around what year were the Pyramids of Giza in Egypt built?',
                'options': ['1500 BCE', '2000 BCE', '2560-2540 BCE', '3000 BCE'],
                'answer': '2560-2540 BCE'
            },
            {
                'question': 'In what year did the first successful powered flight by the Wright brothers take place?',
                'options': ['1893', '1903', '1913', '1923'],
                'answer': '1903'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The highest recorded temperature on Earth was 154°F (68°C) in Death Valley, California, in 1913.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest known prime number as of 2022?',
                'options': ['10 million digits', '15 million digits', '20 million digits', '23 million digits'],
                'answer': '23 million digits'
            },
            {
                'question': 'What is the highest recorded temperature on Earth?',
                'options': ['120°F (49°C)', '135°F (57°C)', '154°F (68°C)', '170°F (77°C)'],
                'answer': '154°F (68°C)'
            },
            {
                'question': 'What is the largest known prime number as of 2022?',
                'options': ['10 million digits', '15 million digits', '20 million digits', '23 million digits'],
                'answer': '23 million digits'
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
        print(f"\nRandom fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()