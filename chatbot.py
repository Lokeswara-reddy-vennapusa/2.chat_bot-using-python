import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

chatbot_responses = [
    (r'hi|hello', ['Hello!', 'Hi there!']),
    (r'how are you?', ["I'm just a computer program, but I'm doing well. How can I assist you?"]),
    (r'what is your name?', ["I'm a chatbot. You can call me ChatGPT."]),
    # Add more patterns and responses here
]

chatbot = Chat(chatbot_responses, reflections)

print("Hello! I'm your chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    print("ChatGPT:", response)
