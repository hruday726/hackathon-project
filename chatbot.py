# AI Chatbot for Customer Support

responses = {
    "hello": "Hi! How can I help you today?",
    "help": "I can assist with orders, billing, or product info. What do you need?",
    "order": "To track your order, please provide your order ID.",
    "billing": "For billing issues, contact our support team at support@company.com",
    "thanks": "You're welcome! Anything else?",
    "bye": "Goodbye! Have a great day!",
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm not sure about that. Can you rephrase?"

# Main loop
print("🤖 Welcome to Customer Support Chatbot")
print("Type 'bye' to exit\n")

while True:
    user_msg = input("You: ")
    if user_msg.lower() == "bye":
        print("Bot: Goodbye!")
        break
    
    response = chatbot_response(user_msg)
    print(f"Bot: {response}\n")