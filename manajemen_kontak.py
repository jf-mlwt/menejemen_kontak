"PROGRAM MANAJEMEN KONTAK"

class Kontak:
    def __init__(self):
        self.kontak = []
    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        else:
            print("Tidak ada kontak yang sesuai!")
            return 1


    def tambah_kontak(self):
        nama = input("Masukkan nama kontak baru: ")
        hp = input("Masukkan nomor Hp kontak baru: ")
        email = input("Masukkan email kontak baru: ")
        kontak_baru = {'nama': nama, 'hp': hp, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan !")

    def hapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan nomor yang akan dihapus : "))
            del self.kontak[i_hapus - 1]
            print("Kontak berhasil dihapus !")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kontak :")
    print("1. Melihat Semua Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("\nMasukkan pilihan anda (1,2,3 atau 4) : ")
    if pilihan == "1":
        kontak_kantor.melihat_kontak()
    elif pilihan == "2":
        kontak_kantor.tambah_kontak()
    elif pilihan == "3":
        kontak_kantor.hapus_kontak()
    elif pilihan == "4":
        break
    else:
        print("Andan memasukkan angka yang salah! silahkan diulang kembali")
