#!/usr/bin/python3

import speech_recognition as sr
import base64
from utility import generate_filename
from os import path, remove

# Put the name of the audio file you want to read here if not using this as a module
AUDIO_FILE_NAME = ""
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), AUDIO_FILE_NAME)

class SpeechToText:
    r = sr.Recognizer()

    @classmethod
    def SphinxTranslation(cls, base64Audio):
        decoded_audio = base64.b64decode(base64Audio)
        temp_audio_file = generate_filename()
        with open(temp_audio_file, mode='bx') as f:
            f.write(decoded_audio)

        with sr.AudioFile(temp_audio_file) as source:
            audio = cls.r.record(source)

        try:
            text_from_audio = cls.r.recognize_sphinx(audio)
            print("Sphinx thinks you said " + text_from_audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        
        remove(temp_audio_file)

        return text_from_audio
        
if __name__ == "__main__":
    stt = SpeechToText()
    f = open(AUDIO_FILE, "rb")
    encoded_audio = base64.b64encode(f.read())
    stt.SphinxTranslation(encoded_audio)
    