
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Define the quiz questions and answers for each topic
quiz_data = {
    "Science": [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Saturn", "Mars"],
            "answer": 1
        },
        {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
            "answer": 0
        },
        # Add more science quiz questions here
    ],
    "Technology": [
        {
            "question": "What is the name of the first computer programming language?",
            "options": ["FORTRAN", "COBOL", "BASIC", "Ada"],
            "answer": 0
        },
        {
            "question": "What is the primary purpose of a web browser?",
            "options": ["To send emails", "To play games", "To access websites", "To write code"],
            "answer": 2
        },
        # Add more technology quiz questions here
    ],
    "History": [
        {
            "question": "In what year did the American Civil War begin?",
            "options": ["1861", "1865", "1914", "1945"],
            "answer": 0
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
            "answer": 2
        },
        # Add more history quiz questions here
    ],
    "General Knowledge": [
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
            "answer": 3
        },
        # Add more general knowledge quiz questions here
    ]
}

def get_random_fact(topic):
    """
    Fetch a random fact from the specified topic using the API or predefined data.
    """
    if topic in topics:
        response = requests.get(topics[topic], headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        if response.status_code == 200:
            facts = response.json()
            return random.choice(facts)['fact']
        else:
            return "Error fetching facts."
    else:
        return "Invalid topic."

def run_quiz(topic):
    """
    Run a quiz for the specified topic, with multiple-choice questions.
    """
    if topic in quiz_data:
        score = 0
        for question in quiz_data[topic]:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question['answer'] + 1:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"Your final score: {score}/{len(quiz_data[topic])}")
    else:
        print("Invalid topic.")

def main():
    """
    Display the topic menu, get user input, and run the corresponding functionality.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    print(f"\nYour selected topic: {selected_topic}")
    print(get_random_fact(selected_topic))

    print("\nNow let's test your knowledge with a quiz!")
    run_quiz(selected_topic)

    print("\nThank you for using the Interactive Knowledge Booster!")

if __name__ == "__main__":
    main()
