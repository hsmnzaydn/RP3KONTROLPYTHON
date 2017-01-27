import pygame


globvar = 1
array=["/home/dvcc/PycharmProjects/firebase/untitled.mp3","/home/dvcc/PycharmProjects/firebase/untitled.mp3"]
def baslat(icerik):
    pygame.init()
    if icerik=="baslat":
        pygame.mixer.music.load(array[0])
    else:
        pygame.mixer.music.load(icerik)
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

def devamediyormu(result2):
    global globvar
    if result2 == "on" and pygame.mixer.music.get_busy() == False and globvar < len(array):
        print("Yeni muzik başladı")
        baslat(array[globvar])
        globvar += 1






