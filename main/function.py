import pygame,requests

pygame.mixer.init()
response = requests.get("https://staticedu-wps.cache.iciba.com/audio/fe7f398766ee10e40bbe65c1b44cf757.mp3")
with open("music/1.mp3", "wb") as file:
    file.write(response.content)
pygame.mixer.music.load("music/1.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass