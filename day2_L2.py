
# #! Karar Blokları - Döngüler - Data Input/Output
# print("2. Gün Başlangıç")

# #userInput = input()
# #print(f"Girilen Değer: {userInput}")

# #! type conversion (veri tipi değişimi) 
# numberStr = "10"
# print(type(numberStr)) 
# number = int(numberStr)  #*String değeri int yaptık
# print(number + 10)
# print(type(number))


# userInput = input() #! Kullanıcıdan input alma
# lessonNote = float(userInput) #! ilgili veriyi float'a çevirme
# print(f"Ders Notunuz: {lessonNote}")


# #*indent
# #*n adet conditiona bağlı karar bloğu
# if lessonNote>50:
#     print("Başarıyla Geçtiniz")
# elif lessonNote == 50:
#     print("Sınırda Geçtiniz")
# elif lessonNote == 49:
#     print("Sınırda Kaldınız")
# else:
#     print("Kaldınız")

#! Kullanıcıdan vize ve final notları alınacak.
#! vize %40  final %60 etkili olacak
#! vize ve final notları ondalıklı sayılar olabilir
#! Uygulama ortalamayı hesaplayacak ve ortalamaya göre 
#! 0-49 FF,  50-60 DD, 60-70 CC, 70-80 BB, 80-100 AA
#* NOT ORTALAMASINI VE HARF NOTUNU KULLANICIYA GÖSTERECEK PROGRAMI KODLAYINIZ


vize = float(input("Vize Notunu Giriniz:"))
if vize > 100:
    print("100'den küçük bir değer giriniz !")
else:
    final = float(input("Final Notunuzu giriniz:"))
    if final > 100:
        print("100'den düşük bir değer giriniz !")
    else:
        average = (vize*0.4+final*0.6)
    print(f"Ders Ortalamanız: {average}")

    if average < 50 and average >=0:
        print("FF Aldınız !")
    elif average < 60 and average >=50:
        print("DD Aldınız!")
    elif average < 70 and average >=50:
        print("CC Aldınız!")
    elif average < 80 and average >=70:
        print("BB Aldınız!")
    else:
        print("AA Aldınız!")

#! Yeni Geliştirmeler !!!
#! Döngüleri araştıracağız
#! kullanıcı bir sayı girecek,örn: 10
#! kullanıcı 10 kere 1. ders için vize ve final
#! kullanıcının girdiği sayı kadar ders için vize final hesaplatıp
#! girdiğiniz N adet dersten x tanesini geçtiniz y tanesini kaldınız
#! 50> geçti   50< kaldı gibi bir yapı olabilir.
#! range veya while kullanabiliriz.