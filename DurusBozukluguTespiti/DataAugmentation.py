from PIL import Image, ImageEnhance, ImageColor, ImageFilter, UnidentifiedImageError
import os

# Klasör ayarları
input_folder = 'pectus excavatum_images_resized'
output_folder = 'PEKTUS EKSKAVATUM'
os.makedirs(output_folder, exist_ok=True)

# Yeni boyut
new_size = (500, 500)

# Görselleri işleme ve veri artırma işlemleri
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_folder, filename)

        try:
            # Görseli aç ve RGB moduna dönüştür
            image = Image.open(image_path).convert('RGB')

            # Resim Rotalama
            img_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor('white', 'RGB'))
            img_rotate.save(os.path.join(output_folder, f"{filename.split('.')[0]}_rotated.jpg"))

            # Resmi aynalama (yatay ve dikey)
            img_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img_horizontal.save(os.path.join(output_folder, f"{filename.split('.')[0]}_flipped.jpg"))

            img_transverse = image.transpose(Image.Transpose.TRANSVERSE)
            img_transverse.save(os.path.join(output_folder, f"{filename.split('.')[0]}_transverse.jpg"))

            # Siyah Beyaz Çevirme
            black_and_white = image.convert("L")
            black_and_white.save(os.path.join(output_folder, f"{filename.split('.')[0]}_bw.jpg"))

            # Parlaklık Ayarı
            brightness_enhancer = ImageEnhance.Brightness(image)
            brighter_image = brightness_enhancer.enhance(1.2)
            brighter_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_bright.jpg"))

            # Renk Doygunluğu Ayarı
            color_enhancer = ImageEnhance.Color(image)
            color_image = color_enhancer.enhance(3)
            color_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_color.jpg"))

            # Kontrast Ayarı
            contrast_enhancer = ImageEnhance.Contrast(image)
            contrast_image = contrast_enhancer.enhance(2)
            contrast_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_contrast.jpg"))

            # Keskinlik Ayarı
            sharpness_enhancer = ImageEnhance.Sharpness(image)
            sharp_image = sharpness_enhancer.enhance(6)
            sharp_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_sharp.jpg"))

            # Filtreleme
            filtered_image = image.filter(ImageFilter.DETAIL)
            filtered_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_filtered.jpg"))

            print(f"{filename} için veri artırma işlemleri tamamlandı.")

        except UnidentifiedImageError:
            print(f"{filename} işlenemedi: Bu dosya geçerli bir resim değil veya bozuk.")
