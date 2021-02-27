import pygame,requests
import json


def music_play():
    with open("json/1.json","r") as file:
        text = json.loads(file.read())
    print(text["tts"])
    response = requests.get(text["tts"])
    with open("music/OneSentenceADay/1.mp3", "wb") as file:  # 暂存文件
        file.write(response.content)
    pygame.mixer.init()
    pygame.mixer.music.load("music/OneSentenceADay/1.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass