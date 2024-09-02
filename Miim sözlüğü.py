memekosesi = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "idk": "Bir şeyin doğru olduğu yada aynen öyle denilmesi(Öyle biliyorum)"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in memekosesi.keys():
 print(memekosesi[word])
else:
 print("Bu kelime daha gelmedi.")
