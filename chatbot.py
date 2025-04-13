import random

responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I'm just a bot, but I'm doing fine. Thanks!",
    "bye": "Goodbye! Have a nice day.",
    "default": "I'm sorry, I don't understand that."
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

def chat():
    print("Bot: Hi! I’m a basic chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)

chat()