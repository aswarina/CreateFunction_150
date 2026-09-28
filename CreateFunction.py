#Tugas 1

def converts_temperature(value, unit):
    if unit == 'C':
        return value * 9/5 + 32
    elif unit == 'F':
        return (value - 32) * 5/9

input_value = int(input("Masukkan value : "))
input_unit = input("Masukkan unit : ")

konversi = converts_temperature(input_value, input_unit)

if input_unit == 'C':
    print("Hasil:", konversi)
else:
    print("Hasil:", konversi) 

#Tugas 2
luas_lingkaran = lambda r: 3.14 * r ** 2                # Fungsi lambda (anonim) untuk menghitung luas lingkaran

input_r = float(input("\nMasukkan r : "))              # Mengambil input jari-jari (float/desimal)
print("Luas :", luas_lingkaran(input_r))                
# Memanggil lambda & mencetak hasil luasnya 