class Dusman:
    def __init__(self,isim="Dusman",kalan_can="1500",saldiri_gucu="50",mermi_sayisi="45"):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldiri_gucu=saldiri_gucu
        self.mermi_sayisi=mermi_sayisi

    def print(self):
        print("Basliyor")
        print("Isım:",self.isim,"Kalan Can:",self.kalan_can,"Saldiri Gucu:",self.isim,"Mermi Sayisi",self.mermi_sayisi)

dusman1 = Dusman("Ali",1000,30,40)
dusman2 = Dusman("Mehmet",2000,20,50)
dusman3=Dusman()
print("Dusman1")

dusman1.print()

print("dusman2")
dusman2.print()
