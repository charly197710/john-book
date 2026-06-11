import os
from PIL import Image

def remove_background():
    try:
        from rembg import remove
        input_path = "assets/logo.png"
        output_path = "assets/logo_transparent.png"
        
        if os.path.exists(input_path):
            print(f"Removing background for {input_path}...")
            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
            print("Background removed successfully.")
        else:
            print(f"Logo not found at {input_path}")
    except Exception as e:
        print(f"Error removing background: {e}")

def crop_image(input_name, output_name, box_ratios):
    input_path = f"assets/{input_name}"
    output_path = f"assets/{output_name}"
    
    if os.path.exists(input_path):
        try:
            img = Image.open(input_path)
            width, height = img.size
            
            left = int(width * box_ratios[0])
            top = int(height * box_ratios[1])
            right = int(width * box_ratios[2])
            bottom = int(height * box_ratios[3])
            
            cropped = img.crop((left, top, right, bottom))
            cropped.save(output_path)
            print(f"Cropped and saved {output_path}")
        except Exception as e:
            print(f"Error cropping {input_name}: {e}")
    else:
        print(f"File not found: {input_path}")

def process_all():
    print("Starting image processing...")
    remove_background()
    
    # format: (left_ratio, top_ratio, right_ratio, bottom_ratio)
    
    # 350.png -> Cabina Fotos (Top Right) & Camara 360 (Bottom Right)
    crop_image("media__1779469676350.png", "cabina_fotos.png", (0.5, 0.0, 1.0, 0.5))
    crop_image("media__1779469676350.png", "camara_360.png", (0.5, 0.5, 1.0, 1.0))
    
    # 365.png -> Libro de firmas (Top Half) & VideoClick (Bottom Right)
    crop_image("media__1779469676365.png", "libro_firmas.png", (0.0, 0.0, 1.0, 0.5))
    crop_image("media__1779469676365.png", "videoclick.png", (0.5, 0.5, 1.0, 1.0))
    
    # 384.png -> Cuadro Entrada (Left half) & Retablos (Bottom Right)
    crop_image("media__1779469676384.png", "cuadro_entrada.png", (0.0, 0.0, 0.45, 1.0))
    crop_image("media__1779469676384.png", "retablos.png", (0.45, 0.5, 1.0, 1.0))
    
    # 397.png -> Fotografia Social (John Book - bottom right)
    crop_image("media__1779469676397.png", "fotografia.png", (0.4, 0.4, 1.0, 1.0))
    
    print("Finished processing images.")

if __name__ == "__main__":
    process_all()
