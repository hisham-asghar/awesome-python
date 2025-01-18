
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
            "The sun is about 93 million miles away from the Earth.",
            "Diamonds are made from compressed carbon that has been exposed to extreme heat and pressure."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The internet was originally called ARPANET and was created in 1969.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The first written language was Sumerian cuneiform, which emerged in Mesopotamia around 3400 BC."
        ],
        "general": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of flamingos is called a flamboyance."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, I don't have any facts for that topic in my database."

def get_trivia_question(topic):
    """
    Fetches a random trivia question and multiple-choice answers from a public API for the given topic.
    """
    api_url = f"https://opentdb.com/api.php?amount=1&category={topic}&type=multiple"
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    if data["response_code"] == 0:
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(answers)
        return question, answers
    else:
        return "Sorry, I couldn't fetch a trivia question for that topic.", []

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = input("Enter the number of your chosen topic: ")
    
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
    
    print("\nHere's a random fact or concept about", topic + ":")
    print(get_random_fact(topic))
    
    print("\nNow let's test your knowledge with a trivia question!")
    question, answers = get_trivia_question(topic)
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = input("Enter the number of the correct answer: ")
    if answers[int(user_answer) - 1] == data["results"][0]["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", data["results"][0]["correct_answer"])

if __name__ == "__main__":
    main()
