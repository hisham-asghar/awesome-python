
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
            "The first confirmed meteorite impact in the United States occurred in 1807 in Weston, Connecticut.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The world's first programmable computer was the ENIAC, completed in 1946.",
            "The first commercial microprocessor was the Intel 4004, released in 1971."
        ],
        "history": [
            "The Pyramids of Giza were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Great Wall of China was built over centuries, beginning in the 3rd century BC."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters tall.",
            "The largest ocean on Earth is the Pacific Ocean."
        ]
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the given topic, using a public API or predefined database.
    """
    if topic == "science":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=17&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return question, choices
    elif topic == "technology":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return question, choices
    elif topic == "history":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=23&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
        return question, choices
    elif topic == "general":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=9&type=multiple")
        data = response.json()
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

    topic_choice = input("Enter the number of your choice: ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting...")
        return

    print("\nHere's a random fact about", topic + ":")
    print(get_random_fact(topic))

    print("\nNow let's test your knowledge with a quiz!")
    question, choices = quiz_question(topic)
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = input("Enter the number of your answer: ")
    if choices[int(user_answer) - 1] == quiz_question(topic)[1][-1]:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
