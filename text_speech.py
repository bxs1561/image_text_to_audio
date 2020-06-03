from gtts import gTTS
import os
import pytesseract  # convert image to text
from PIL import Image
import pyttsx3  # s a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
from googletrans import Translator  # translate to language
import speech_recognition as sr


def text_to_speech_use_gTTs():
    # text = "स्वागतम्"
    text = "Hello, how are you doing"
    language = 'en'

    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("speech.mp3")
    print(myobj.get_urls())  # myobj.save("welcome.mp3")

    #
    # os.system("mpg321 welcome.mp3")


# convert image to text and text to voice and save
def comvert_image_text_to_speech():
    image = Image.open("download.jpeg")
    # convert image to string of text
    result = pytesseract.image_to_string(image)
    print(result)
    with open("result.txt", mode='w') as f:
        f.write(result)
    trans = Translator()
    res = trans.translate(result, dest='hindi')

    with open("hindi.text", 'w') as file:
        trans_to_lan = res.text
        file.write(trans_to_lan)

    # save text to speech in file
    with open("result.txt", 'r') as red:
        # print(red.read().strip())
        string = str(red.read())
        print(string)
        myobj = gTTS(text=string, lang="en", slow=False)
        myobj.save('nepali.wav')

    # print(res.text)
    # engine = pyttsx3.init()
    # engine.say(res)
    # engine.runAndWait()

    # speech.runAndWait()

    # print(res)


def text_to_speech_use_pyttsx3():
    speech_convert = pyttsx3.init()
    speech_convert.setProperty('rate', 150)
    speech_convert.setProperty('volume', 0.7)

    # to change voices to boy and girl
    voices = speech_convert.getProperty('voices')  # getting details of current voice

    speech_convert.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    # speech_convert.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    speech_convert.say("Hello I am good")
    speech_convert.say("And you")

    speech_convert.runAndWait()


def audio_to_text():
    # audio = r.AudioFile('speech.mp3')
    #   with audio as source:
    # audio = r.record(source)
    # r.recognize_google(audio)

    Audio_file = ("speech.mp3")
    speech = sr.Recognizer()
    with sr.AudioFile(Audio_file) as src:
        audio = speech.record(src)
    try:
        print("The audio file contains: " + speech.recognize_google(audio))
    except:
        pass


def speech_recognization():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        print("Time over,thanks")
    try:
        # print("TEXT: " + r.recognize_google(audio, language="en"));
        print("TEXT: " + r.recognize_google(audio))
    #
    except:
        print("Sorry could not recognize your voice")

        pass


def main():
    speech_recognization()
    # audio_to_text()
    # text_to_speech_use_pyttsx3()
    # comvert_image_text_to_speech()
    # text_to_speech_use_gTTs()


if __name__ == '__main__':
    main()
