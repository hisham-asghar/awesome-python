
import random
import requests
import json

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter the number of your choice: ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == "Science":
        facts = [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Cats have fewer toes on their back paws than their front paws."
        ]
    elif topic == "Technology":
        facts = [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial email service was launched by CompuServe in 1979.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ]
    elif topic == "History":
        facts = [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta was signed in 1215, establishing the principle that everyone is subject to the law, even the king.",
            "The French Revolution began in 1789 with the Storming of the Bastille."
        ]
    elif topic == "General Knowledge":
        facts = [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), exceeding the 2 mph (3.2 km/h) speed limit."
        ]
    return random.choice(facts)

# Function to display a quiz with multiple-choice questions
def quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == "Science":
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    elif topic == "Technology":
        questions = [
            {
                "question": "What is the name of the first programmable computer?",
                "choices": ["ENIAC", "UNIVAC", "MARK I", "Z1"],
                "answer": "ENIAC"
            },
            {
                "question": "Which company developed the first commercial web browser?",
                "choices": ["Microsoft", "Apple", "Netscape", "Google"],
                "answer": "Netscape"
            },
            {
                "question": "What is the name of the first commercial smartphone?",
                "choices": ["iPhone", "BlackBerry", "Sidekick", "Simon"],
                "answer": "Simon"
            }
        ]
    # Add more questions for other topics as needed

    # Display the quiz and get the user's answers
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter the number of your answer: ")
        if question["choices"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions)}.")

# Main function to run the interactive knowledge booster
def main():
    choice = display_menu()
    topic = topics[choice]
    print(f"\nYou have selected: {topic}")
    print(get_random_fact(topic))
    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
