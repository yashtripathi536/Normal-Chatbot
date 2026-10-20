# Basic Rule-Based Chatbot - CodeAlpha Task 4

EXIT_WORDS = ("bye", "goodbye", "exit")


def get_response(user_input):
    """Return a reply based on what the user typed."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text in ("what is your name", "your name", "who are you"):
        return "I'm CodeBot, a simple Python chatbot."
    elif text in ("thanks", "thank you"):
        return "You're welcome!"
    elif text == "help":
        return "Try saying: hello, how are you, your name, thanks, or bye."
    elif text in EXIT_WORDS:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    print("=== CodeBot ===")
    print("Type 'help' for options. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("CodeBot: Please type something.")
            continue

        reply = get_response(user_input)
        print("CodeBot:", reply)

        if user_input.lower().strip() in EXIT_WORDS:
            break


if __name__ == "__main__":
    main()