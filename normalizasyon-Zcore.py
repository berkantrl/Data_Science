import random


class normalizasyon:
    def data_generate(): #İşlem için gerekli veriler oluşturuluyor.
        numbers = list()
        for i in range(10):
            numbers.append(random.randint(0,50)) # 0 ile 50 arasındaki sayılardan oluşturmak istedim isteğe göre değiştirilebilir.
        return numbers
    
    def find_greater(numbers): # Numbers dizinindeki en büyük ve en küçük sayı dizinini bulmamızı sağlayan fonksiyon
        smaller = 50
        greater = 0
        for i in numbers :
            if i < smaller: 
                smaller = i
            if i > greater:
                greater = i
        return smaller,greater

    def calculator_nrm(numbers,smaller,greater): # Normalizasyon formülüne göre işlemleri gerçekleştirip normalizasyonları bularak dizi halinde geri döndürüyor. 
        normalizasyon = list()
        for i in range (len(numbers)):
            nrm = (numbers[i]-smaller)/(greater-smaller)
            normalizasyon.append(nrm) # Her sonucu diziye ekleme işlemi gerçekleştiriliyor.
        
        return normalizasyon


class Z_score:

    def find_average(numbers): # Sayıların ortalamasını bularak geri döndürüyor. 
        total = 0
        for i in numbers:
            total = total + i
        average = total/len(numbers)
        return average 
    
    def find_standard(numbers,average): # Standart sapmayı formül işlemlerini gerçekleştirerek buluyor.
        total = 0
        for i in numbers:
            difference = i - average
            difference = difference**2
            total = total + difference
        part = (total/(len(numbers)-1))
        standard = part ** 0.5
        return standard

    def calculator_Z (numbers,standart,average): # Z score yine formüle göre yapılarak bulunup dizi şeklinde döndürülüyor. 
        z_scr = list()
        for x in numbers:
            score = (x - average) / standart
            z_scr.append(score)
        return z_scr

if __name__ == "__main__": # Main fonksiyonu içinde sınıfları ve fonksiyonları çağırma işlemi

    numbers = normalizasyon.data_generate()
    smaller, greater = normalizasyon.find_greater(numbers)
    normalzsyn = normalizasyon.calculator_nrm(numbers,smaller,greater)

    average = Z_score.find_average(numbers)
    standard = Z_score.find_standard(numbers,average)
    z_scr = Z_score.calculator_Z(numbers,standard,average)

    print ("Numbers","       Normalizayon","            Z Score")
    for i in range (len(numbers)):
        print(numbers[i],"      ",normalzsyn[i],"       ",z_scr[i])
        

    


    