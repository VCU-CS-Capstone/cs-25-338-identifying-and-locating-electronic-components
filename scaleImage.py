from PIL import Image
import os

def shrink_image(image_path, output_folder):
    # Open the image
    image = Image.open(image_path)
    
    # Get the original size of the image
    original_width, original_height = image.size
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize the scaling factor
    scale_factor = 1.0
    
    # Loop to shrink the image by 1% until it reaches 50% of its original size
    while scale_factor >= 0.5:
        # Calculate the new size
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        # Resize the image
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        
        # Create the output filename
        filename = f"shrunk_{int(scale_factor * 100)}_percent.jpg"
        output_path = os.path.join(output_folder, filename)
        
        # Save the resized image
        resized_image.save(output_path)
        
        print(f"Image shrunk to {int(scale_factor * 100)}% of original size and saved to {output_path}")
        
        # Decrease the scale factor by 1%
        scale_factor -= 0.01

# Example usage
image_path = "path/to/your/image.jpg"
output_folder = "path/to/output/folder"
shrink_image(image_path, output_folder)