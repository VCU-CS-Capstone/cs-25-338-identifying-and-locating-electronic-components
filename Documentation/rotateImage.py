from PIL import Image
import os

def rotate_image(image_path, output_folder, degrees=2):
    # Open the image
    image = Image.open(image_path)
    
    # Rotate the image by the specified degrees
    rotated_image = image.rotate(degrees, expand=True)
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract the filename from the original image path
    filename = os.path.basename(image_path)
    
    # Create the output path
    output_path = os.path.join(output_folder, filename)
    
    # Save the rotated image
    rotated_image.save(output_path)
    
    print(f"Rotated image saved to {output_path}")

# Example usage
image_path = "path/to/your/image.jpg"
output_folder = "path/to/output/folder"
rotate_image(image_path, output_folder)