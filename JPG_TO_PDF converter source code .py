from PIL import Image
import os

def convert_all_jpgs_to_pdfs(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    os.makedirs(destination_folder, exist_ok=True)

    # Get all JPG/JPEG files
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg'))]

    if not jpg_files:
        print("No JPG files found in source folder.")
        return

    for image_name in jpg_files:
        image_path = os.path.join(source_folder, image_name)
        try:
            image = Image.open(image_path)

            # Convert to RGB if needed
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            pdf_name = os.path.splitext(image_name)[0] + ".pdf"
            pdf_path = os.path.join(destination_folder, pdf_name)

            image.save(pdf_path, "PDF")
            print(f"Converted: {image_name} → {pdf_name}")
        
        except Exception as e:
            print(f"Failed to convert {image_name}: {e}")

# Example usage
if __name__ == "__main__":
    src_folder = input("Enter source folder path (where JPG files are): ")
    dest_folder = input("Enter destination folder path (to save PDFs): ")
    convert_all_jpgs_to_pdfs(src_folder, dest_folder)
