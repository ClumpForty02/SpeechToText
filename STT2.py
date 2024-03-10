import speech_recognition as sr
import pyaudio
import pyttsx3

recognizer = sr.Recognizer()


def record_text():
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("Say something.....")
                audio = recognizer.listen(mic)
            try:
                text = (recognizer.recognize_google(audio))
                text = text.lower()

                return text
            except Exception as e:
                print("Speech recognition error:", e)

        except KeyboardInterrupt:
            print("Exiting...")
        break


def output_text(text):
    f = open("Output2.txt", "a")  # a means that we want to append the text to the end of the file
    f.write(text)
    f.write("\n")
    f.close()
    return

while 1:
    text = record_text()
    output_text(text)
    print("Text written.")

