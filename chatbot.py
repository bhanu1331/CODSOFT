def chatresponse(x):
    x = x.lower()

    travels = ["travel", "trip", "vacation", "places"]
    thanks = ["thank", "thanks", "appreciate"]
    foodpreferences = ["hungry", "food", "eat", "craving"]
    confirmations = ["yes", "yeah", "yup", "yep", "of course"]
    salutations = ["hello", "hi", "hola", "hey"]
    questions = ["how are you", "what's up", "how's life"]
    farewells = ["bye", "goodbye", "see you", "later"]

    if any(word in x for word in salutations):
        return "Hi! What can I do for you?"
    elif any(word in x for word in foodpreferences):
        return "Hungry, huh? Let's explore some tasty dishes together!"
    elif any(word in x for word in travels):
        return "Planning your next adventure? Let's explore some exciting destinations!"
    elif any(word in x for word in questions):
        return "Everything's going smoothly! How about you?"
    elif any(word in x for word in confirmations):
        return "Perfect! That's exactly what I needed to know."
    elif any(word in x for word in farewells):
        return "Goodbye! Have a great day!"
    elif any(word in x for word in thanks):
        return "You're welcome!"
    else:
        return "Sorry, I didn’t understand. Can you rephrase?"

def main():
    print("Welcome to the chatbot!")
    print("Type 'quit' to exit.")

    while True:
        x = input("You: ")

        if x.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", chatresponse(x))

if __name__ == "__main__":
    main()
