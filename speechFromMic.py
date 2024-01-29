import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record():
    # Loop in case speech isnt picked up
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0.2)

                # Listens to mic input
                audio = r.listen(source)

                # recognizes audio
                rec_text = r.recognize_google(audio)

                return rec_text
            
        except sr.RequestError as e:
            print(f"Cant return results; {e}")
        
        except sr.UnknownValueError:
            print("Unknown error")

    return

def output(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record()
    output(text)