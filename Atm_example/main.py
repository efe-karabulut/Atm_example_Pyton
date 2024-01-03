print(
    """
    **********************
    Atm Programı
    a-) Bakiye sorgula(1)
    b-) Para yatır(2)
    c-) Para çek(3)
    **********************
      """
)
bakiye = 1500
while True:
    islem = input("Yapmak istediğiniz işlemi giriniz. Çıkmak için 'q'ya basınız:")
    if islem == "q":
        print("Yine bekleriz.")
        break
    elif islem == "1":
        print("Bakiyeniz:", bakiye)
    elif islem == "2":
        try:
            yeniMiktar = int(input("Lütfen Yatırılacak tutarı giriniz:"))
            bakiye += yeniMiktar
            print("Para yatıma işlemi başarılı.")
        except:
            print("Lütfen geçerli bir sayı giriniz!")
    elif islem == "3":
        try:
            cekilenMiktar = int(input("Lütfen çekmek istediğiniz tutarı giriniz:"))
            if cekilenMiktar > bakiye:
                print("Yetersiz bakiye.")
            else:
                print("Para çekme işlemi başarılı.")
                bakiye -= cekilenMiktar
        except:
            print("lütfen geçerli bir sayı giriniz!")
    else:
        print("Böyle bir işlem bulunamadı lütfen geçerli bir işlem sayısı giriniz!")
