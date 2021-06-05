# PROGRAM fungsiatm
# Kumpulan fungsi dan prosedur yang akan dipanggil pada program main

# KAMUS
# df : pandas dataframe

# ALGORITMA

# import library pandas dan time
import pandas as pd
import time

def menu():
    # Mencetak menu ke layar dan menerima input pilihan dari pengguna
    
    # KAMUS LOKAL
    # menu : int
    
    # ALGORITMA
    print('''
-----------------------------
  /$$$$$$  /$$$$$$$$ /$$      /$$       /$$$$$$$                               /$$                              
 /$$__  $$|__  $$__/| $$$    /$$$      | $$__  $$                             | $$                              
| $$  \ $$   | $$   | $$$$  /$$$$      | $$  \ $$ /$$$$$$  /$$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$/$$$$ 
| $$$$$$$$   | $$   | $$ $$/$$ $$      | $$$$$$$//$$__  $$| $$__  $$ /$$__  $$| $$  /$$/ /$$__  $$| $$_  $$_  $$
| $$__  $$   | $$   | $$  $$$| $$      | $$____/| $$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$/ | $$  \ $$| $$ \ $$ \ $$
| $$  | $$   | $$   | $$\  $ | $$      | $$     | $$_____/| $$  | $$| $$  | $$| $$_  $$ | $$  | $$| $$ | $$ | $$
| $$  | $$   | $$   | $$ \/  | $$      | $$     |  $$$$$$$| $$  | $$|  $$$$$$$| $$ \  $$|  $$$$$$/| $$ | $$ | $$
|__/  |__/   |__/   |__/     |__/      |__/      \_______/|__/  |__/ \____  $$|__/  \__/ \______/ |__/ |__/ |__/
                                                                     /$$  \ $$                                  
                                                                    |  $$$$$$/                                  
                                                                     \______/                                   
-----------------------------
    Pilih menu:
    1. Cek Saldo
    2. Tarik Saldo
    3. Deposit Tunai
    4. Transfer Saldo
    5. Ganti PIN''')
    menu = int(input("Pilih nomor menu: "))
    return menu

def wait(t):
    # Menahan waktu dengan jumlah detik sesuai argumen
    
    # KAMUS LOKAL
    # i, t : integer
    
    # ALGORITMA
    print("Silahkan tunggu...")
    time.sleep(t)

def prompt():
    # Memberi pilihan kepada pengguna apakah akan melanjutkan pemakaian atau tidak
    
    # KAMUS LOKAL
    # ask : string
    
    # ALGORITMA
    ask = input("Apakah anda ingin melanjutkan transaksi? (y/n) ")
    if (ask == 'y'):
        return 1
    else:
        print("Terima kasih telah menggunakan ATM Pengkom.")
        return 0

def cekSaldo(rek):
    # Mencetak saldo rekening pengguna
    
    # KAMUS LOKAL
    # rek, saldo : int
    
    # ALGORITMA
    saldo = df.loc[rek][1]
    wait(1.1)
    print("Saldo anda sekarang Rp" + str(saldo) + ".")

def tarikSaldo(rek, jumlahTarik):
    # Mengurangi saldo pengguna sesuai jumlah yang ingin ditarik dan mencetak sisa saldo
    
    # KAMUS LOKAL
    # rek, jumlahTarik, saldo : int
    
    # ALGORITMA
    saldo = df.loc[rek][1]
    saldo -= jumlahTarik
    wait(1.1)
    if (saldo < 0):
        print("Gagal menarik uang. Jumlah uang yang ingin ditarik lebih besar dari saldo.")
    else:  # saldo > 0
        print("Berhasil menarik uang sebanyak Rp" + str(jumlahTarik) + ".")
        print("Sisa saldo anda sekarang Rp" + str(saldo) + ".")
        df.loc[rek][1] = saldo
        df.to_csv('data.csv')

def deposit(rek, jumlahDepo):
    # Menambah saldo pengguna sesuai jumlah yang ingin dimasukkan
    
    # KAMUS LOKAL
    # rek, jumlahDepo, saldo : int
    
    # ALGORITMA
    saldo = df.loc[rek][1]
    saldo += jumlahDepo
    wait(1.1)
    print("Berhasil mendeposit uang sebanyak Rp" + str(jumlahDepo) + ".")
    print("Sisa saldo anda sekarang Rp" + str(saldo) + ".")
    df.loc[rek][1] = saldo
    df.to_csv('data.csv')

def transfer(rek, jumlahTransfer, rekTransfer):
    # Mengurangi saldo pengguna dan menambah saldo di rekening lain yang dipilih dengan jumlah yang diinput
    
    # KAMUS LOKAL
    # rek, jumlahTransfer, rekTransfer, saldoa, saldor : int
    
    # ALGORITMA
    try:
        saldor = df.loc[rekTransfer][1]
    except:
        print("Rekening yang anda masukkan tidak valid.")
        return 0
    saldoa = df.loc[rek][1]
    saldoa = saldoa - jumlahTransfer - 2500
    wait(1.1)
    if (saldoa < 0):
        print("Gagal transfer uang. Jumlah uang yang ingin ditransfer dan biaya transfer lebih besar dari saldo.")
        saldoa = saldoa + jumlahTransfer + 2500
    else:
        print("Berhasil transfer uang sebanyak Rp" + str(jumlahTransfer) + ", dengan biaya transfer Rp2500.")
        print("Sisa saldo anda sekarang Rp" + str(saldoa) + ".")
        saldor += jumlahTransfer
        df.loc[rek][1] = saldoa
        df.loc[rekTransfer][1] = saldor
        df.to_csv('data.csv')


def gantiPIN(rek, pinbaru):
    # Mengganti pin ATM pengguna untuk autentikasi berikutnya
    
    # KAMUS LOKAL
    # rek, pinbaru : int
    
    # ALGORITMA
    if(len(pinbaru) == 6 and pinbaru.isnumeric()):
        df.loc[rek][0] = str(pinbaru)
        wait(1.1)
        print("Berhasil mengubah PIN.")
        df.to_csv('data.csv')
    else:
        print("PIN baru yang anda masukkan tidak valid.")


# inisialisasi dataframe
df = pd.read_csv("data.csv", index_col="Rekening")