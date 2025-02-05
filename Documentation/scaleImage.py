from PIL import Image
import os

def rotate_image_360(image_path, output_folder, degrees_step=2):
    # Open the image
    image = Image.open(image_path)
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract the filename and extension from the original image path
    filename, ext = os.path.splitext(os.path.basename(image_path))
    
    # Initialize the rotation angle
    angle = 0
    
    # Loop to rotate the image from 0 to 360 degrees in steps of `degrees_step`
    while angle <= 360:
        # Rotate the image by the current angle
        rotated_image = image.rotate(angle, expand=True)
        
        # Create the output filename
        output_filename = f"{filename}_rotated_{angle}_degrees{ext}"
        output_path = os.path.join(output_folder, output_filename)
        
        # Save the rotated image
        rotated_image.save(output_path)
        
        print(f"Image rotated by {angle} degrees and saved to {output_path}")
        
        # Increment the angle by `degrees_step`
        angle += degrees_step

# Example usage
image_path = "path/to/your/image.jpg"
output_folder = "path/to/output/folder"
rotate_image_360(image_path, output_folder)