# Program that transcribes speech recorded from microphone

# Returns the following results
#     1. Success - Boolean or not if api request was successful
#     2. Error - None if no error occurred else returns a message containing the error.
#     3. Transcription - None if speech could not be transcribed else returns the transcription



import random
import time

import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be 'Recognizer'")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be 'Microphone'")


    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
            "success" : True,
            "error" : None,
            "transcription":None
            }


    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

if __name__=="__main__":
    WORDS = ["red", "blue", "yellow", "black", "white", "orange"]
    GUESSES = 3
    PROMPT_LIMIT = 5

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    word = random.choice(WORDS)

    instructions = (
            "I'm thinking of these words:\n"
            "{words}\n"
            "You have {n} tries to guess which one.\n"
            ).format(words=', '.join(WORDS), n=GUESSES)

    print(instructions)
    time.sleep(3)

    for i in range(GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer,microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Sorry, I did not get that. Can you please repeat ?\n")

        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        print("You said: {}".format(guess["transcription"]))

        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < GUESSES - 1

        if guess_is_correct:
            print("Correct! You win!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect, Try again.\n")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.format(word)")
            break
