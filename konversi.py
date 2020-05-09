#install tabulate di console dengan perintah
#pip install tabulate
from tabulate import tabulate

def hitungNilai(num1,num2,num3):
	num=int((num1/100*30)+int(num2/100*30)+int(num3/100*40))
	return num
	
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
	elif Akhir >= 40:
		grade = "E"
		bobot = "0,00"
	elif Akhir < 40:
		grade = "T"
		bobot = "Tunda"
	return grade
	
def main():
	loops = int(input("Jumlah Mahasiswa: "))
	inputs = []
	total=[]
	count = 0
	for x in range(loops):
		print("Input data ke-",x+1)
		nama=input("Nama: ")
		nim=input("Nim: ")
		num1=int(input("Tugas: "))
		num2=int(input("UTS: "))
		num3=int(input("UAS: "))
		akhir=hitungNilai(num1,num2,num3)
		total.append(akhir)
		grade=konversiGrade(akhir)
		count += 1 
		ele = [count,nama,nim,num1,num2,num3,akhir,grade] 
		inputs.append(ele) 
		print("")
	return inputs,total
	
	

def cetakData():	
	inputs,total=main()
	print("Laporan Nilai data sains")
	avg = sum(total)/len(total)
	print(tabulate(inputs,headers=['No', 'NIM','NAMA','TUGAS','UTS','UAS','AKHIR','GRADE']))
	print("Total Nilai :",sum(total))
	print("Total Rata - rata :",round(avg,2))
	print("Total Terendah :",min(x[6] for x in inputs))
	print("Total Tertinggi :",max(x[6] for x in inputs))
cetakData()
