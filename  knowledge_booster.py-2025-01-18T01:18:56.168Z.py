
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The sun is a star at the center of the solar system.",
            "DNA is the genetic material that carries the instructions for the development and functioning of living organisms.",
            "The human brain has around 86 billion neurons."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "Artificial intelligence (AI) is the simulation of human intelligence processes by machines."
        ],
        "history": [
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Roman Empire was one of the largest and most influential civilizations in history.",
            "The Renaissance was a cultural movement that began in Italy in the 14th century."
        ],
        "general": [
            "The tallest mammal is the giraffe.",
            "The Great Wall of China is the longest man-made structure in the world.",
            "The largest ocean on Earth is the Pacific Ocean."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, we don't have any facts for that topic."

def get_trivia_question(topic):
    """
    Fetches a multiple-choice trivia question and its answers from a public API for the given topic.
    """
    api_url = f"https://opentdb.com/api.php?amount=1&category={get_category_id(topic)}&type=multiple"
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    if data["response_code"] == 0:
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(answers)
        return question, answers
    else:
        return "Sorry, we couldn't fetch a trivia question for that topic.", []

def get_category_id(topic):
    """
    Maps the given topic to the corresponding category ID used by the trivia API.
    """
    category_ids = {
        "science": 17,
        "technology": 18,
        "history": 23,
        "general": 9
    }
    
    if topic in category_ids:
        return category_ids[topic]
    else:
        return 0

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
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
        print("Invalid choice. Exiting.")
        return
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_random_fact(topic))
    
    print("\nNow, let's test your knowledge with a trivia question!")
    question, answers = get_trivia_question(topic)
    print(question)
    
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = input("Enter the number of your answer: ")
    
    if int(user_answer) == answers.index(answers[-1]) + 1:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
