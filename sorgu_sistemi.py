import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

# Veritabanı bağlantı bilgileri
db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'ilterdatabase'
}




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

#Kullanici Dolaplari
dolaplar = {"ahmet":[] , "bahar":[] , "ilter":[] , "alper":[] , "burak":[]}




# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Giris Sorgu Sistemi")
root.geometry("300x200")

# Etiketler ve giriş alanları
tk.Label(root, text="Kullanici Adi:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="sifre:").grid(row=1, column=0, padx=10, pady=10)

kullanici_adi_entry = tk.Entry(root)
kullanici_adi_entry.grid(row=0, column=1, padx=10, pady=10)

sifre_entry = tk.Entry(root, show="*")
sifre_entry.grid(row=1, column=1, padx=10, pady=10)

current_user = None
kitaplar_penceresi = None 

def yeni_pencere():
    global kitaplar_penceresi

    if kitaplar_penceresi is None:
        kitaplar_penceresi = tk.Toplevel(root)
        kitaplar_penceresi.title("Hosgeldiniz")
        kitaplar_penceresi.geometry("400x400")

    kitap_listesi(1)

def kitap_listesi(sayfa):
    if kitaplar_penceresi is None:
        return

    for widget in kitaplar_penceresi.winfo_children():
        widget.destroy()
    
    if sayfa == 1:
        kitaplar = bookList[:5]
    else:
        kitaplar = bookList[5:]
    
    for kitap in kitaplar:
        tk.Label(kitaplar_penceresi, text=f"{kitap['Book No']} - {kitap['writer']} - {kitap['Book Name']}").pack()

    tk.Button(kitaplar_penceresi, text="1. Sayfa", command=lambda: kitap_listesi(1)).pack()
    tk.Button(kitaplar_penceresi, text="2. Sayfa", command=lambda: kitap_listesi(2)).pack()
    tk.Button(kitaplar_penceresi, text="Kitap Al", command=kitap_al).pack()
    tk.Button(kitaplar_penceresi, text="Kitap Teslim", command=kitap_teslim).pack()
    tk.Button(kitaplar_penceresi, text="Aldiginiz Kitaplar", command=alinan_kitaplar_penceresi).pack()

def kitap_al():
    kitap_no = simpledialog.askstring("Kitap Al", "Almak istediginiz kitap numarasini girin:")
    
    kitap_var_mi = any(kitap_no in [kitap["Book No"] for kitap in kitaplar] for kitaplar in dolaplar.values())
    if kitap_var_mi:
        messagebox.showinfo("Hata", "Kitap daha önce kiralanmis.")
        return
    
    for kitap in bookList[:]:
        if kitap["Book No"] == kitap_no:
            bookList.remove(kitap)
            dolaplar[current_user].append(kitap)
            messagebox.showinfo("Basarili", "Kitap basariyla alindi.")
            break
    else:
        messagebox.showinfo("Hata", "Gecersiz kitap numarasi.")
    
    # Aldiktan sonra pencereyi güncelle
    alinan_kitaplar_penceresi()

def kitap_teslim():
    kitap_no = simpledialog.askstring("Kitap Teslim", "Teslim etmek istediginiz kitap numarasini girin:")
    for kitap in dolaplar[current_user]:
        if kitap["Book No"] == kitap_no:
            dolaplar[current_user].remove(kitap)
            bookList.append(kitap)
            messagebox.showinfo("Basarili", "Kitap basariyla teslim edildi.")
            break
    else:
        messagebox.showinfo("Hata", "Gecersiz kitap numarasi.")
    
    # Teslim ettikten sonra pencereyi güncelle
    alinan_kitaplar_penceresi()

def alinan_kitaplar_penceresi():
    if kitaplar_penceresi is None:
        return
    
    for widget in kitaplar_penceresi.winfo_children():
        if isinstance(widget, tk.Toplevel) and widget.title() == "Aldiginiz Kitaplar":
            widget.destroy()
            break
    
    alinan_kitaplar_penceresi = tk.Toplevel(kitaplar_penceresi)
    alinan_kitaplar_penceresi.title("Aldiginiz Kitaplar")
    alinan_kitaplar_penceresi.geometry("400x400")
    
    for kitap in dolaplar[current_user]:
        tk.Label(alinan_kitaplar_penceresi, text=f"{kitap['Book No']} - {kitap['writer']} - {kitap['Book Name']}").pack()

def sorgula():
    global current_user
    kullanici_adi = kullanici_adi_entry.get().lower().strip()
    sifre = sifre_entry.get().strip()
    
    try:
        # Veritabanına bağlan
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Kullanıcıyı sorgula
        query = "SELECT * FROM kullanici_bilgileri WHERE kullanici_adi = %s AND sifre = %s"
        cursor.execute(query, (kullanici_adi, sifre))
        
        sonuc = cursor.fetchone()
        
        if sonuc:
            current_user = kullanici_adi
            messagebox.showinfo("Sonuc", "Giris basarili!")
            yeni_pencere()
        else:
            messagebox.showinfo("Sonuc", "Kullanici adi veya sifre yanlis.")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showinfo("Hata", f"Veritabanı hatası: {err}")

# Sorgula butonu
sorgula_buton = tk.Button(root, text="Sorgula", command=sorgula)
sorgula_buton.grid(row=2, column=1, padx=10, pady=10)

# Ana döngüyü baslatma
root.mainloop()
