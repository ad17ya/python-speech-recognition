import speech_recognition as sr

print("Speech Recognition Package version")
print(sr.__version__)


# creating a recognizer class
r = sr.Recognizer()


# This fails since it requires an audio file as an argument
# r.recognize_google()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source) # recrod method records the data from the entire file

# Let's check whats the type of the audio file that we recorded
audio_type = type(audio)
print("Type of audio that we recorded is ", audio_type)

# Transcribing the file and printing the result
text = r.recognize_google(audio)
print("Transcribing the whole file")
print(text)



###### Capturing segments with offset and duration ######

duration_time = 4
with harvard as source:
    audio = r.record(source, duration=duration_time)

segment_text = r.recognize_google(audio)
print("\nCapturing segment with duration of ", duration_time ,"seconds")
print(segment_text)


# Record method when used inside a block moves ahead when caputring two different times.

with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)

text1 = r.recognize_google(audio1)
text2 = r.recognize_google(audio2)


print("\nRecord method when used inside a block continues to record further and doesn't reset")
print(text1)
print(text2)


# Using the offset keyword

with harvard as source:
    audio = r.record(source, offset=4, duration=3)

text = r.recognize_google(audio)


print("\nUsing the offset keyword")
print(text)

# Offset is mostly used when we already know the structure of the file

print ("Bad usage of offset when values set to 4.7 and duration is 2.8")
with harvard as source:
    audio = r.record(source, offset=4.7, duration=2.8)

text = r.recognize_google(audio)
print(text)

print("\nThis leads to mismatching because of using bad offset values it might miss parts of some words and match the rest of the word with the other one")


###### How does noise affect here? ######
# Using the jackhammer.wav file here since it has some noise in it.

jackhammer = sr.AudioFile('jackhammer.wav')

with jackhammer as source:
    audio_noise = r. record(source)

text = r.recognize_google(audio_noise)
print("\nWhat if the audio file contains some noise")
print(text)



# Trying the adjust_for_ambient_noise() method to fix this

with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    audio_adjusted = r.record(source)

# text = r.recognize_google(audio_adjusted)

# If the above method doesn't work the below works
# text=r.recognize_google(audio_adjusted, language='en-IN', show_all=True)

print("\nAfter using the adjust for ambient noise method on the source file")
print(text)


# the time frame that adjust_for_ambient_noise() uses for analysis with the duration keyword
# it takes numerical value and is set to 1 by default

with jackhammer as source:
    r.adjust_for_ambient_noise(source, duration=2)
    audio_adjusted = r.record(source)

# To see the list of all possible transcripts add the show_all argument as well
text = r.recognize_google(audio_adjusted, show_all=True)
print("\nUsing duration with adjust_for_ambient_noise")
print(text)
