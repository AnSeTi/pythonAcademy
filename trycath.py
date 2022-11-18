
#!Hata yakalama
#* number = 1/0
#* print(number)
#ZeroDivisionError: division by zero HATASI
#Bu hatanın altında kalan satırlar çalışmayacaktır !!

#* examNote = float(input("Lütfen Sınav notunuzu Giriniz:"))
#* print(examNote)
#ValueError: could not convert string to float: 'asd'
# asd girdisi floata dönüştürülemedi hatası

#! Pythonda tryexcep olarak geçer
#! Run-Time exception  Try-Except
    #* Girdi hatalarında vb. runtime exception olur 
#! Compile-Time exception
    #* deneme="dsa"  kod çalıştırılmaz compile ederken bulunur.
#!  run time except olanlarda program ne yaapcağını bilmez ve bizim anlatmamız gerekir.(handle etmek)
try:
    examNote = float(input("Lütfen Sınav notunuzu Giriniz:"))
    print(examNote)
except ValueError:  #ValueError olduğunu hatayı görünce anlayabiliriz.
    print("Value Error var")
except ZeroDivisionError:
    print("Sayı 0'a bölünemez")
except:
    print("Doğru Bir Girdi Girmediniz")
finally: #except blokları sona erdiğinde çalıştırılacak olan bloklaru içerebilir.
    print("hata yok-Try Except sona erdi..")
    
