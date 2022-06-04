# Speech Recognition with Python

Found this amazing tutorial so implementing it.

    http://realpython.com/python-speech-recognition/


Here is the author's repo

    http://github.com/realpython/python-speech-recognition

## Contents

The contents are as follows:

* [Prerequisites](#prerequisites)
    * [For microphone use](#for-microphone-use)
    * [For speech recognition](#for-speech-recognition)
* [Speech Engine](#speech-engine)
    * [Smoke Test](#smoke-test)
    * [Ambient Noise](#ambient-noise)
* [Speech testing](#speech-testing)
* [And finally, the guessing game](#and-finally-the-guessing-game)

## Prerequisites

Python 3 and `pip` installed.

#### For microphone use

1. Check for `pyaudio`:

    ``` Python
    >>> import pyaudio as pa
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named pyaudio
    >>>
    ```

[The next step is for linux; check the [pyaudio requirements](http://people.csail.mit.edu/hubert/pyaudio/#downloads) first.]

2. Install `python-pyaudio`: ( I use arch btw so using pacman )

    ```
    $ sudo pacman -S python-pyaudio
    ```

    Or use pip :

    ```
    $ pip install --user pyaudio
    ```

3. Verify installation:

    ``` Python
    >>> import pyaudio as pa
    >>> pa.__version__
    '0.2.11'
    >>>
    ```

#### For speech recognition

SpeechRecognition can be used as a _sound recorder_:

    http://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

This is probably fine for occasional use - but there are better options available.

1. Check for `SpeechRecognition`:

    ```
    $ pip list --format=freeze | grep SpeechRecognition
    ```

2. Install `SpeechRecognition`:

    ```
    $ pip install --user SpeechRecognition
    ```

3. Verify:

    ``` Python
    >>> import speech_recognition as sr
    >>> sr.__version__
    '3.8.1'
    >>>
    ```


## Speech Engine

The tutorial provides multiple options but I have used the __Google Web Speech API__.


#### Smoke Test

The final step may take a few seconds to execute:

``` Python
>>> import speech_recognition as sr
>>> r = sr.Recognizer()
>>> harvard = sr.AudioFile('audio_files/harvard.wav')
>>> with harvard as source:
...     audio = r.record(source)
...
>>> type(audio)
<class 'speech_recognition.AudioData'>
>>> r.recognize_google(audio)
u'the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health and zest a salt pickle taste fine with ham tacos al Pastore are my favorite a zestful food is the hot cross bun'
>>>
```

#### Ambient Noise

``` Python
>>> jackhammer = sr.AudioFile('audio_files/jackhammer.wav')
>>> with jackhammer as source:
...     audio = r.record(source)
...
>>> r.recognize_google(audio)
u'the snail smell of old beer drinkers'
>>> with jackhammer as source:
...     r.adjust_for_ambient_noise(source)
...     audio = r.record(source)
...
>>> r.recognize_google(audio)
u'still smell old gear vendors'
>>>
```

[Slightly different from the tutorial's `the snail smell of old gear vendors` and `still smell of old beer vendors`.]

And:

``` Python
>>> with jackhammer as source:
...     r.adjust_for_ambient_noise(source, duration=0.5)
...     audio = r.record(source)
...
>>> r.recognize_google(audio)
u'the snail smell like old beermongers'
>>>
```

[Pretty much the same as `the snail smell like old Beer Mongers`.]


## Speech testing

Using the speech recognition module:

    $ python -m speech_recognition
    A moment of silence, please...
    Set minimum energy threshold to 259.109953712
    Say something!
    Got it! Now to recognize it...
    You said hello hello
    Got it! Now to recognize it...
    You said the rain in Spain
    Say something!
    ^C$

And:

``` Python
>>> with mic as source:
...     audio = r.listen(source)
...
>>> r.recognize_google(audio)
u'Shazam'
>>>
```

And, as stated in the article, a loud hand-clap generates an exception:

``` Python
>>> with mic as source:
...     audio = r.listen(source)
...
>>> r.recognize_google(audio)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/owner/.local/lib/python2.7/site-packages/speech_recognition/__init__.py", line 858, in recognize_google
    if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()
speech_recognition.UnknownValueError
>>>
```


## And finally, the guessing game

Run the guessing game as follows:

    $ python guessing_game.py
    I'm thinking of one of these words:
    red, blue, yellow, black, white, orange
    You have 3 tries to guess which one.

    Guess 1. Speak!
    You said: violet
    Incorrect. Try again.

    Guess 2. Speak!
    You said: lavender
    Incorrect. Try again.

    Guess 3. Speak!
    You said: purple
    Sorry, you lose!
    I was thinking of 'red'.
