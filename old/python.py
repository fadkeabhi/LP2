from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
bot = ChatBot('UniversityBot')

# Train the chatbot with questions and answers for universities in Maharashtra
trainer = ListTrainer(bot)
trainer.train([
    "Which university is good for B.Tech in Mumbai?",
    "There are several good universities in Mumbai. Some of the top ones include IIT Bombay, University of Mumbai, and Mumbai University Institute of Chemical Technology.",
    "Can you provide some details about IIT Bombay?",
    "Indian Institute of Technology (IIT Bombay) is one of the top universities in Mumbai. It is a public technical and research university established in 1958. The university offers various courses including B.Tech in Computer Science and Engineering.",
    "What is the cutoff for IIT Bombay in JEE-Advanced 2023?",
    "The cutoff for IIT Bombay in JEE-Advanced 2023 was 170.",
    "Can you provide some details about University of Mumbai?",
    "University of Mumbai is a public state university established in 1857. It offers various undergraduate and postgraduate courses in various fields.",
    "Can you provide some details about Mumbai University Institute of Chemical Technology?",
    "Mumbai University Institute of Chemical Technology is a public university established in 1933. It offers various undergraduate and postgraduate courses in chemical engineering and technology.",
    "What is the cutoff for Mumbai University Institute of Chemical Technology in JEE-Main 2023?",
    "The cutoff for Mumbai University Institute of Chemical Technology in JEE-Main 2023 was 6000."
])

# Get user input and let the chatbot respond
print("Ask me a question about universities in Mumbai:")
while True:
    try:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print("Bot:", response)
    except KeyboardInterrupt:
        break