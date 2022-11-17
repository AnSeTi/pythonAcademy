
#! Karar Blokları - Döngüler - Data Input/Output
print("2. Gün Başlangıç")

#userInput = input()
#print(f"Girilen Değer: {userInput}")

#! type conversion (veri tipi değişimi) 
numberStr = "10"
print(type(numberStr)) 
number = int(numberStr)  #*String değeri int yaptık
print(number + 10)
print(type(number))


userInput = input() #! Kullanıcıdan input alma
lessonNote = float(userInput) #! ilgili veriyi float'a çevirme
print(f"Ders Notunuz: {lessonNote}")


#*indent
#*n adet conditiona bağlı karar bloğu
if lessonNote>50:
    print("Başarıyla Geçtiniz")
elif lessonNote == 50:
    print("Sınırda Geçtiniz")
elif lessonNote == 49:
    print("Sınırda Kaldınız")
else:
    print("Kaldınız")
