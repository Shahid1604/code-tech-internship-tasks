from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["what is your name", ["I am a CODTECH Chatbot."]],
    ["how are you", ["I'm doing great!"]],
    ["what is python", ["Python is a programming language."]],
    ["bye", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)
print("Chatbot is running... (type 'bye' to exit)")
chatbot.converse()
