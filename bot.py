# chatbot.py
from responses import responses

def chatbot_response(input_text):
    # Convert the input to lowercase for case-insensitive matching
    input_text = input_text.lower()

    # Check if the input text matches any predefined responses
    if input_text in responses:
        return responses[input_text]
    else:
        return responses["default"]

# Chatbot interaction loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)







