import pygame
import muzikler


def baslat():
    pygame.init()
    pygame.mixer.music.load("/home/dvcc/PycharmProjects/firebase/can.mp3")
    pygame.mixer.music.play()
    print("Muzik basladi")
def durdur():
    pygame.mixer.music.stop()
    print("durduruldu")
def pause():
    pygame.mixer.music.pause()
    print("pause edildi")
def unpause():
    pygame.mixer.music.unpause()
    print("devam ettiriliyor")