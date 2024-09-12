# chatbot.py
# Dependencies: transformers
# Install with: pip install transformers

from transformers import pipeline

def chat():
    chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chatbot(user_input)
        print(f"Bot: {response['generated_text']}")

if __name__ == "__main__":
    chat()
