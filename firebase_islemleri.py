from firebase import firebase
import mp3cal#mp3cal dosyasının metodlarını kullanmak için çalıştırıyoruz
import time

firebase=firebase.FirebaseApplication('https://python-b7487.firebaseio.com')#Firebase hesabına bağlanıyoruz her firebase projesi için farklı bir link vardır onu yapıştırın.Firebasede database kısmında link yazıyordur.




sayac_led=0
sayac_mp3=0
sayac=1
sondurum="null"

while sayac==1:#Sürekli databaseden veri çekmek için kullanıyoruz
    time.sleep(1)
   # result = firebase.get('/kontroller', 'isik_kontrol')#Burada kontroller sekmesinin altındaki isik_kontrol verisini çekiyoruz her seferinde
    try:
        result2 = firebase.get('/kontroller', 'mp3_kontrol')
        mp3durum=firebase.get('/kontroller','mp3_durum')#Burada kontroller sekmesinin altındaki mp3_kontrol verisini çekiyoruz her seferinde
        print('Mp3 kontrol:',result2,'Mp3 durum',mp3durum)#Ve güncel durumun çıktısını alıyoruz
        if result2=='on' and sayac_mp3==0:
            mp3cal.baslat("baslat")
            sayac_mp3 = 1
        if result2=='off' and sayac_mp3==1:
            mp3cal.durdur()
            sayac_mp3=0
        if mp3durum == 'pause' and result2=='on':
            mp3cal.pause()
            sondurum="pause"
        if sayac_mp3==1 and mp3durum=='stop':
            mp3cal.durdur()
            sayac_mp3=0
        if mp3durum=="unpause" and sondurum=="pause":
            mp3cal.unpause()
            sondurum="null"
        mp3cal.devamediyormu()


    except ValueError:
        print("Hata")


