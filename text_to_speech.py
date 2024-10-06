import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

    def speak(self, text, voice_choice):
        if voice_choice == 1:
            self.engine.setProperty('voice', self.voices[0].id)  # US Male
        elif voice_choice == 2:
            self.engine.setProperty('voice', self.voices[1].id)  # UK Female
        elif voice_choice == 3:
            self.engine.setProperty('voice', self.voices[2].id)  # US Female
        self.engine.say(text)
        self.engine.runAndWait()
