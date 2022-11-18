
#! Dosyadan veri okuma
#farklı dizinde olsaydı dosya yolunu belirtmeliyiz
#aynı dizinde direkt dosya ismi yeterli
#*file = open("sample.txt","r")
# harfler mod gösterir. "a" "w" "r" vs. modlardan sadece birini kullanabiliriz.
#"r" read okuma modu belirtir
#"a" append, üzerine yazma işlemidir/ekleme
#"w" write yazma işlemini temsil eder. (sıfırdan yazma)
#ilgili open fonksiyonuna "w" parametresini belirtirsek yazma yapacağımızı gösteririz.
# *file.writelines("\n deneme 123")
#* print(file.read())
#* file.close()

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
employeesCount=0
while True:
    try:
        while employeesCount <=0:
            employeesCount = int(input("Çalışan Sayısı Giriniz: "))
    except ValueError:
        print("Hatalı alışan Sayısı Girişi Yaptınız")
    else:
        break
file = open("employees.txt","a+")
for i in range(employeesCount):
    employeeName = str(input(f"{i+1}. Çalışan İsmini Giriniz: "))
    employeeSname = str(input(f"{i+1}. Çalışan Soyadını Giriniz: "))
    while True:
        try:
            employeeSalary = float(input(f"{i+1}. Çalışan Maaş giriniz: "))
        except ValueError:
            print("Hatalı Giriş Yaptınız")
        else:
            break
    file.writelines(f"{employeeName} {employeeSname} - {employeeSalary}\n")
file.seek(0) #seek cursoru liste sonundan başlatıyor.
print(file.read())