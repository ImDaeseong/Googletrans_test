import os

from googletrans import Translator
from gtts import gTTS
import playsound


def speaken(text):
    tts = gTTS(text=text, lang='en')

    # 임시 음성 파일 저장
    tts.save("output.mp3")

    # 음성 파일 재생
    playsound.playsound("output.mp3")


def speakko(text):
    tts = gTTS(text=text, lang='ko')

    # 임시 음성 파일 저장
    tts.save("output.mp3")

    # 음성 파일 재생
    playsound.playsound("output.mp3")


def koconverten():

    # 파일 텍스트 읽기
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "input.txt")
    # print(file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    # print(text)

    # 한글을 영문으로
    translator = Translator()
    translation = translator.translate(text, src='ko', dest='en')
    print(translation.text)

    # 영문 번역 결과를 음성으로 변환
    tts = gTTS(text=translation.text, lang='en')

    # 임시 음성 파일 저장
    tts.save("output.mp3")

    # 음성 파일 재생
    playsound.playsound("output.mp3")


if __name__ == '__main__':
    # speaken("Hello")
    # speakko("안녕하세요")
    koconverten()
