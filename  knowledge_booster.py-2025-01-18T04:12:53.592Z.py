
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first digital computer, ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "technology": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The term 'bug' was first used in computing in 1947 when a moth was found stuck in a Harvard Mark II computer.",
            "The world's first text message was sent on December 3, 1992, and read 'Merry Christmas'."
        ],
        "history": [
            "The ancient Egyptians built the pyramids as tombs for their pharaohs.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Magna Carta, signed in 1215, was a landmark document that limited the power of the English monarchy."
        ],
        "general": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Italy to shave them off.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the given topic using a public API.
    """
    # Replace the API endpoint with a real one that provides trivia questions
    api_url = f"https://opentdb.com/api.php?amount=1&category={topic.upper()}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    question = data["results"][0]["question"]
    choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
    random.shuffle(choices)
    return question, choices

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = input("Enter your choice (1-4): ")
    
    topics = ["science", "technology", "history", "general"]
    
    if topic_choice.isdigit() and 1 <= int(topic_choice) <= 4:
        topic = topics[int(topic_choice) - 1]
        print(f"\nHere's a random fact about {topic}:")
        print(get_random_fact(topic))
        
        print(f"\nNow let's test your {topic} knowledge with a quiz!")
        question, choices = quiz_question(topic)
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4 and choices[int(user_answer) - 1] == data["results"][0]["correct_answer"]:
            print("Correct! You're a knowledge champion!")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
