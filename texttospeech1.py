from gtts import gTTS
import os
def test():
    x = open("D:\workspace\codes\Texttospeech1.txt", "r+").read().replace("\n", " ")
    y = "en"
    z = gTTS(text = str(x), lang = y, slow = False)
    z.save("Texttospeech1.mp3")
test()
