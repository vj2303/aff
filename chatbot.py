# import json

# def load_responses(file_path):
#     try:
#         with open(file_path, "r") as file:
#             return json.load(file)
    
#     except FileNotFoundError:
#         print("Responses file not found.")
#         return {}
    
# response_file = "responses.txt"
# responses = load_responses(response_file)

# def chat_response(user_input):
#     if user_input in responses:
#         return responses[user_input]
#     else:
#         return responses.get("Default", "I cannot help you with that")

# print("____Welcome to ChatBot____")
# while True:
#     user_input = input("You: ").strip()
#     if user_input.lower() == 'bye':
#         print("ChatBot: Goodbye!")
#         break
#     result = chat_response(user_input)
#     print("ChatBot: ", result)

import json

def load_responses(file_path):
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found.")
        return {}
    
responses_path = "responses.txt" 
responses = load_responses(responses_path)

def bot_response(user_input):
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["Default"]
    
print("____Welcome to ChatBot____")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye!")
        break
    result = bot_response(user_input)
    print("ChatBot: ",result)