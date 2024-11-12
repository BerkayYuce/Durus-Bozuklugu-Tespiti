from PIL import Image, UnidentifiedImageError
import os

# Klasör ayarları
input_folder = 'fotolar'
output_folder = 'fotolar_resized'
os.makedirs(output_folder, exist_ok=True)

# Yeni Boyutu ayarlama
new_size = (256, 256)

# Görselleri işleme ve boyut artırma
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_folder, filename)

        try:
            # Görseli aç
            image = Image.open(image_path).convert('RGB')

            # Görseli yeniden boyutlandırma
            img_resized = image.resize(new_size)

            # Yeni görseli kaydetme
            img_resized.save(os.path.join(output_folder, f"{filename.split('.')[0]}_resized.jpg"))

            print(f"{filename} için boyut artırma işlemi tamamlandı.")

        except UnidentifiedImageError:
            print(f"{filename} işlenemedi: Bu dosya geçerli bir resim değil veya bozuk.")
