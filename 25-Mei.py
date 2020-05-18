#install tabulate di console dengan perintah
#pip install tabulate
#pip install numpy 
import numpy as np
from tabulate import tabulate
#Fungsi untuk menghitung nilai
def HitungNilaiAkhir(absen,num1,num2,num3):
	num=float(int(absen/100*10)+int(num1/100*20)+int(num2/100*30)+int(num3/100*40))
	return num

#Fungsi untuk Konversi Grade	
def konversiGrade(akhir):
	Akhir = int(akhir)
	if Akhir >= 90:
		grade = "A"
		bobot = "4,00"
	elif Akhir >= 85:
		grade = "A-"
		bobot = "3,70"
	elif Akhir >= 80:
		grade = "B+"
		bobot = "3,30"
	elif Akhir >= 75:
		grade = "B"
		bobot = "2,70"
	elif Akhir >= 70:
		grade = "B-"
		bobot = "2,30"
	elif Akhir >= 65:
		grade = "C+"
		bobot = "2,00"
	elif Akhir >= 60:
		grade = "C-"
		bobot = "1,70"
	elif Akhir >= 50:
		grade = "D"
		bobot = "1,00"
	elif Akhir < 40:
		grade = "E"
		bobot = "0,00"
	elif Akhir < 40:
		grade = "T"
		bobot = "Tunda"
	return grade
	
#Fungsi Main
def main():
	loops = int(input("Jumlah Mahasiswa: "))
	inputs = []
	total=[]
	my_array=[]
	count = 0
	for x in range(loops):
		print("Input data ke-",x+1)
		nama=input("Nama: ")
		nim=input("Nim: ")
		absen=int(input("Absen: "))
		num1=int(input("Tugas: "))
		num2=int(input("UTS: "))
		num3=int(input("UAS: "))
		akhir=HitungNilaiAkhir(absen,num1,num2,num3)
		total.append(akhir)
		grade=konversiGrade(akhir)
		count += 1 
		ele = [count,nama,nim,absen,num1,num2,num3,akhir,grade] 
		inputs.append(ele) 
		inputan= np.array((inputs),dtype=object)
		print("")
		print(inputan)
	return inputs,total,inputan
	
	
#Fungsi untuk mencetak data
def cetakData():	
	inputs,total,inputan =main()
	print("Laporan Nilai data sains")
	avg = sum(total)/len(total)
	print(tabulate(inputs,headers=['No', 'NIM','NAMA','Nilai Absen','TUGAS','UTS','UAS','AKHIR','GRADE']))
	print("Total Nilai :",sum(total))
	print("Total Rata - rata :",round(avg,2))
cetakData()
