
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the chosen topic.
    """
    if topic == "Science":
        # Fetch a random science fact from an API or database
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "Technology":
        # Fetch a random technology fact from an API or database
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "History":
        # Fetch a random history fact from an API or database
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "General Knowledge":
        # Fetch a random general knowledge fact from an API or database
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general")
        facts = response.json()
        return random.choice(facts)["fact"]
    else:
        return "Sorry, I don't have any information for that topic."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the chosen topic.
    """
    if topic == "Science":
        # Fetch science-related quiz questions and answers from an API or database
        response = requests.get("https://opentdb.com/api.php?amount=5&category=17&type=multiple")
        quiz_data = response.json()["results"]
        for question in quiz_data:
            print(question["question"])
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer-1] == question["correct_answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}")
            print()
    elif topic == "Technology":
        # Fetch technology-related quiz questions and answers from an API or database
        response = requests.get("https://opentdb.com/api.php?amount=5&category=18&type=multiple")
        quiz_data = response.json()["results"]
        for question in quiz_data:
            print(question["question"])
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer-1] == question["correct_answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}")
            print()
    elif topic == "History":
        # Fetch history-related quiz questions and answers from an API or database
        response = requests.get("https://opentdb.com/api.php?amount=5&category=23&type=multiple")
        quiz_data = response.json()["results"]
        for question in quiz_data:
            print(question["question"])
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer-1] == question["correct_answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}")
            print()
    elif topic == "General Knowledge":
        # Fetch general knowledge-related quiz questions and answers from an API or database
        response = requests.get("https://opentdb.com/api.php?amount=5&category=9&type=multiple")
        quiz_data = response.json()["results"]
        for question in quiz_data:
            print(question["question"])
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer-1] == question["correct_answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}")
            print()
    else:
        print("Sorry, I don't have any quiz information for that topic.")

def main():
    """
    Main function to run the interactive knowledge-boosting script.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")
    
    topic_choice = int(input("Enter the number of the topic you want to explore: "))
    
    if topic_choice in topics:
        topic = topics[topic_choice]
        print(f"\nHere's a random fact about {topic}:")
        print(get_random_fact(topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(topic)
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
