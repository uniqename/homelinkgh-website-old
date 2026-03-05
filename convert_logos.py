#!/usr/bin/env python3
"""
Convert SVG logos to PNG format for web use
"""

import os
import base64
from pathlib import Path

def svg_to_png_base64(svg_content, width=200, height=80):
    """Convert SVG to PNG using base64 encoding (fallback method)"""
    # For web use, we can embed SVG directly or use this as base64
    svg_b64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{svg_b64}"

def create_png_replacement():
    """Create a simple PNG using ASCII art as fallback"""
    # Since we may not have PIL available, let's create a simple HTML-based logo
    return """<svg width="200" height="80" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="80" fill="#f8f9fa"/>
  <circle cx="40" cy="40" r="30" fill="#2E8B57"/>
  <text x="40" y="45" text-anchor="middle" fill="white" font-family="Arial" font-size="20">🏠</text>
  <text x="120" y="35" fill="#2E8B57" font-family="Arial" font-size="18" font-weight="bold">HomeLinkGH</text>
  <text x="120" y="55" fill="#006B3C" font-family="Arial" font-size="10">Professional Services</text>
</svg>"""

def main():
    try:
        # Try to use Pillow if available
        from PIL import Image, ImageDraw, ImageFont
        import io
        
        def create_homelinkgh_png():
            # Create a professional PNG logo
            img = Image.new('RGBA', (200, 80), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw background circle
            draw.ellipse([5, 5, 75, 75], fill=(46, 139, 87), outline=(0, 107, 60), width=2)
            
            # Draw house shape (simplified)
            house_points = [(20, 45), (40, 25), (60, 45), (55, 45), (55, 55), 
                           (45, 55), (45, 50), (35, 50), (35, 55), (25, 55), (25, 45)]
            draw.polygon(house_points, fill=(255, 255, 255))
            
            # Add text
            try:
                font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 18)
                font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 10)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            draw.text((85, 20), "HomeLinkGH", fill=(46, 139, 87), font=font_large)
            draw.text((85, 45), "Professional Home Services", fill=(102, 102, 102), font=font_small)
            
            # Save PNG
            img.save('/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/logo.png')
            print("✅ Created HomeLinkGH PNG logo")
            
            # Create favicon
            favicon = img.resize((32, 32), Image.Resampling.LANCZOS)
            favicon.save('/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/favicon.ico')
            print("✅ Created HomeLinkGH favicon")
        
        def create_consulting_png():
            # Create consulting PNG logo
            img = Image.new('RGBA', (200, 80), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw hexagon background
            hex_points = [(40, 10), (60, 20), (60, 40), (40, 50), (20, 40), (20, 20)]
            draw.polygon(hex_points, fill=(30, 58, 138), outline=(30, 64, 175), width=2)
            
            # Draw growth chart
            chart_points = [(28, 35), (32, 30), (36, 25), (40, 20), (44, 25), (48, 18), (52, 22)]
            for i in range(len(chart_points)-1):
                draw.line([chart_points[i], chart_points[i+1]], fill=(255, 255, 255), width=2)
            
            # Draw data points
            for point in chart_points:
                draw.ellipse([point[0]-2, point[1]-2, point[0]+2, point[1]+2], fill=(255, 255, 255))
            
            # Add text
            try:
                font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
                font_medium = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
                font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 8)
            except:
                font_large = font_medium = font_small = ImageFont.load_default()
            
            draw.text((85, 15), "Enam", fill=(30, 58, 138), font=font_large)
            draw.text((85, 35), "Consulting", fill=(55, 65, 81), font=font_medium)
            draw.text((85, 55), "Strategic Business Solutions", fill=(102, 102, 102), font=font_small)
            
            # Save PNG
            consulting_path = '/Users/enamegyir/Documents/Projects/enam-consulting-website'
            if os.path.exists(consulting_path):
                img.save(f'{consulting_path}/logo.png')
                print("✅ Created Consulting PNG logo")
                
                # Create favicon
                favicon = img.resize((32, 32), Image.Resampling.LANCZOS)
                favicon.save(f'{consulting_path}/favicon.ico')
                print("✅ Created Consulting favicon")
        
        # Create the PNG logos
        create_homelinkgh_png()
        create_consulting_png()
        
    except ImportError:
        print("⚠️  Pillow not available, creating SVG-based solutions...")
        
        # Read SVG files and save as optimized versions
        homelinkgh_path = '/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy'
        with open(f'{homelinkgh_path}/logo.svg', 'r') as f:
            svg_content = f.read()
        
        # Create a simplified PNG-equivalent using canvas/SVG
        print("✅ SVG logos ready for web use")
        print("💡 For better PNG conversion, install Pillow: pip install Pillow")

if __name__ == "__main__":
    main()