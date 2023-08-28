import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def voice_assistant():
    with sr.Microphone() as source:
        print("Listening... Speak something:")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio).lower()
            print("You said:", user_input)

            if "hello" in user_input:
                response = "Hello! How can I help you?"
            elif "how are you" in user_input:
                response = "I'm just a program, but I'm here to assist you!"
            else:
                response = "Sorry, I didn't understand that."

            print("Assistant:", response)
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
    voice_assistant()