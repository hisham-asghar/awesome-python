Here is the raw Python code without any additional commentary:

import random
import json
import requests

def get_random_fact(topic):
    api_url = f"https://uselessfacts.jsph.pl/random.json?category={topic}"
    response = requests.get(api_url)
    data = response.json()
    return data["text"]

def run_quiz(topic):
    if topic == "science":
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    else:
        pass

    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    topics = ["science", "technology", "history", "general"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic.capitalize()}")

    topic_choice = int(input("Enter your choice (1-4): ")) - 1
    selected_topic = topics[topic_choice]
    print(f"You have chosen: {selected_topic.capitalize()}")

    print("Here's a random fact or concept about the topic:")
    fact = get_random_fact(selected_topic)
    print(fact)

    print("Now, let's test your knowledge with a quiz!")
    run_quiz(selected_topic)

    print("Thank you for using the Interactive Knowledge Builder!")

if __name__ == "__main__":
    main()