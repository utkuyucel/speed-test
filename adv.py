import sys
import time
import random


class Engine:

	def __init__(self, wordlist):
		self.wordlist = wordlist
		self.dondur = []
		self.new = []
		self.sayac = 1
		self.zaman = time.perf_counter()
		self.kelime_sayaci = 0

	def run(self, sort = False):
		if sort == False:
			random.shuffle(self.dondur)
			self.zaman

		if sort == True:
			self.dondur.sort()

		while True:
			for i in range(0, len(self.dondur)):

				x = input(f"{self.dondur[i]} -> ")

				if (x == "q"):
					print("Çıkış yapılıyor.")
					bitis = time.perf_counter()
					print("\nToplam yazılan kelime: ",self.kelime_sayaci, "\n")
					print(f"{bitis-self.zaman} saniye sürdü.")
					return 1

				elif (x == " "):
					continue

				elif (x not in self.dondur):
					while (x not in self.dondur):
						print("Hatalı veya eksik giriş\n")
						x = input(f"{self.dondur[i]} -> ")

						if (x == "q"):
							print("Çıkış yapılıyor.")
							bitis = time.perf_counter()
							print("\nToplam yazılan kelime: ",self.kelime_sayaci, "\n")
							print(f"{bitis-self.zaman} saniye sürdü.")
							return 1

						elif (x == " "):
							break

						elif (x in self.dondur):
							self.kelime_sayaci += 1
							continue

				self.kelime_sayaci += 1

			if 1:
				break
					
		bitis = time.perf_counter()
		son = bitis - self.zaman

		print(f"{son} saniye sürdü.")

	def getwordlist(self):
		try:
			with open(self.wordlist, "r", encoding = "utf-8") as f:
				x = f.readlines()
				for i in x:
					self.dondur.append(i.split(" "))
					self.dondur = self.dondur[0]

			
			print("Kullanılan teknik: 1\n")

			return self.dondur

		except:
			print("İkinci yol deneniyor..")
			with open(self.wordlist, "r", encoding = "utf-8") as f:
				x = f.readlines()
				for i in x:
					i = i.replace("\n", "")
					self.new.append(i)

				self.dondur = self.new

			print("Kullanılan teknik: 2\n")

			return self.dondur

def baslat():
	karistir = input("Kelimeler karıştırılsın mı? (e/h): ")

	engine = Engine("kelimeler.txt")
	engine.getwordlist()

	if (karistir == "e" or karistir == "E"):
		engine.run(False)
	elif (karistir == "h" or karistir == "H"):
		engine.run(True)

	else:
		print("Geçerli bir seçenek girin.")


baslat()

