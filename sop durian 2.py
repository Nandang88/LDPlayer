pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Sob durian asli medan
    List Menu sob durian
 
    ==============================
    A. sob durian : Rp 20.000
    B. sob durian alpukat : Rp 25.000
    C. sob durian L: Rp 30.000
    D. sob durian alpukat L : Rp 35.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu durian ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "sob durian"
        harga=(20000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "sob durian alpukat"
        harga = (25000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "sob durian L"
        harga=int(30000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga = int(harga-diskon+ppn)
        else:
          diskon=0
          totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "sob durian alpukat"
        harga=int(35000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("sob durian asli medan")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")