def chatbot():
    print("🤖 Welcome! I am a Basic Chatbot.")
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user == "i am fine":
            print("Bot: That's great to hear!")

        elif user == "what is your name":
            print("Bot: My name is Basic Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()