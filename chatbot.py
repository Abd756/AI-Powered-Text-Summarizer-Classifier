from modules.assistant import assistant_response

print("Welcome to the AI-Powered Chatbot! Type your message and press Enter. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == 'exit':
        print("Goodbye!")
        break
    response = assistant_response(user_input)
    print(f"Assistant: {response}\n")
