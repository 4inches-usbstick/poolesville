"""
High-tier computer science sh*tposting.

Through text-to-speech, says a plethora of flavorful profanity and colorful \
    language, given the user says the word "Poolesville."
To the Magnet admission office, this one is for you. It barely works, just \
    like you. <3
"""

import speech_recognition as sr

recognition = sr.Recognizer()
microphone = sr.Microphone(
    sr.Microphone.list_microphone_names().index("pulse"))

with microphone as stream:
    recognition.adjust_for_ambient_noise(stream)
    data = recognition.listen(stream)
    print(recognition.recognize_sphinx(data))
    if data.split(" ")[0][1:] in ["ool", "ools"]:
        # TTS here
        pass
