import random
import requests
import json

def get_topic_info(topic):
    """
    Fetches information about the selected topic from a predefined database or public API.
    """
    topic_data = {
        "science": {
            "description": "Learn about the latest discoveries and advancements in science.",
            "facts": [
                "The human body has around 60,000 miles of blood vessels.",
                "Bananas are slightly radioactive.",
                "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
            ],
            "questions": [
                {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
                {"question": "Which planet in our solar system has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": 0},
                {"question": "What is the process of turning a liquid into a gas called?", "options": ["Condensation", "Evaporation", "Sublimation", "Boiling"], "answer": 1}
            ]
        },
        "technology": {
            "description": "Explore the latest advancements in technology and how they impact our lives.",
            "facts": [
                "The first computer mouse was invented in 1964 and had only one button.",
                "The world's first text message was sent on December 3, 1992.",
                "The first commercial jet flight took place in 1952."
            ],
            "questions": [
                {"question": "What is the name of the programming language created by Guido van Rossum?", "options": ["Java", "C++", "Python", "Ruby"], "answer": 2},
                {"question": "Which company developed the first commercially successful smartphone?", "options": ["Apple", "Samsung", "BlackBerry", "Nokia"], "answer": 2},
                {"question": "What is the name of the first web browser created by Tim Berners-Lee?", "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"], "answer": 3}
            ]
        },
        "history": {
            "description": "Dive into the fascinating stories and events that shaped our world.",
            "facts": [
                "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
                "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
                "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
            ],
            "questions": [
                {"question": "Which ancient civilization is known for its advanced mathematics and astronomy?", "options": ["Egyptians", "Greeks", "Mayans", "Chinese"], "answer": 1},
                {"question": "Which event is considered the start of the American Civil War?", "options": ["The Battle of Gettysburg", "The Emancipation Proclamation", "The Assassination of Abraham Lincoln", "The Attack on Fort Sumter"], "answer": 3},
                {"question": "Which famous explorer is credited with discovering America?", "options": ["Christopher Columbus", "Leif Erikson", "Vasco da Gama", "Marco Polo"], "answer": 0}
            ]
        },
        "general": {
            "description": "Explore a wide range of interesting facts and trivia about the world around us.",
            "facts": [
                "The tallest mammal is the giraffe, which can grow up to 18 feet (5.5 meters) tall.",
                "The largest known prime number as of 2022 has 23 million digits.",
                "The first known use of the word \"OK\" was in a Boston newspaper in 1839."
            ],
            "questions": [
                {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 3},
                {"question": "What is the rarest blood type?", "options": ["A", "B", "AB", "O"], "answer": 2},
                {"question": "Which country is known as the "Land of the Rising Sun"?", "options": ["China", "Japan", "South Korea", "Taiwan"], "answer": 1}
            ]
        }
    }
    return topic_data[topic]

def display_topic_info(topic):
    """
    Displays information about the selected topic, including a random fact and an interactive quiz.
    """
    topic_info = get_topic_info(topic)
    print(f"Topic: {topic.capitalize()}")
    print(topic_info["description"])
    print("\nRandom Fact:")
    print(random.choice(topic_info["facts"]))
    print("\nQuiz Time!\n")
    
    questions = topic_info["questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is {question['options'][question['answer']]}.\n")

def main():
    """
    Displays a menu for users to select a topic and then calls the display_topic_info function.
    """
    print("Welcome to the Interactive Knowledge Hub!\n")
    print("Please select a topic:")
    print("1. Science\n2. Technology\n3. History\n4. General Knowledge")
    
    topic_choice = input("Enter your choice (1-4): ")
    
    topics = ["science", "technology", "history", "general"]
    if topic_choice.isdigit() and 1 <= int(topic_choice) <= 4:
        display_topic_info(topics[int(topic_choice) - 1])
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()