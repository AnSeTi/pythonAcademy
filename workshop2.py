
file = open("sample.txt","r")
# harfler mod gösterir. "a" "w" "r" vs. modlardan sadece birini kullanabiliriz.
#"r" read okuma modu belirtir
#"a" append, üzerine yazma işlemidir/ekleme
#"w" write yazma işlemini temsil eder. (sıfırdan yazma)
#ilgili open fonksiyonuna "w" parametresini belirtirsek yazma yapacağımızı gösteririz.
#file.writelines("\n deneme 123")
print(file.read())
file.close()

file.open("employees")

#! PAİR KONUSU
#! bir şirket çalışanları verilernizi tutan dosya oluşturulacak
#! emplotees.txt
#! kullanıcıdan çalışan sayısı alınacak
#! çalışan sayısı kadar isim, soyisim, maaş bilgisi alıonacak
#! dosyada ki her satıra "ad soyad - maaş" kalıbında çalışan bilgileri eklenecek.
#! programın sonunda dosyadan bilgileri satr satır okuyup listeyecek kod yazılacak.
#!eklenen çalışanlar mevcut çalışan bilgilerini silmeyecek !!
#! belirli noktalarda hata yakalama işlemlerini unutmayalım
#! maaş için=asd ,  çalışan sayısı: girdiler doğru olmaya bilir.