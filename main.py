import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robo Speaker")

while True:
    word = input("Enter what you want to say: ")
    
    if word.lower() == "exit":
        engine.say("Goodbye")
        engine.runAndWait()
        break

engine.say(word)
