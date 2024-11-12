from PIL import Image, ImageEnhance, ImageFilter, UnidentifiedImageError
import os

# Klasör ayarları
input_folder = 'pectus excavatum_images'  # İşlenecek görsellerin bulunduğu klasör
output_folder = 'pectus excavatum_images_resized'  # İşlenmiş görsellerin kaydedileceği klasör
os.makedirs(output_folder, exist_ok=True)

# Yeniden boyutlandırma için hedef boyut
new_size = (256, 256)

# Görselleri işleme ve kalite artırma işlemi
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Yalnızca jpg ve png dosyaları
        image_path = os.path.join(input_folder, filename)

        try:
            # Görseli aç ve RGB moduna dönüştür
            image = Image.open(image_path).convert('RGB')

            # Görseli yeniden boyutlandırma
            img_resized = image.resize(new_size)

            # Keskinlik artırma
            enhancer = ImageEnhance.Sharpness(img_resized)
            enhanced_image = enhancer.enhance(2.0)  # Keskinliği artır (1.0 normal, 2.0 artırılmış)

            # Detay filtresi uygulama
            final_image = enhanced_image.filter(ImageFilter.DETAIL)

            # İşlenmiş görseli kaydet
            output_path = os.path.join(output_folder, f"enhanced_resized_{filename}")
            final_image.save(output_path)
            print(f"{filename} başarıyla işlenip kaydedildi.")

        except UnidentifiedImageError:
            print(f"{filename} işlenemedi: Bu dosya geçerli bir resim değil veya bozuk.")
        except Exception as e:
            print(f"{filename} işlenirken hata oluştu: {e}")
