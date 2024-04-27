import pyttsx3
import os


if __name__ == "__main__":
    print("\n                                  Welcome to Robospeaker 1.1 Created by Sam")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to speak : ")
        if x == "q":
            y = "Good bye"
            engine.say(y)
            engine.runAndWait()

            break


        engine.say(x)
        engine.runAndWait()
 