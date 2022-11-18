lessonCount = 0
while lessonCount <= 0 or lessonCount >10:
    lessonCount = int(input("Ders sayısını giriniz: "))

passedLessons_rev = []
failedLessons_rev = []
passedLessonsExams = []
passedLessonsFinals = []
failedLessonsExams = []
failedLessonsFinals = []
count = 0



for i in range(lessonCount):
    lessonExam = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    if lessonExam > 100:
        print("100'den aşağı bir sayı giriniz!")
    else:
        lessonFinal = float(input(f"{i+1}. ders için final notunu giriniz: "))
        if lessonFinal > 100:
            print("100'den aşağı bir sayı giriniz!")
        else:
            lessonAverage = (lessonExam*.4) + (lessonFinal*.6)
            count += 1
            if lessonAverage >= 50:
                passedLessons_rev.append([count,lessonAverage])
                passedLessonsExams.append(lessonExam)
                passedLessonsFinals.append(lessonFinal)
                print(f"Girdiğiniz {count}.  ders sınavından , {passedLessons_rev[len(passedLessons_rev) - 1]} notu ile geçtiniz.")
            else:
                failedLessons_rev.append([count,lessonAverage])
                failedLessonsExams.append(lessonExam)
                failedLessonsFinals.append(lessonFinal)
                print(f"Girdiğiniz {count}.  ders sınavından , {failedLessons_rev[len(failedLessons_rev) - 1]} notu ile kaldınız.")

print(f"{passedLessons_rev} ortalama notları ile {len(passedLessons_rev)} dersten geçtiniz. {failedLessons_rev} ortalama notları ile {len(failedLessons_rev)} dersten kaldınız.")
print(f"Geçtiğiniz derslerin vize notları: {passedLessonsExams}, Geçtiğiniz derslerin final notları: {passedLessonsFinals}.\nKaldığınız derslerin vize notları: {failedLessonsExams}, Kaldığınız derslerin final notları: {failedLessonsFinals}.")