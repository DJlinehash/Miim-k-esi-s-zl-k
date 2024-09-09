import random

Karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

Parola_uzunlugu = int(input("Parolanız Kaç haneli olsun?"))

Parola = ""

for i in range(Parola_uzunlugu):
    Parola += random.choice(Karakterler)

    print(Parola)