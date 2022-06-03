#Install pyaudio

import speech_recognition as sr

r = sr.Recognizer()

# This is how you use default mic
mic = sr.Microphone()

# To see which other mics are available
# print(sr.Microphone.list_microphone_names())

# To select third from the ones listed above
# sr.Microphone(device_index=3)


#Using listen to capture microphone input
try:
    with mic as source:
        r.adjust_for_ambient_noise(source)   # Handling ambient noise
        audio = r.listen(source)
        text=r.recognize_google(audio)
        print(text)
except sr.UnknownValueError as error:
    print("Sorry, didn't get that.")
