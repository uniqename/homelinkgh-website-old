#!/usr/bin/env python3
"""
Convert HomeLinkGH phone screenshots to iPad dimensions for App Store submission
"""

from PIL import Image, ImageDraw, ImageFont
import os

def convert_to_ipad_dimensions(input_path, output_dir):
    """Convert phone screenshot to iPad dimensions with proper scaling"""
    
    # iPad dimensions
    ipad_pro_size = (2048, 2732)  # iPad Pro Portrait
    ipad_12_9_size = (2064, 2752)  # iPad 12.9" Portrait
    
    # Load original image
    original = Image.open(input_path)
    original_width, original_height = original.size
    
    # Get filename without extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    # Convert to both iPad sizes
    for size_name, (target_width, target_height) in [
        ("ipad_pro_portrait", ipad_pro_size),
        ("ipad_12_9_portrait", ipad_12_9_size)
    ]:
        # Create new image with iPad dimensions and white background
        ipad_image = Image.new('RGB', (target_width, target_height), 'white')
        
        # Calculate scaling to fit the phone screenshot centered on iPad
        # Scale to fit within 70% of iPad width to simulate tablet scaling
        max_width = int(target_width * 0.7)
        max_height = int(target_height * 0.8)
        
        # Calculate scale factor maintaining aspect ratio
        scale_w = max_width / original_width
        scale_h = max_height / original_height
        scale = min(scale_w, scale_h)
        
        # Calculate new dimensions
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        
        # Resize the original image
        resized = original.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Calculate position to center the image
        x = (target_width - new_width) // 2
        y = (target_height - new_height) // 2
        
        # Paste the resized image onto the iPad canvas
        ipad_image.paste(resized, (x, y))
        
        # Save the converted image
        output_filename = f"homelinkgh_{base_name.lower()}_{size_name}_{target_width}x{target_height}.png"
        output_path = os.path.join(output_dir, output_filename)
        ipad_image.save(output_path, 'PNG', quality=95)
        print(f"Created: {output_filename}")

def main():
    input_dir = "/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/phone_screenshots_to_convert"
    output_dir = "/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/ipad_screenshots_final"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Process all PNG files in input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")
            convert_to_ipad_dimensions(input_path, output_dir)
    
    print(f"\n✅ All iPad screenshots created in: {output_dir}")
    print("\nFiles ready for App Store Connect upload:")
    for filename in sorted(os.listdir(output_dir)):
        print(f"  - {filename}")

if __name__ == "__main__":
    main()