import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Say something.....")
            audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_(audio)
            text = text.lower()

            print(f"Recognized text here: {text}")
        except Exception as e:
            print("Speech recognition error:", e)

    except KeyboardInterrupt:
        print("Exiting...")
    break
