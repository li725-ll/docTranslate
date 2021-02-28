import pygame,requests
import json,time
from PIL import Image


def music_play():
    pygame.mixer.init()
    pygame.mixer.music.load("music/OneSentenceADay/today.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    

def load_image():
    with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json","r") as file:
        text = json.loads(file.read())
    print(text["fenxiang_img"])
    response = requests.get(text["fenxiang_img"])
    with open("images/index/index.jpg", "wb") as file:  # 暂存图像文件
        file.write(response.content)
    # 修改图片大小
    img = Image.open("images/index/index.jpg")
    img.resize((540, 700)).save("images/index/index.jpg")


def load_music():
    with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json","r") as file:
        text = json.loads(file.read())
    response = requests.get(text["tts"])
    with open("music/OneSentenceADay/today.mp3", "wb") as file:  # 暂存文件
        file.write(response.content)