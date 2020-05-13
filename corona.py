import requests
from bs4 import BeautifulSoup
import smtplib
from tkinter import *
pencere = Tk ()
pencere.title("KORONAVİRÜS")
pencere.geometry("800x450")
arkaplan = PhotoImage(file= r"Başlıksız-3 (2).png")
Label(pencere,image=arkaplan).place(relwidth=1,relheight=1)


def veri_al():
    maill = mail.get()
    sifre = sifreAl.get()
    yolla = YollanacakMail.get()
    botubaslat(maill,sifre,yolla)



etiket1 = Label(text = "Mail Adresinizi Giriniz")
etiket1.pack()
mail = Entry()
mail.pack()

etiket2 = Label(text = "Mail Şifrenizi Giriniz")
etiket2.pack()
sifreAl = Entry(show="*")
sifreAl.pack()

etiket3 = Label(text = "Verileri Nereye Yollayalım ?")
etiket3.pack()
YollanacakMail = Entry()
YollanacakMail.pack()

buton = Button(text="Bot'u Başlat",command=veri_al)
buton.pack()

#etiket4 = Label(text = "Mail Göndermek İstemiyorsanız Direk Bot'u Başlat Butonuna Basabilirsiniz.",font=("Open Sans","8","normal"))
#etiket4.pack()



eski=0
def botubaslat(maill,sifre,yolla):

    def corona():
            global eski
            link = "https://covid19.saglik.gov.tr/"
            r=requests.get(link)
            soup = BeautifulSoup(r.content,"lxml")
            Baslik = soup.find("div",attrs={"class":"baslik-tablo"}).text.strip()
            Tarih = soup.find("div",attrs={"class":"takvim text-center"}).select("p:nth-of-type(1)")[0].text + " " + soup.find("div",attrs={"class":"takvim text-center"}).select("p:nth-of-type(2)")[0].text + " " +soup.find("div",attrs={"class":"takvim text-center"}).select("p:nth-of-type(3)")[0].text
            Test = float(soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(1)> span:nth-of-type(2)")[0].text.strip().replace(".",""))
            Vaka = soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(2)> span:nth-of-type(2)")[0].text
            Vefat = soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(3)> span:nth-of-type(2)")[0].text
            Yogun = soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(4)> span:nth-of-type(2)")[0].text
            Entube = soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(5)> span:nth-of-type(2)")[0].text
            iyilesme = soup.find("ul",attrs={"list-group list-group-genislik"}).select("li:nth-of-type(6)> span:nth-of-type(2)")[0].text
            G_Test = soup.find("div",attrs={"mtop-bosluk buyuk-bilgi-l"}).select("ul:nth-of-type(1)>li:nth-of-type(1)>span:nth-of-type(2)")[0].text.strip()
            G_Vaka = soup.find("div",attrs={"mtop-bosluk buyuk-bilgi-l"}).select("ul:nth-of-type(1)>li:nth-of-type(2)>span:nth-of-type(2)")[0].text.strip()
            G_Vefat = soup.find("div",attrs={"mtop-bosluk buyuk-bilgi-l"}).select("ul:nth-of-type(1)>li:nth-of-type(3)>span:nth-of-type(2)")[0].text.strip()
            G_iyilesme = soup.find("div",attrs={"mtop-bosluk buyuk-bilgi-l"}).select("ul:nth-of-type(1)>li:nth-of-type(4)>span:nth-of-type(2)")[0].text.strip()


            #print("\*/"*12)
            #print("\n{}\n\nTARİH : {}\nTOPLAM TEST SAYISI :  {}\nTOPLAM VAKA SAYISI : {}\nTOPLAM VEFAT SAYISI : {}\nYOĞUN BAKIM SAYISI : {}\nENTÜBE HASTA SAYISI : {}\nTOPLAM İYİLEŞME SAYISI : {}\n".format(Baslik,Tarih,Test,Vaka,Vefat,Yogun,Entube,iyilesme))
            #print("\*/"*12)
            #print("Sonuçları Göndermek İçin Mail Adresinizi ve Şifrenizi Giriniz :")

            l.configure(text=str("{} \nTarih {}\nTOPLAM TEST SAYISI :  {}\nTOPLAM VAKA SAYISI : {}\nTOPLAM VEFAT SAYISI : {}\nYOĞUN BAKIM SAYISI : {}\nENTÜBE HASTA SAYISI : {}\nTOPLAM İYİLEŞME SAYISI : {}\nBUGÜNKÜ TEST SAYISI : {}\nBUGÜNKÜ VAKA SAYISI : {}\nBUGÜNKÜ VEFAT SAYISI : {}\nBUGÜNKÜ İYİLEŞME SAYISI : {}\nGönderilecek Mail : {}".format(Baslik,Tarih,Test,Vaka,Vefat,Yogun,Entube,iyilesme,G_Test,G_Vaka,G_Vefat,G_iyilesme,yolla)))
            pencere.after(1,corona)
            if eski < Test:
                if len(maill)<3 or len(sifre)<3 or len(yolla)<3:
                                l.configure(text=str("{} \nTarih {}\nTOPLAM TEST SAYISI :  {}\nTOPLAM VAKA SAYISI : {}\nTOPLAM VEFAT SAYISI : {}\nYOĞUN BAKIM SAYISI : {}\nENTÜBE HASTA SAYISI : {}\nTOPLAM İYİLEŞME SAYISI : {}\nBUGÜNKÜ TEST SAYISI : {}\nBUGÜNKÜ VAKA SAYISI : {}\nBUGÜNKÜ VEFAT SAYISI : {}\nBUGÜNKÜ İYİLEŞME SAYISI : {}\nGönderilecek Mail : {}".format(Baslik,Tarih,Test,Vaka,Vefat,Yogun,Entube,iyilesme,G_Test,G_Vaka,G_Vefat,G_iyilesme,yolla)))


                else:
                    mesaj="\n{}\n\nTARİH : {}\nTOPLAM TEST SAYISI :  {}\nTOPLAM VAKA SAYISI : {}\nTOPLAM VEFAT SAYISI : {}\nYOĞUN BAKIM SAYISI : {}\nENTÜBE HASTA SAYISI : {}\nTOPLAM İYİLEŞME SAYISI : {}\nBUGÜNKÜ TEST SAYISI : {}\nBUGÜNKÜ VAKA SAYISI : {}\nBUGÜNKÜ VEFAT SAYISI : {}\nBUGÜNKÜ İYİLEŞME SAYISI : {}\n\nBu mail eğitim amaçlı gönderilmiştir.".format(Baslik,Tarih,Test,Vaka,Vefat,Yogun,Entube,iyilesme,G_Test,G_Vaka,G_Vefat,G_iyilesme).encode('utf-8')
                    mail = smtplib.SMTP("smtp.gmail.com",587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login(maill,sifre)
                    mail.sendmail("DENEME",yolla,mesaj)
                    eski = Test


    l=Label(text=0,font="Verdana 16 bold",bg="#282c34")
    l.place(x=124,y=0)

    corona()

pencere.mainloop()
