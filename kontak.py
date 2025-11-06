"Berisi kelas kontak untuk menjalankan project manajemen kontak"

from dokumen import membuka_kontak, menyimpan_kontak

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()
    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Tidak ada kontak yang sesuai!")
            return 1


    def tambah_kontak(self):
        nama = input("Masukkan nama kontak baru: ")
        hp = input("Masukkan nomor Hp kontak baru: ")
        email = input("Masukkan email kontak baru: ")
        kontak_baru = f'{nama} ({hp}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan !")

    def hapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukkan nomor yang akan dihapus : "))
                del self.kontak[i_hapus - 1]
                print("Kontak berhasil dihapus !")
            except:
                print("Input yang anda masukkan salah!")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)