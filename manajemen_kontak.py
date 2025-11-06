"PROGRAM MANAJEMEN KONTAK"

import kontak

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

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
            kontak_kantor.keluar_kontak()
            break
        else:
            print("Andan memasukkan angka yang salah! silahkan diulang kembali")

if __name__ == "__main__":
    main()