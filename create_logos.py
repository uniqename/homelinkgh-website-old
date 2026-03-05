#!/usr/bin/env python3
"""
Create professional logos for HomeLinkGH websites
"""

import os
from pathlib import Path

def create_homelinkgh_logo_svg():
    """Create professional HomeLinkGH logo with Ghana flag colors"""
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
  <!-- Background circle -->
  <circle cx="40" cy="40" r="35" fill="#2E8B57" stroke="#006B3C" stroke-width="2"/>
  
  <!-- House icon -->
  <path d="M20 45 L40 25 L60 45 L55 45 L55 55 L45 55 L45 50 L35 50 L35 55 L25 55 L25 45 Z" 
        fill="white" stroke="none"/>
  
  <!-- Chimney -->
  <rect x="48" y="28" width="4" height="8" fill="white"/>
  
  <!-- Door -->
  <rect x="37" y="50" width="6" height="5" fill="#2E8B57"/>
  <circle cx="41" cy="52.5" r="0.5" fill="white"/>
  
  <!-- Text: HomeLinkGH -->
  <text x="85" y="30" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#2E8B57">
    HomeLink
  </text>
  <text x="85" y="50" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#006B3C">
    GH
  </text>
  
  <!-- Ghana flag accent -->
  <rect x="85" y="55" width="30" height="8" fill="#CE1126"/>
  <rect x="85" y="57.67" width="30" height="2.67" fill="#FCD116"/>
  <rect x="85" y="60.33" width="30" height="2.67" fill="#006B3C"/>
  
  <!-- Tagline -->
  <text x="85" y="72" font-family="Arial, sans-serif" font-size="8" fill="#666">
    Professional Home Services
  </text>
</svg>'''
    return svg_content

def create_consulting_logo_svg():
    """Create professional consulting logo"""
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
  <!-- Background hexagon -->
  <polygon points="40,10 60,20 60,40 40,50 20,40 20,20" 
           fill="#1E3A8A" stroke="#1E40AF" stroke-width="2"/>
  
  <!-- Consulting icon - graph/chart -->
  <path d="M28 35 L32 30 L36 25 L40 20 L44 25 L48 18 L52 22" 
        stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/>
  
  <!-- Data points -->
  <circle cx="28" cy="35" r="2" fill="white"/>
  <circle cx="32" cy="30" r="2" fill="white"/>
  <circle cx="36" cy="25" r="2" fill="white"/>
  <circle cx="40" cy="20" r="2" fill="white"/>
  <circle cx="44" cy="25" r="2" fill="white"/>
  <circle cx="48" cy="18" r="2" fill="white"/>
  <circle cx="52" cy="22" r="2" fill="white"/>
  
  <!-- Text: Enam -->
  <text x="85" y="28" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#1E3A8A">
    Enam
  </text>
  
  <!-- Text: Consulting -->
  <text x="85" y="48" font-family="Arial, sans-serif" font-size="16" fill="#374151">
    Consulting
  </text>
  
  <!-- Underline accent -->
  <rect x="85" y="52" width="80" height="2" fill="#1E40AF"/>
  
  <!-- Tagline -->
  <text x="85" y="68" font-family="Arial, sans-serif" font-size="8" fill="#666">
    Strategic Business Solutions
  </text>
</svg>'''
    return svg_content

def save_svg_file(content, filepath):
    """Save SVG content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filepath}")

def create_favicon_svg(logo_type="homelinkgh"):
    """Create favicon-ready SVG (simplified)"""
    if logo_type == "homelinkgh":
        svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <circle cx="16" cy="16" r="15" fill="#2E8B57"/>
  <path d="M8 18 L16 10 L24 18 L22 18 L22 22 L18 22 L18 20 L14 20 L14 22 L10 22 L10 18 Z" 
        fill="white"/>
  <rect x="19" y="12" width="2" height="4" fill="white"/>
</svg>'''
    else:  # consulting
        svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <polygon points="16,4 24,8 24,16 16,20 8,16 8,8" fill="#1E3A8A"/>
  <path d="M10 14 L12 12 L14 10 L16 8 L18 10 L20 7 L22 9" 
        stroke="white" stroke-width="1.5" fill="none"/>
  <circle cx="10" cy="14" r="1" fill="white"/>
  <circle cx="12" cy="12" r="1" fill="white"/>
  <circle cx="14" cy="10" r="1" fill="white"/>
  <circle cx="16" cy="8" r="1" fill="white"/>
  <circle cx="18" cy="10" r="1" fill="white"/>
  <circle cx="20" cy="7" r="1" fill="white"/>
  <circle cx="22" cy="9" r="1" fill="white"/>
</svg>'''
    return svg_content

def main():
    # Create logos directory
    current_dir = Path('/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy')
    
    # Create HomeLinkGH logo
    homelinkgh_logo = create_homelinkgh_logo_svg()
    save_svg_file(homelinkgh_logo, current_dir / 'logo.svg')
    
    # Create HomeLinkGH favicon
    homelinkgh_favicon = create_favicon_svg("homelinkgh")
    save_svg_file(homelinkgh_favicon, current_dir / 'favicon.svg')
    
    # Create consulting logo
    consulting_dir = Path('/Users/enamegyir/Documents/Projects/enam-consulting-website')
    if consulting_dir.exists():
        consulting_logo = create_consulting_logo_svg()
        save_svg_file(consulting_logo, consulting_dir / 'logo.svg')
        
        consulting_favicon = create_favicon_svg("consulting")
        save_svg_file(consulting_favicon, consulting_dir / 'favicon.svg')
    
    print("\n✅ All logos created successfully!")
    print("- HomeLinkGH: Professional home services logo with Ghana colors")
    print("- Consulting: Clean business consulting logo with growth chart")
    print("\nNext: Convert SVG to PNG/ICO formats for web use")

if __name__ == "__main__":
    main()