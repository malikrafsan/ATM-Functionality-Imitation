# PROGRAM main
# Simulasi kerja ATM
# Program utama yang akan dijalankan saat membuka ATM

# KAMUS
# df : pandas dataframe
# rek, pin, saldo, tries, me, jumlahTarik, jumlahDepo, rekTransfer, pinbaru: int

# ALGORITMA

# import library pandas dan fungsi buatan pada file fungsiatm
import pandas as pd
import fungsiatm as fn

#deklarasi tipe data per kolom dataframe
dtype_dic = {'Rekening': int,
            'PIN': str,
            'Saldo': int
}
#inisialisasi dataframe
df = pd.read_csv("data.csv", index_col="Rekening", dtype=dtype_dic)
tries = 0
rek = ""

#Penyocokan rekening dengan yang ada di database
while (rek not in df["PIN"]):
    rek = int(input("Masukkan rekening anda: "))
    if (rek not in df["PIN"]):
        print("Rekening anda tidak valid. Silahkan coba lagi.")

#Autentikasi PIN
while (tries < 3):
    try:
        pin = int(input("Masukkan PIN: "))
        if (str(pin) == df.loc[rek][0]):
            saldo = df.loc[rek][1]
            break
        else:
            raise KeyError
    except KeyError:
        if (tries < 2):
            print("PIN anda salah. Coba lagi. (" + str(2-tries) + " percobaan lagi).")
        else:
            print("Kartu ATM anda terblokir. Silahkan hubungi Bank terdekat.")
            exit()
        tries += 1

#Main menu
me = 0
while True:
    me = fn.menu()
    if me == 1:
        #Pilihan menu pertama, cek saldo
        fn.cekSaldo(rek)
        if (fn.prompt() == 0):
            break
    elif me == 2:
        #Pilihan menu kedua, tarik saldo
        jumlahTarik = int(input("Masukkan jumlah saldo yang ingin ditarik: "))
        fn.tarikSaldo(rek, jumlahTarik)
        if (fn.prompt() == 0):
            break
    elif me == 3:
        #Pilihan menu ketiga, deposit tunai
        jumlahDepo = int(input("Masukkan jumlah uang yang ingin dideposit: "))
        fn.deposit(rek, jumlahDepo)
        if (fn.prompt() == 0):
            break
    elif me == 4:
        #Pilihan menu keempat, Transfer
        rekTransfer = int(input("Rekening tujuan: "))
        jumlahTransfer = int(input("Masukkan jumlah uang yang ingin ditransfer: "))
        fn.transfer(rek, jumlahTransfer, rekTransfer)
        if (fn.prompt() == 0):
            break
    elif me == 5:
        #Pilihan menu kelima, ganti PIN
        pinbaru = input("Masukkan PIN baru: ")
        fn.gantiPIN(rek, pinbaru)
        if (fn.prompt() == 0):
            break
    else:
        #Bila nomor menu tidak valid
        print("Nomor menu tidak valid.")
        if (fn.prompt() == 0):
            break