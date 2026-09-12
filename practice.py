"""
Shunday class tuzing tuzing nomi Shop, va uni constructoriga 3 hil mahsulot pass bolsin,
hamda classning 3ta methodi bolsin, biri qoldiq, biri sotish va biri qabul. 
Har bir method ishga tushgan vaqt ham log qilinsin.
MASALAN: const shop = new Shop(4, 5, 2); 
shop.qoldiq() return hozir 20:40da 4ta non, 5ta lagmon va 2ta cola mavjud! shop.sotish('non', 3) & shop.qabul('cola', 4) & shop.qoldiq() 
return hozir 20:50da 1ta non, 5ta lagmon va 6ta cola mavjud!
"""


class Shop():

    def __init__(self, non, cola, muzqaymoq):
        self.non = non
        self.cola = cola
        self.muzqaymoq = muzqaymoq

    def qoldiq(self):
        print(f"{self.non}ta non, {self.cola}ta cola, {self.muzqaymoq}ta muzqaymoq")

    def sotish(self, name, amount):
        if (name == 'non'):
            if (self.non > amount):
                self.non -= amount
                print(f"{name} {self.non}ta qoldi")
            else:
                print(f"{name} not enough")
        elif (name == 'cola'):
            if (self.cola > amount):
                self.cola -= amount
                print(f"{name} {self.cola}ta qoldi")
            else:
                print(f"{name} not enough")
        elif (name == 'muzqaymoq'):
            if (self.muzqaymoq > amount):
                self.muzqaymoq -= amount
                print(f"{name} {self.muzqaymoq}ta qoldi")
            else:
                print(f"{name} not enough")
        else:
            print(f"{name} not found")

    def qabul(self, name, amount):
        if (name == 'non'):
            self.non += amount
            print(f"{name} {amount}ta qushildi")
            print(f"{name} {self.non}ta mavjud")
        elif (name == 'cola'):
            self.cola += amount
            print(f"{name} {amount}ta qushildi")
            print(f"{name} {self.cola}ta mavjud")
        elif (name == 'muzqaymoq'):
            self.muzqaymoq += amount
            print(f"{name} {amount}ta qushildi")
            print(f"{name} {self.muzqaymoq}ta mavjud")
        else:
            print(f"{name} not found")


products = Shop(3, 6, 7)
products.qoldiq()
# products.sotish('muzqaymoq', 2)
products.qabul('cola', 2)
# products.qabul('cola', 3)
# products.qoldiq()