"PROGRAM MANAJEMEN KONTAK"

kontak1 = {'nama' : 'Jana', 'hp' : '085216470753', 'email' : 'jana@gmail.com'}
kontak2 = {'nama' : 'Fauzi', 'hp' : '082244395803', 'email' : 'fauzi@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak :")
    print("1. Melihat Semua Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("\nMasukkan pilihan anda (1,2,3 atau 4) : ")
    if pilihan == "1":
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        else:
            print("Tidak ada kontak yang sesuai!")
    elif pilihan == "2":
        nama = input("Masukkan nama kontak baru: ")
        hp = input("Masukkan nomor Hp kontak baru: ")
        email = input("Masukkan email kontak baru: ")
        kontak_baru = {'nama': nama, 'hp' : hp, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan !")
    elif pilihan == "3":
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        else:
            print("Tidak ada kontak yang sesuai!")
            continue

        i_hapus = int(input("Masukkan nomor yang akan dihapus : "))
        del kontak[i_hapus-1]
        print("Kontak berhasil dihapus !")
    elif pilihan == "4":
        break
    else:
        print("Andan memasukkan angka yang salah! silahkan diulang kembali")
