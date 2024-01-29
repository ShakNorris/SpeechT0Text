import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

audio_file = "path/to/audio_file.wav"

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile(audio_file) as source:
    
    audio_text = r.listen(source)

    try:
        
        # Using google speech recognition. Supports other languages as well
        text = r.recognize_google(audio_text)
        print('Converting audio into text ...')
        print(text)
     
    except sr.RequestError as e:
            print(f"Cant return results; {e}")