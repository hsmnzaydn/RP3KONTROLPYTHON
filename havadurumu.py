from bs4 import BeautifulSoup
import requests
from gtts import gTTS
import mp3cal
import time

def havadurumu():
   source = requests.get('http://www.sabah.com.tr/hava-durumu/istanbul')
   soup = BeautifulSoup(source.text, 'html.parser')
   sicaklik= soup.findAll('div', attrs={'class': 'durum flaticon-HKY'})


   for i in sicaklik:
    break




   sicaklik=i.text
   durum2=sicaklik.replace('o', "")
   durum3=durum2.replace('/','')
   sicaklik=durum3.split()



   tts = gTTS(text="İstanbul bugün"+str(sicaklik[1])+"derece"+"Hissedilen sıcaklık ise"+str(sicaklik[2])+"derece", lang='tr')
   tts.save("havadurumu.mp3")
   mp3cal.baslat("havadurumu.mp3")
   time.sleep(1)
   
