
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept for the given topic.
    """
    if topic == '1':  # Science
        # Fetch a random science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '2':  # Technology
        # Fetch a random technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '3':  # History
        # Fetch a random history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '4':  # General Knowledge
        # Fetch a random general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general')
        facts = response.json()
        return random.choice(facts)['fact']
    else:
        return "Invalid topic selected."

def quiz(topic):
    """
    Provide an interactive quiz for the given topic.
    """
    if topic == '1':  # Science
        # Load science quiz questions and answers from a database or API
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
                'answer': 'Jupiter'
            },
            # Add more science quiz questions and answers
        ]
    elif topic == '2':  # Technology
        # Load technology quiz questions and answers from a database or API
        questions = [
            {
                'question': 'What is the primary function of a computer processor (CPU)?',
                'options': ['Data storage', 'Network communication', 'Graphic rendering', 'Computation'],
                'answer': 'Computation'
            },
            {
                'question': 'What is the name of the first commercially successful smartphone?',
                'options': ['iPhone', 'BlackBerry', 'Nokia 3310', 'Motorola RAZR'],
                'answer': 'BlackBerry'
            },
            # Add more technology quiz questions and answers
        ]
    elif topic == '3':  # History
        # Load history quiz questions and answers from a database or API
        questions = [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'James Madison'],
                'answer': 'George Washington'
            },
            # Add more history quiz questions and answers
        ]
    elif topic == '4':  # General Knowledge
        # Load general knowledge quiz questions and answers from a database or API
        questions = [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            # Add more general knowledge quiz questions and answers
        ]
    else:
        return "Invalid topic selected."

    # Randomly select a question from the list of questions
    question = random.choice(questions)

    # Display the question and options
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if question['options'][int(user_answer) - 1] == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    selected_topic = input("Enter the topic number (1-4): ")

    # Fetch a random fact or concept for the selected topic
    fact = get_random_fact(selected_topic)
    print(f"Random {topics[selected_topic]} fact: {fact}")

    # Provide an interactive quiz for the selected topic
    quiz(selected_topic)

if __name__ == "__main__":
    main()
