import math

# TUGAS 1
def konversi_suhu(nilai, satuan):
  """Mengubah suhu dari C ke F atau dari F ke C."""
  satuan = satuan.upper()  # Mengantisipasi huruf kecil

  if satuan == "C":
    hasil = (nilai * 9 / 5) + 32
    return f"{nilai}°C = {hasil:.2f}°F"
  elif satuan == "F":
    hasil = (nilai - 32) * 5 / 9
    return f"{nilai}°F = {hasil:.2f}°C"
  else:
    return "Satuan tidak valid! Gunakan 'C' atau 'F'."