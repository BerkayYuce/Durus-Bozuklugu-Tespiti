import os

# Klasör yolu
folder_path = 'PEKTUS EKSKAVATUM'
rename_factor = 'pektus ekskavatum'

# Dosya numaralandırma başlangıcı
start_number = 0

# Klasördeki her dosyayı yeniden adlandırma
for i, filename in enumerate(os.listdir(folder_path), start=start_number):
    # Dosya uzantısını koruma (örn. jpg, png)
    file_extension = os.path.splitext(filename)[1]

    # Yeni dosya adı belirleme (pektus_{numara}.jpg)
    new_filename = f"{rename_factor}_{i}{file_extension}"

    # Eski ve yeni dosya yolunu belirleme
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)

    # Dosyayı yeniden adlandırma
    os.rename(old_file, new_file)
    print(f"{filename} yeniden adlandırıldı -> {new_filename}")

print("Tüm dosyalar yeniden adlandırıldı.")
