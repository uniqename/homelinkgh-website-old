#!/usr/bin/env python3
"""
Create realistic iPad screenshots that look like actual device screenshots
"""

from PIL import Image, ImageDraw, ImageFilter
import os

def create_realistic_ipad_screenshot(phone_screenshot_path, output_path, ipad_size):
    """Create a realistic iPad screenshot by properly scaling the phone screenshot"""
    
    target_width, target_height = ipad_size
    
    # Load the phone screenshot
    phone_img = Image.open(phone_screenshot_path)
    phone_width, phone_height = phone_img.size
    
    # Calculate the aspect ratio
    phone_aspect = phone_width / phone_height
    ipad_aspect = target_width / target_height
    
    if phone_aspect > ipad_aspect:
        # Phone is wider relative to height, fit by width
        new_width = target_width
        new_height = int(target_width / phone_aspect)
    else:
        # Phone is taller relative to width, fit by height  
        new_height = target_height
        new_width = int(target_height * phone_aspect)
    
    # Resize the phone screenshot to fill the iPad dimensions
    resized_phone = phone_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Create the final iPad image
    if new_width == target_width:
        # Image fills width, center vertically
        ipad_img = Image.new('RGB', (target_width, target_height), '#f0f0f0')
        y_offset = (target_height - new_height) // 2
        ipad_img.paste(resized_phone, (0, y_offset))
    else:
        # Image fills height, center horizontally
        ipad_img = Image.new('RGB', (target_width, target_height), '#f0f0f0')
        x_offset = (target_width - new_width) // 2
        ipad_img.paste(resized_phone, (x_offset, 0))
    
    # For iPad screenshots, we actually want to just stretch the phone screenshot
    # to fill the entire iPad dimensions since that's what the app would do
    ipad_img = phone_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Save the result
    ipad_img.save(output_path, 'PNG', quality=95)
    print(f"Created realistic iPad screenshot: {os.path.basename(output_path)}")

def main():
    input_dir = "/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/phone_screenshots_to_convert"
    output_dir = "/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/ipad_screenshots_realistic"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # iPad dimensions for App Store
    ipad_dimensions = [
        ("ipad_pro_portrait", (2048, 2732)),
        ("ipad_12_9_portrait", (2064, 2752))
    ]
    
    # Map phone screenshots to descriptive names
    screenshot_mapping = {
        "IMG_9347.PNG": "home_services",
        "IMG_9348.PNG": "smart_picks", 
        "IMG_9349.PNG": "food_delivery"
    }
    
    # Process each phone screenshot
    for filename in os.listdir(input_dir):
        if filename.upper() in screenshot_mapping:
            screen_name = screenshot_mapping[filename.upper()]
            input_path = os.path.join(input_dir, filename)
            
            print(f"Processing {filename} as {screen_name}...")
            
            # Create both iPad sizes
            for size_name, dimensions in ipad_dimensions:
                output_filename = f"homelinkgh_{screen_name}_{size_name}_{dimensions[0]}x{dimensions[1]}.png"
                output_path = os.path.join(output_dir, output_filename)
                
                create_realistic_ipad_screenshot(input_path, output_path, dimensions)
    
    print(f"\n✅ Realistic iPad screenshots created in: {output_dir}")
    print("\nFiles ready for App Store Connect upload (in recommended order):")
    
    # List files in logical order for App Store
    screen_order = ["home_services", "smart_picks", "food_delivery"]
    for screen in screen_order:
        for filename in sorted(os.listdir(output_dir)):
            if screen in filename:
                print(f"  - {filename}")

if __name__ == "__main__":
    main()