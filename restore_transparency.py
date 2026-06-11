from PIL import Image, ImageDraw

def restore_transparency(input_path, output_path):
    # Open the image and convert to RGBA
    img = Image.open(input_path).convert("RGBA")
    
    # Flood fill from the 4 corners to replace near-black with transparent
    # thresh=30 allows for slight JPEG compression artifacts around pure black
    corners = [(0, 0), (img.width - 1, 0), (0, img.height - 1), (img.width - 1, img.height - 1)]
    for corner in corners:
        ImageDraw.floodfill(img, corner, (0, 0, 0, 0), thresh=25)
    
    # Save the resulting transparent PNG
    img.save(output_path)

if __name__ == "__main__":
    restore_transparency('assets/logo_oficial.jpg', 'assets/logo_restored.png')
    print("Transparencia restaurada con exito!")
