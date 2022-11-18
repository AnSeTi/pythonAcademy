
#* Yeni Geliştirmeler !!!
#* Döngüleri araştıracağız
#* kullanıcı bir sayı girecek,örn: 10
#* kullanıcı 10 kere 1. ders için vize ve final
#* kullanıcının girdiği sayı kadar ders için vize final hesaplatıp
#* girdiğiniz N adet dersten x tanesini geçtiniz y tanesini kaldınız
#* 50> geçti   50< kaldı gibi bir yapı olabilir.
#* range veya while kullanabiliriz.


#! 1. kullanıcı gireceği ders sayısını belirtecek
lessonCount = int(input("Kaç adet ders notu gireceksiniz? ="))

#! Girilen ders sayısı kadar 2 adet soru sorulacak
#! 1. ders için vize, 1. ders için final giriniz
#! girilen notlar float olabilir
passedExams=0
failedExams=0
for i in range(lessonCount):
    lessonExam1.append = float(input(f"{i+1}. ders için vize notunu giriniz ="))
    lessonExam2 = float(input(f"{i+1}. ders için final notunu giriniz ="))
    totalExamNote = (lessonExam1*0.4)+(lessonExam2*0.6)
    if totalExamNote > 50:
        passedExams += 1
    else:
        failedExams += 1
print(f"{passedExams} adet dersten geçtiniz. {failedExams} adet dersten kaldınız.")






#* girilen her dersi sıralayıp(notları), 
#* geçtğiniz dersler bunlar, kaldığınız dersler bunlardır.
#* ders i için  final:zz vize:xx  gibi

