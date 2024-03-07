import speech_recognition
import speech_recognition as sr
import pyaudio
import pyttsx3

recognizer = sr.Recognizer()

while True:

    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Say something.....")
            audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized text here: {text}")
        except Exception as e:
            print("Speech recognition error:", e)

    except KeyboardInterrupt:
        print("Exiting...")
    break
