class buku:
	def _init_ (self, judul, penulis, genre, status):
		self.judul = judul
		self.penulis = penulis
		self.genre = genre
		self.status = status
		
	def _str_(self):
		return f'{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}'
		
class perpustakaan:
	def _init_(self):
		self.koleksi_buku = [ ]
		
	def tampilkan_buku(self):
		if self.koleksi_buku:
			print("--Daftar buku--")
			for buku in self.koleksi_buku:
				print(buku)
		else:
			print("koleksi buku masih kosong.")
			
	def cari_buku(self, judul):
		for buku in self.koleksi_buku:
			if buku.judul.lower( ) == judul.lower( ):
				print(buku)
				return
		print(f'buku dengan judul tidak ditemukan.')
		
	def pinjam_buku(self, buku, anggota):
		if buku.status == "tersedia":
			buku.status = "dipinjam"
			anggota.buku_pinjaman.append(buku)
			print(f'buku "{buku.judul}" berhasil dipinjam oleh {anggota.nama}.')
			print(f'buku "{buku.judul}" tidak tersedia untuk dipinjam.')
				
class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_pinjaman = []

    def pinjam_buku(self, buku):
        self.buku_pinjaman.append(buku)
        print(f"{self.nama} berhasil meminjam buku {buku}")

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"{self.nama} memiliki buku pinjaman:")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman saat ini")
    def main():
        #Buat beberapa buku
        buku1=Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
        buku2=Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
        buku3=Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam")
        
        #Buat perpustakaan dan anggota
        perpustakaan = Perpustakaan()
        perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])
        anggota1=Anggota("Andi", 12345)
        anggota2=Anggota("Budi", 56789)
        
        #Jalankan program
        print("\n-- Menu Perpustakaan --")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan")
        angka=int(input("pilih menu: "))
        if angka == 1:
            perpustakaan.tampilkan_buku();
        elif angka == 2:
            judul=input("input judul buku:")
            perpustakaan.cari_buku(judul);
        elif angka == 3:
            buku=input("buku yang di pinjam:")
            anggota=input("input nama anggota :")
            perpustakaan.pinjam_buku(buku,anggota)
        else:
            print("anda salah pilih")
        if _name_=="__main__":
            main();