"Program Kalkulator BMI"

print("Perhitungan BMI (Body Mess Index)")
print("=================================")
berat = float(input("Masukkan berat badan (kg) : "))
tinggi = float(input("Masukkan tinggi badan (m) : "))

bmi = berat/(tinggi**2)
berat_ideal= dict()
berat_ideal["bawah"]= 18.5*(tinggi**2)
berat_ideal["atas"]= 25*(tinggi**2)

if bmi < 18.5:
    kondisi = "Anda kekurangan berat badan :("
elif bmi <= 25:
    kondisi = "Anda memiliki berat badan yang normal :)"
elif bmi <= 30:
    kondisi = "Anda mengalami kelebihan berat badan :D"
else:
    kondisi = "Anda mengalami obesitas"

print("\nHasil Perhitungan Kalkulator BMI")
print("================================")
print(f"Hasil nilai bmi anda adalah {bmi:.2f}")
print(f"{kondisi}")
print(f"Berat badan ideal anda adalah dalam rentan {berat_ideal['bawah']:.2f} kg - {berat_ideal['atas']:.2f} kg")
print("Terimakasih telah bersedia menggunakan program ini :)")
