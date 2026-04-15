import os
from PIL import Image

def convert_png_to_webp(directory, quality=80):
    """
    Converts all .png files in the specified directory to .webp.
    Deletes the original .png file after successful conversion.
    """
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]
    
    if not files:
        print("No .png files found in the directory.")
        return

    print(f"Found {len(files)} files to convert.")

    for filename in files:
        png_path = os.path.join(directory, filename)
        webp_filename = os.path.splitext(filename)[0] + '.webp'
        webp_path = os.path.join(directory, webp_filename)

        try:
            with Image.open(png_path) as img:
                img.save(webp_path, 'webp', quality=quality)
            import shutil
            png_dest = os.path.join(directory, 'png', filename)
            if not os.path.exists(os.path.join(directory, 'png')):
                os.makedirs(os.path.join(directory, 'png'))
            
            shutil.move(png_path, png_dest)
            print(f"Moved original to png folder: {filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    assets_dir = "./assets"
    convert_png_to_webp(assets_dir, quality=80)
    print("Optimization Complete!")
