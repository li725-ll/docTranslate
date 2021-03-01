import pygame,requests
import json,time,os
from PIL import Image


def music_play():
    pygame.mixer.init()
    pygame.mixer.music.load("music/OneSentenceADay/"+time.strftime("%Y-%m-%d", time.localtime())+".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    

def load_image():
    dirs = os.listdir("images/index")
    if dirs:  # 判断是否下载过
        if time.strftime("%Y-%m-%d", time.localtime()) + ".jpg" in dirs:
            pass
        else:
            for i in dirs:
                os.remove("images/index/" + i)
                
            with open("json/" + time.strftime("%Y-%m-%d", time.localtime()) + ".json", "r") as file:
                text = json.loads(file.read())
            response = requests.get(text["fenxiang_img"])
            with open("images/index/" + time.strftime("%Y-%m-%d", time.localtime()) + ".jpg", "wb") as file:  # 暂存图像文件
                file.write(response.content)
            # 修改图片大小
            img = Image.open("images/index/" + time.strftime("%Y-%m-%d", time.localtime()) + ".jpg")
            img.resize((540, 700)).save("images/index/" + time.strftime("%Y-%m-%d", time.localtime()) + ".jpg")
    else:
        with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json","r") as file:
            text = json.loads(file.read())
        response = requests.get(text["fenxiang_img"])
        with open("images/index/"+time.strftime("%Y-%m-%d", time.localtime())+".jpg", "wb") as file:  # 暂存图像文件
            file.write(response.content)
        # 修改图片大小
        img = Image.open("images/index/"+time.strftime("%Y-%m-%d", time.localtime())+".jpg")
        img.resize((540, 700)).save("images/index/"+time.strftime("%Y-%m-%d", time.localtime())+".jpg")


def load_music():
    dirs = os.listdir("music/OneSentenceADay")
    if dirs:#判断是否下载过
        if time.strftime("%Y-%m-%d", time.localtime())+".mp3" in dirs:
            pass
        else:
            for i in dirs:
                os.remove("music/OneSentenceADay/"+i)
                
            with open("json/" + time.strftime("%Y-%m-%d", time.localtime()) + ".json", "r") as file:
                text = json.loads(file.read())
            response = requests.get(text["tts"])
            with open("music/OneSentenceADay/"+time.strftime("%Y-%m-%d", time.localtime())+".mp3", "wb") as file:  # 暂存文件
                file.write(response.content)
    else:
        with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json","r") as file:
            text = json.loads(file.read())
        response = requests.get(text["tts"])
        with open("music/OneSentenceADay/"+time.strftime("%Y-%m-%d", time.localtime())+".mp3", "wb") as file:  # 暂存文件
            file.write(response.content)
 
        
#
def vab_play(shuru):
    pygame.mixer.init()
    pygame.mixer.music.load("music/vocabulary/"+shuru+".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass