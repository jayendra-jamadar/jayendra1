import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a chatbot, so I don't have feelings, but thanks for asking!", "I'm here to help."],
    "bye": ["Goodbye!", "See you later!", "Farewell!"],
    "i have a problem":["Sure i am here to solve it,is it legal, market related etc"],
    "legal":["Advice etc"],
    "market":["Advice etc"],
    "default": ["Sorry I dont hold this information right now.", "Could you please rephrase that?", "Sorry, I don't have this information right now ."]
}

def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])
    
while True:
    user_input = input("You: ")
    if user_input.lower() == "thanks":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)