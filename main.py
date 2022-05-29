import speech_recognition as sr

print(sr.__version__)


# creating a recognizer class
r = sr.Recognizer()


# This fails since it requires an audio file as an argument
# r.recognize_google()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
        audio = r.record(source) # recrod method records the data from the entire file

# Let's check whats the type of the audio file that we recorded
print(type(audio))

# Transcribing the file and printing the result
text = r.recognize_google(audio)
print(text)
