print ("Calculator Sederhana")
print (20* "-")
print ("Menu !")
print ("1. Penjumlahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")

menu   = input ("Silahkan pilih 1/2/3/4  : ")
angka1 = float (input("Masukan angka pertama : "))
angka2 = float (input("Masukan angka kedua   : "))
print (20* "-")

if menu == "1":
  print ("Penjumlahan")
  print (angka1 , "+" , angka2)
  hasil = angka1 + angka2
  print ("Hasilnya = ",hasil)

elif menu == "2":
  print ("Pengurangan")
  print (angka1 , "-" , angka2)
  hasil2 = angka1 - angka2
  print ("Hasilnya = ",hasil2)

elif menu == "3":
  print ("Perkalian")
  print (angka1 , "*" , angka2)
  hasil3 = angka1 * angka2
  print ("Hasilnya = ",hasil3)

elif menu == "4":
  print ("Pembagian")
  print (angka1 , "/" , angka2)
  hasil4 = angka1 / angka2
  print ("Hasilnya  = ",hasil4)

else:
  print ("Kode salah")
