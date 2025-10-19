"Program Kalkulator BMI"

print("Perhitungan BMI (Body Mess Index)")
print("=================================")
berat = input("Masukkan berat badan (kg) : ")
berat = float(berat)
tinggi = input("Masukkan tinggi badan (m) : ")
tinggi = float(tinggi)

bmi = berat/(tinggi**2)
berat_ideal= dict()
berat_ideal["bawah"]= 18.5*(tinggi**2)
berat_ideal["atas"]= 25*(tinggi**2)

print(f"Nilai BMI normal diantara 18.5 - 25 m^2. Hasil nilai bmi anda adalah {bmi:.2f}")
print(f"Berat badan ideal anda adalah dalam rentan {berat_ideal['bawah']:.2f} kg - {berat_ideal['atas']:.2f} kg")
print("Terimakasih telah bersedia menggunakan program ini :)")
