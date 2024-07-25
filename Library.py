
#Kitap Listesi
bookList = [
        {"Book No": "1", "writer": "Don Kisot", "Book Name": "Miguel de Cervantes"},
        {"Book No": "2","writer": "William Shakespare","Book Name": "Romeo ve Juliet",},
        {"Book No": "3", "writer": "Victor Hugo", "Book Name": "Sefiller"},
        {"Book No": "4", "writer": "Fyodol Dostovsky", "Book Name": "Suc ve Ceza"},
        {"Book No": "5", "writer": "Dante Alighieri", "Book Name": "The Divine Comedy"},
        {"Book No": "6", "writer": "Charlotte Bronte", "Book Name": "Jane Eyre"},
        {"Book No": "7", "writer": "Gustava Flaubert", "Book Name": "Madama Bovary"},
        {"Book No": "8", "writer": "Stendhal", "Book Name": "Kirmizi ve Siyah"},
        {"Book No": "9", "writer": "Charles Dickens","Book Name": "Great Expectations",},
        {"Book No": "10", "writer": "Lev Tolstoy", "Book Name": "Anna Karenina"},
    ]

#Kullanici Listesi
UserList = [
        {"Kullanici Id:" : "1" , "Kullanici Ismi:" :"ahmet" , "Kullanici Sifresi:" : "1234"},
        {"Kullanici Id:" : "2" , "Kullanici Ismi:" :"Bahar" , "Kullanici Sifresi:" : "1235"},             
        {"Kullanici Id:" : "3" , "Kullanici Ismi:" :"ilter" , "Kullanici Sifresi:" : "1236"},             
        {"Kullanici Id:" : "4" , "Kullanici Ismi:" :"alper" , "Kullanici Sifresi:" : "1237"},             
        {"Kullanici Id:" : "5" , "Kullanici Ismi:" :"burak" , "Kullanici Sifresi:" : "1238"},             
    ]

#Kullanici Dolaplari
dolaplar = {"ahmet":[] , "bahar":[] , "ilter":[] , "alper":[] , "burak":[]}

#Sistemin Dongu Baslangici
while True:
    system = input("Sisteme Giris: 1 \nSistemden Cikis: 2\n")
    if system == "1":
        print("Sisteme Girildi\n")
        
        while True:  
            
            #Kullanici Bilgileri Alma-Kontrol
            kullaniciSorguAd = input("Kullanici Adinizi Giriniz: ").lower().strip()
            kullaniciSorguSifre = input("Kullanici Sifrenizi Giriniz: ").strip()
            
            #Kontrol Kısmı
            for kullanici in UserList:
                if kullanici["Kullanici Ismi:"].lower() == kullaniciSorguAd and kullanici["Kullanici Sifresi:"] == kullaniciSorguSifre:
                    print("\nBasarili Giris")
                    break
            else:
                print("\nGirdiginiz kullanici adi bulunamadi\n")
                continue
            break
        
        firstBookPage = bookList[:5]
        secondBookPage = bookList[5:]
        

        #Kitap Katalog Gecisleri
        print("Kitap Katalog Sayfalari:\nBirinci Sayfa Icin 1'e\nIkinci Sayfa Icin 2'ye\n")
        while True:
            katalog = input("Cikmak Icin 3'e basin\nBulundugunuz Sayfa: ")
            print()
            if katalog == "1":
                for i in firstBookPage:
                    print(i)
            
            elif katalog == "2":
                for i in secondBookPage:
                    print(i)
        
            elif katalog == "3":
                break
            
            else:
                print("Yanlis Sayi Girdiniz\n")
                continue
        
        #Kullanicinin Kitap Alması-Dolabına Aktarılması
        kitapSecim = input("Almak Istediginiz Kitap Numarasini Giriniz: ")
        
        #kullanıcının girdiği kitap başkasında var mı yok mu onu kontrol et 
        #gokhan abiye tam aciklat
        kitapVarmi = any(kitapSecim in [kitap["Book No"] for kitap in kitaplar] for kitaplar in dolaplar.values())
        if kitapVarmi:
            print("Kitap Daha Once Kiralanmis")
            
        else:
            for eklenenKitap in bookList[:]:
                if eklenenKitap["Book No"] == kitapSecim:
                    #Kullanicinin aldigi kitabi listeden silme 
                    bookList.remove(eklenenKitap)
       
                    #Kullanicinin aldigi kitabi kendi dolabina ekleme
                    while True:
                        dolapIsmi = input("Dolap Isminizi Giriniz: ").strip().lower()
                        if dolapIsmi == kullaniciSorguAd:
                            if dolapIsmi in dolaplar:
                                dolaplar[dolapIsmi].append(eklenenKitap)
                                break       
                        else:
                            print("Yanlis Dolap Ismi")
                            continue
       
             
            #Kullanicinin Dolap Icerigi 
            for dolap,kitaplar in dolaplar.items():
               if dolapIsmi == dolap:
                   print(f"{dolap}: {kitaplar}")
        
        #Kitap teslim etme
        kitapTeslim = input("Kitap Teslim Etmek Ister misiniz? (Evet/Hayir)").lower().strip()
        if kitapTeslim == "evet":
            teslimEdilenKitap = input("Teslim Etmek Istediginiz Kitabi Giriniz: ")
            for kullanici , kitaplar in dolaplar.items():
                for kitap in kitaplar:
                    if kitap["Book No"] == teslimEdilenKitap:
                        kitaplar.remove(kitap)
                        bookList.append(kitap)
                        print("Kitap Teslim Edildi")
                
        elif kitapTeslim == "hayir":
            for i , j in dolaplar.items():
                print(i , j)

        

    elif system == "2":
        for i in bookList:
            print(i)
        break
    


    # Ayni kitabi baska biri almaya calistigi zaman uyarı ver.
    # Kitabi alan kisiye zaman bilgileri verilsin ne zaman aldigi ne zaman geri verecegi maksimum 20 gun alabilsin kitabi. 
    # Kullanici max 3 kitap alabilsin. 
    # Kullanici girdigi zaman eger zamani gecmis kitap varsa soylesin ne zaman geri vermesi gerekirdi ne kadar gec kaldı gibi ve uyarı alsın.
    # Kullanicinin elindeki kitaplarin zaman kavramı bilgileri olsun mesela kac gün kaldi son gunune gibi.