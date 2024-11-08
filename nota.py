import sys

def jumlah(x, y) :
	return x + y

def kurang(x, y) :
	return x - y
	
def kali(x, y) :
	return x * y
	
harga1 = 7000
harga2 = 9000
harga3 = 11000
harga4 = 13000
harga5 = 14000
harga6 = 16000




print("""

[•] ========== Mi Ayam Mas Fais =========== [•]

[•] 1. Mi ayam biasa : 7k
[•] 2. Mi ayam ceker :9k
[•] 3. Mi ayan bakso  biasa :  11k
[•] 4. Mi ayam bakso jumbo : 13k
[•] 5. Mi ayam bakso ceker : 14k
[•] 6. Mi ayam bakso jumbo ceker : 16k

[•] ==================================== [•]
""")


try :
            pilihan = int(input("Masukan Pilihan Nomor : "))
            angka = int(input("Masukan Jumlah : "))
            bayar = int(input("Uangnya Berapa : "))
            
except ValueError :
    print("[ ! ] Pilih Yang Bener!!")
    
    sys.exit()
    
total1 = (angka * harga1)
total2 = (angka * harga2)
total3 = (angka * harga3)
total4 = (angka * harga4)
total5 = (angka * harga5)
total6 = (angka * harga6)
    
if pilihan == 1 :
	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam biasa 
	Harga : 7k
	Harga Total :  Rp.{kali(angka, harga1)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total1)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
elif pilihan == 2 :
   	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam ceker
	Harga : 9k
	Harga Total :  Rp.{kali(angka, harga2)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total2)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
elif pilihan == 3 :
	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam bakso biasa
	Harga : 11k
	Harga Total :  Rp.{kali(angka, harga3)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total3)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
elif pilihan == 4 :
	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam bakso jumbo
	Harga : 13k
	Harga Total : Rpm {kali(angka, harga4)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total4)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
elif pilihan == 5 :
	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam bakso ceker
	Harga : 14k
	Harga Total :  Rp.{kali(angka, harga5)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total5)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
elif pilihan == 6 :
	print(f"""
	Nota
	
	[•]==>Mi Ayam Mas Fais<==[•]
	
	Nama Menu : Mi ayam bakso jumbo ceker
	Harga : 16k
	Harga Total : Rp.{kali(angka, harga6)}
	Bayar : Rp.{bayar}
	Kembalian : Rp.{kurang(bayar, total6)}
    
         Terima Kasih Sudah Membeli
    
	""")
	
else :
	print("[!] YANG BENER WOII!!")
	

