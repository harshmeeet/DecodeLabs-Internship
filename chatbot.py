print("================================")
print(" Welcome to DecodeBot 🤖")
print(" Type 'exit' to quit")
print("================================")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey!",
    "how are you": "I am doing great!",
    "who are you": "I am DecodeBot.",
    "your name": "I am DecodeBot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who created you": "I was created using Python.",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "help": "Try: hello, hi, how are you, your name, what is ai, joke, bye, exit",
    "bye": "Goodbye!"
}

while True:

    user_input = input("\nYou: ")

    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Bot: Exiting chatbot...")
        break

    response = responses.get(
        clean_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", response)