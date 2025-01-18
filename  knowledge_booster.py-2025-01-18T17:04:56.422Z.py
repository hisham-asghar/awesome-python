
import random
import requests
import json

# Define the topics and associated facts/concepts
topics = {
    "science": [
        ("The human body has around 60,000 miles of blood vessels.", "The total length of blood vessels in the human body is estimated to be around 60,000 miles, which is enough to circle the Earth twice."),
        ("Ants can lift 50 times their own body weight.", "Ants are incredibly strong for their size, with the ability to lift up to 50 times their own body weight."),
        ("The Earth is the only planet in our solar system with liquid water on its surface.", "The presence of liquid water on Earth's surface is a key factor that makes it habitable for life as we know it.")
    ],
    "technology": [
        ("The first computer virus was created in 1983.", "The first computer virus, known as the 'Brain' virus, was created in 1983 by two brothers in Pakistan."),
        ("The internet was originally created for military communication.", "The internet was initially developed as a network for military communication, known as ARPANET, in the 1960s."),
        ("The first mobile phone call was made in 1973.", "The first mobile phone call was made by Martin Cooper of Motorola in 1973, using a prototype device that weighed nearly 2 pounds.")
    ],
    "history": [
        ("The Great Wall of China is the longest man-made structure in the world.", "The Great Wall of China, built over centuries, is the longest man-made structure in the world, stretching approximately 13,171 miles (21,196 km)."),
        ("The Pyramids of Giza were built over a period of 20 years.", "The three major pyramids at Giza, the largest of which is the Great Pyramid, were built over a period of around 20 years during the reign of the pharaoh Khufu (also known as Cheops)."),
        ("The first public library was established in ancient Athens.", "The first known public library was established in ancient Athens, Greece, around 5th century BC, providing access to books and scrolls for the general public.")
    ],
    "general": [
        ("The tallest mammal is the giraffe.", "The giraffe is the tallest living terrestrial animal, with males reaching heights of up to 6 meters (20 feet)."),
        ("The largest ocean on Earth is the Pacific Ocean.", "The Pacific Ocean is the largest and deepest of the world's five oceans, covering an area of approximately 63 million square miles."),
        ("The Nobel Prizes were first awarded in 1901.", "The Nobel Prizes, which recognize outstanding achievements in various fields, were first awarded in 1901, as specified in the will of Alfred Nobel.")
    ]
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    print()

def get_random_fact(topic):
    if topic not in topics:
        print("Invalid topic. Please try again.")
        return None
    
    fact, explanation = random.choice(topics[topic])
    print(f"Random fact about {topic.capitalize()}: {fact}")
    print(f"Explanation: {explanation}")
    print()
    return fact, explanation

def quiz_question(topic):
    if topic not in topics:
        print("Invalid topic. Please try again.")
        return None
    
    fact, explanation = random.choice(topics[topic])
    options = ["A", "B", "C", "D"]
    correct_answer = options[0]
    
    print(f"Quiz question about {topic.capitalize()}:")
    print(fact)
    print()
    
    for i in range(1, len(options)):
        option = options[i]
        print(f"{option}) {random.choice(topics[topic])[0]}")
    
    print(f"{correct_answer}) {fact}")
    
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer == correct_answer:
        print("Correct! You're a knowledge master.")
    else:
        print("Incorrect. Better luck next time!")
    print()

def main():
    display_menu()
    topic = input("Enter a topic: ").lower()
    get_random_fact(topic)
    quiz_question(topic)

if __name__ == "__main__":
    main()
