from firebase import firebase
import mp3cal
import time
import havadurumu

firebase=firebase.FirebaseApplication('https://python-b7487.firebaseio.com')#Firebase hesabına bağlanıyoruz her firebase projesi için farklı bir link vardır onu yapıştırın.Firebasede database kısmında link yazıyordur.


sayac_led=0
sayac_mp3=0
sayac=1
sondurum="null"
while sayac==1:
    time.sleep(1)
    try:
        mp3kontrol = firebase.get('/kontroller', 'mp3_kontrol')
        mp3durum=firebase.get('/kontroller','mp3_durum')
        havadurumu_kontrol=firebase.get('/kontroller','havadurumu_kontrol')
        print('Mp3 kontrol:', mp3kontrol, 'Mp3 durum', mp3durum,"Hava durumu",havadurumu_kontrol)
        if mp3kontrol== 'on' and sayac_mp3==0:
            mp3cal.baslat("baslat")
            sayac_mp3 = 1
        if mp3kontrol== 'off' and sayac_mp3==1:
            mp3cal.durdur()
            sayac_mp3=0
        if mp3durum == 'pause' and mp3kontrol== 'on':
            mp3cal.pause()
            sondurum="pause"
        if sayac_mp3==1 and mp3durum=='stop':
            mp3cal.durdur()
            sayac_mp3=0
        if mp3durum=="unpause" and sondurum=="pause":
            mp3cal.unpause()
            sondurum="null"
        mp3cal.devamediyormu(mp3kontrol)
        if havadurumu_kontrol=="on":
            havadurumu.havadurumu()




    except ValueError:
        print("Hata")


