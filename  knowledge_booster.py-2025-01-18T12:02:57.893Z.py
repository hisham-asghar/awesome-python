
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    topics = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains over 200 billion stars.",
            "Diamonds are made from compressed carbon that was formed millions of years ago."
        ],
        "technology": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The internet was originally called ARPANET, and was created in 1969 by the U.S. Department of Defense."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built over a 20-year period, with an estimated 100,000 workers.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "general": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The largest known snowflake was 15 inches wide.",
            "The first person convicted of speeding was going 8 mph."
        ]
    }
    
    if topic in topics:
        return random.choice(topics[topic])
    else:
        return "Sorry, that topic is not available. Please choose from: science, technology, history, or general."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic, fetching questions and answers from a public API.
    """
    if topic == "science":
        url = "https://opentdb.com/api.php?amount=5&category=17&type=multiple"
    elif topic == "technology":
        url = "https://opentdb.com/api.php?amount=5&category=18&type=multiple"
    elif topic == "history":
        url = "https://opentdb.com/api.php?amount=5&category=23&type=multiple"
    elif topic == "general":
        url = "https://opentdb.com/api.php?amount=5&category=9&type=multiple"
    else:
        return "Sorry, that topic is not available. Please choose from: science, technology, history, or general."
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    if data["response_code"] == 0:
        questions = data["results"]
        score = 0
        for question in questions:
            print(question["question"])
            print("A. " + question["incorrect_answers"][0])
            print("B. " + question["incorrect_answers"][1])
            print("C. " + question["incorrect_answers"][2])
            print("D. " + question["correct_answer"])
            
            answer = input("Your answer (A/B/C/D): ").upper()
            if answer == question["correct_answer"][0]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is", question["correct_answer"])
        
        print(f"You scored {score} out of 5 on the {topic} quiz.")
    else:
        return "Sorry, there was an error fetching the quiz questions."

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
        print("Invalid choice. Please try again.")
        return
    
    print("\nHere's a random fact about", topic + ":")
    print(get_random_fact(topic))
    
    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
