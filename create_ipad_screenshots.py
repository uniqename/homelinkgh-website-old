#!/usr/bin/env python3
"""
Create professional iPad screenshots for HomeLinkGH App Store submission.
Generates realistic iPad layouts for the home services and food delivery app.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# iPad dimensions for App Store
IPAD_PRO_PORTRAIT = (2048, 2732)  # 12.9" iPad Pro Portrait
IPAD_12_9_PORTRAIT = (2064, 2752)  # 12.9" iPad Portrait (newer)

# HomeLinkGH brand colors (from website analysis)
BRAND_GREEN = "#2E8B57"  # Primary green
BRAND_ORANGE = "#FF6B35"  # Accent orange  
BRAND_GOLD = "#FFA500"   # Ghana flag gold
BRAND_RED = "#CE1126"    # Ghana flag red
BRAND_DARK = "#1a1a1a"   # Dark text
BRAND_GRAY = "#666666"   # Secondary text
BACKGROUND_LIGHT = "#f8f9fa"  # Light background
WHITE = "#ffffff"

def create_ipad_screenshot(width, height, screen_type, filename):
    """Create a professional iPad screenshot"""
    
    # Create the main image
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts (fallback to default if not available)
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttc", 80)
        header_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttc", 60)
        body_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttc", 40)
        small_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttc", 32)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    if screen_type == "home":
        create_home_screen(draw, width, height, title_font, header_font, body_font, small_font)
    elif screen_type == "services":
        create_services_screen(draw, width, height, title_font, header_font, body_font, small_font)
    elif screen_type == "booking":
        create_booking_screen(draw, width, height, title_font, header_font, body_font, small_font)
    elif screen_type == "profile":
        create_profile_screen(draw, width, height, title_font, header_font, body_font, small_font)
    
    return img

def create_home_screen(draw, width, height, title_font, header_font, body_font, small_font):
    """Create the home screen with main services"""
    
    # Status bar
    draw.rectangle([0, 0, width, 100], fill=BRAND_GREEN)
    draw.text((width//2 - 200, 30), "9:41 AM", fill=WHITE, font=body_font, anchor="mm")
    
    # Header with logo area
    draw.rectangle([0, 100, width, 300], fill=BRAND_GREEN)
    
    # Logo placeholder (circular)
    logo_x, logo_y = 150, 150
    draw.ellipse([logo_x, logo_y, logo_x + 100, logo_y + 100], fill=WHITE)
    draw.text((logo_x + 50, logo_y + 50), "🏠", fill=BRAND_GREEN, font=header_font, anchor="mm")
    
    # App title and tagline
    draw.text((300, 170), "HomeLinkGH", fill=WHITE, font=title_font)
    draw.text((300, 240), "Professional Home Services Ghana", fill=WHITE, font=body_font)
    
    # Search bar
    search_y = 350
    draw.rectangle([100, search_y, width-100, search_y+80], fill=WHITE, outline=BRAND_GRAY)
    draw.text((130, search_y+40), "🔍 Search for services...", fill=BRAND_GRAY, font=body_font, anchor="lm")
    
    # Quick access buttons
    quick_y = 480
    button_width = (width - 300) // 3
    
    services = [
        ("🍽️", "Food\nDelivery", BRAND_ORANGE),
        ("🛒", "Grocery\nShopping", BRAND_GREEN),
        ("🧹", "Cleaning\nServices", BRAND_GOLD)
    ]
    
    for i, (icon, text, color) in enumerate(services):
        x = 100 + i * (button_width + 50)
        draw.rectangle([x, quick_y, x + button_width, quick_y + 180], fill=color, outline=color)
        draw.text((x + button_width//2, quick_y + 60), icon, fill=WHITE, font=header_font, anchor="mm")
        draw.text((x + button_width//2, quick_y + 130), text, fill=WHITE, font=small_font, anchor="mm")
    
    # Recent orders section
    recent_y = 720
    draw.text((100, recent_y), "Recent Orders", fill=BRAND_DARK, font=header_font)
    
    orders = [
        "House Cleaning - Completed",
        "Food Delivery - In Progress", 
        "Plumbing Repair - Scheduled"
    ]
    
    for i, order in enumerate(orders):
        order_y = recent_y + 80 + i * 100
        draw.rectangle([100, order_y, width-100, order_y + 80], fill=BACKGROUND_LIGHT, outline=BRAND_GRAY)
        draw.text((130, order_y + 40), order, fill=BRAND_DARK, font=body_font, anchor="lm")
        draw.text((width-130, order_y + 40), "View →", fill=BRAND_GREEN, font=body_font, anchor="rm")

def create_services_screen(draw, width, height, title_font, header_font, body_font, small_font):
    """Create the services listing screen"""
    
    # Header
    draw.rectangle([0, 0, width, 200], fill=BRAND_GREEN)
    draw.text((100, 100), "← All Services", fill=WHITE, font=header_font, anchor="lm")
    
    # Filter tabs
    tab_y = 250
    tabs = ["All", "Food", "Home", "Beauty", "Repairs"]
    tab_width = (width - 200) // len(tabs)
    
    for i, tab in enumerate(tabs):
        x = 100 + i * tab_width
        color = BRAND_ORANGE if i == 0 else BACKGROUND_LIGHT
        text_color = WHITE if i == 0 else BRAND_DARK
        draw.rectangle([x, tab_y, x + tab_width - 20, tab_y + 60], fill=color)
        draw.text((x + tab_width//2 - 10, tab_y + 30), tab, fill=text_color, font=body_font, anchor="mm")
    
    # Service cards grid
    services = [
        ("🍕", "Food Delivery", "Order from local restaurants", "4.8 ⭐", BRAND_ORANGE),
        ("🧹", "House Cleaning", "Professional cleaning service", "4.9 ⭐", BRAND_GREEN),
        ("🔧", "Home Repairs", "Plumbing, electrical & more", "4.7 ⭐", BRAND_GOLD),
        ("💄", "Beauty Services", "Makeup & nail services", "4.8 ⭐", BRAND_RED),
        ("👕", "Laundry Service", "Wash, dry & fold service", "4.6 ⭐", BRAND_GREEN),
        ("🛒", "Grocery Shopping", "Personal shopping service", "4.9 ⭐", BRAND_ORANGE)
    ]
    
    card_width = (width - 300) // 2
    card_height = 250
    
    for i, (icon, title, desc, rating, color) in enumerate(services):
        row = i // 2
        col = i % 2
        x = 100 + col * (card_width + 100)
        y = 400 + row * (card_height + 50)
        
        # Card background
        draw.rectangle([x, y, x + card_width, y + card_height], fill=WHITE, outline=BRAND_GRAY)
        
        # Service icon
        draw.text((x + 50, y + 50), icon, fill=color, font=header_font)
        
        # Service details
        draw.text((x + 120, y + 40), title, fill=BRAND_DARK, font=body_font)
        draw.text((x + 120, y + 90), desc, fill=BRAND_GRAY, font=small_font)
        draw.text((x + 120, y + 130), rating, fill=BRAND_ORANGE, font=small_font)
        
        # Book button
        draw.rectangle([x + card_width - 120, y + 180, x + card_width - 20, y + 220], fill=color)
        draw.text((x + card_width - 70, y + 200), "Book", fill=WHITE, font=small_font, anchor="mm")

def create_booking_screen(draw, width, height, title_font, header_font, body_font, small_font):
    """Create the booking/order screen"""
    
    # Header
    draw.rectangle([0, 0, width, 200], fill=BRAND_GREEN)
    draw.text((100, 100), "← House Cleaning", fill=WHITE, font=header_font, anchor="lm")
    
    # Service provider card
    provider_y = 250
    draw.rectangle([100, provider_y, width-100, provider_y + 200], fill=WHITE, outline=BRAND_GRAY)
    
    # Provider photo placeholder
    draw.ellipse([150, provider_y + 30, 250, provider_y + 130], fill=BRAND_GREEN)
    draw.text((200, provider_y + 80), "👤", fill=WHITE, font=header_font, anchor="mm")
    
    # Provider details
    draw.text((300, provider_y + 50), "Sarah's Cleaning Service", fill=BRAND_DARK, font=header_font)
    draw.text((300, provider_y + 100), "⭐ 4.9 (127 reviews)", fill=BRAND_ORANGE, font=body_font)
    draw.text((300, provider_y + 140), "✓ Verified • 2.3 km away", fill=BRAND_GREEN, font=body_font)
    
    # Service options
    options_y = 500
    draw.text((100, options_y), "Select Service", fill=BRAND_DARK, font=header_font)
    
    options = [
        ("Basic Cleaning", "₵80", "2-3 hours • Living room, kitchen, bathroom"),
        ("Deep Cleaning", "₵150", "4-5 hours • Full house deep clean"),
        ("Move-in/out Clean", "₵200", "5-6 hours • Complete move-in preparation")
    ]
    
    for i, (service, price, desc) in enumerate(options):
        option_y = options_y + 80 + i * 120
        
        # Radio button
        draw.ellipse([120, option_y + 10, 150, option_y + 40], outline=BRAND_GREEN, width=3)
        if i == 1:  # Selected option
            draw.ellipse([125, option_y + 15, 145, option_y + 35], fill=BRAND_GREEN)
        
        # Service details
        draw.text((180, option_y), service, fill=BRAND_DARK, font=body_font)
        draw.text((180, option_y + 40), desc, fill=BRAND_GRAY, font=small_font)
        draw.text((width - 150, option_y + 20), price, fill=BRAND_GREEN, font=header_font, anchor="rm")
    
    # Date and time selection
    datetime_y = 920
    draw.text((100, datetime_y), "Select Date & Time", fill=BRAND_DARK, font=header_font)
    
    draw.rectangle([100, datetime_y + 60, width//2 - 50, datetime_y + 120], fill=BACKGROUND_LIGHT, outline=BRAND_GRAY)
    draw.text((100 + (width//2 - 150)//2, datetime_y + 90), "📅 Tomorrow, Mar 15", fill=BRAND_DARK, font=body_font, anchor="mm")
    
    draw.rectangle([width//2 + 50, datetime_y + 60, width - 100, datetime_y + 120], fill=BACKGROUND_LIGHT, outline=BRAND_GRAY)
    draw.text((width//2 + 50 + (width//2 - 150)//2, datetime_y + 90), "🕐 10:00 AM", fill=BRAND_DARK, font=body_font, anchor="mm")
    
    # Book button
    book_y = height - 300
    draw.rectangle([100, book_y, width - 100, book_y + 100], fill=BRAND_GREEN)
    draw.text((width//2, book_y + 50), "Book Service - ₵150", fill=WHITE, font=header_font, anchor="mm")

def create_profile_screen(draw, width, height, title_font, header_font, body_font, small_font):
    """Create the user profile screen"""
    
    # Header
    draw.rectangle([0, 0, width, 300], fill=BRAND_GREEN)
    
    # Profile photo
    draw.ellipse([width//2 - 80, 120, width//2 + 80, 280], fill=WHITE)
    draw.text((width//2, 200), "👤", fill=BRAND_GREEN, font=title_font, anchor="mm")
    
    # User info
    draw.text((width//2, 350), "John Doe", fill=BRAND_DARK, font=header_font, anchor="mm")
    draw.text((width//2, 400), "john.doe@email.com", fill=BRAND_GRAY, font=body_font, anchor="mm")
    draw.text((width//2, 440), "📍 East Legon, Accra", fill=BRAND_GRAY, font=body_font, anchor="mm")
    
    # Stats
    stats_y = 520
    stats = [("12", "Orders"), ("4.8", "Rating"), ("₵480", "Saved")]
    stat_width = (width - 200) // 3
    
    for i, (number, label) in enumerate(stats):
        x = 100 + i * stat_width
        draw.text((x + stat_width//2, stats_y), number, fill=BRAND_GREEN, font=header_font, anchor="mm")
        draw.text((x + stat_width//2, stats_y + 50), label, fill=BRAND_GRAY, font=body_font, anchor="mm")
    
    # Menu options
    menu_y = 650
    menu_items = [
        ("📋", "Order History"),
        ("❤️", "Favorite Services"),
        ("💳", "Payment Methods"),
        ("🏠", "Saved Addresses"),
        ("🔔", "Notifications"),
        ("⚙️", "Settings"),
        ("📞", "Support"),
        ("🚪", "Sign Out")
    ]
    
    for i, (icon, text) in enumerate(menu_items):
        item_y = menu_y + i * 80
        
        draw.rectangle([100, item_y, width - 100, item_y + 70], fill=WHITE, outline=BRAND_GRAY)
        draw.text((150, item_y + 35), icon, fill=BRAND_GREEN, font=body_font, anchor="lm")
        draw.text((220, item_y + 35), text, fill=BRAND_DARK, font=body_font, anchor="lm")
        draw.text((width - 150, item_y + 35), "→", fill=BRAND_GRAY, font=body_font, anchor="rm")

def main():
    """Generate all iPad screenshots"""
    
    # Create output directory
    output_dir = "/Users/enamegyir/Documents/Projects/homelinkgh-website-deploy/ipad_screenshots"
    os.makedirs(output_dir, exist_ok=True)
    
    screens = ["home", "services", "booking", "profile"]
    dimensions = [
        (IPAD_PRO_PORTRAIT, "ipad_pro_portrait"),
        (IPAD_12_9_PORTRAIT, "ipad_12_9_portrait")
    ]
    
    print("🎨 Creating iPad screenshots for HomeLinkGH...")
    
    for screen_type in screens:
        print(f"📱 Creating {screen_type} screen...")
        
        for (width, height), size_name in dimensions:
            img = create_ipad_screenshot(width, height, screen_type, f"{screen_type}_{size_name}")
            
            filename = f"{output_dir}/homelinkgh_{screen_type}_{size_name}_{width}x{height}.png"
            img.save(filename, "PNG", quality=95, optimize=True)
            print(f"✅ Saved: {filename}")
    
    print(f"\n🎉 All screenshots created successfully!")
    print(f"📁 Location: {output_dir}")
    print(f"📱 Generated {len(screens) * len(dimensions)} iPad screenshots")
    
    # Create a summary file
    summary_file = f"{output_dir}/README.md"
    with open(summary_file, 'w') as f:
        f.write("# HomeLinkGH iPad Screenshots for App Store\n\n")
        f.write("Professional iPad screenshots for App Store submission.\n\n")
        f.write("## Screenshots Generated\n\n")
        
        for screen_type in screens:
            f.write(f"### {screen_type.title()} Screen\n")
            for (width, height), size_name in dimensions:
                filename = f"homelinkgh_{screen_type}_{size_name}_{width}x{height}.png"
                f.write(f"- `{filename}` ({width}x{height}px)\n")
            f.write("\n")
        
        f.write("## App Features Showcased\n\n")
        f.write("- 🏠 **Home Screen**: Quick service access, recent orders, search functionality\n")
        f.write("- 🛍️ **Services Screen**: Complete service catalog with ratings and booking\n")
        f.write("- 📋 **Booking Screen**: Service provider selection, pricing, date/time booking\n")
        f.write("- 👤 **Profile Screen**: User management, order history, settings\n\n")
        f.write("## Technical Specifications\n\n")
        f.write("- **iPad Pro Portrait**: 2048x2732px\n")
        f.write("- **iPad 12.9\" Portrait**: 2064x2752px\n")
        f.write("- **Format**: PNG with 95% quality\n")
        f.write("- **Brand Colors**: Ghana flag colors with professional design\n")
    
    print(f"📋 Summary created: {summary_file}")

if __name__ == "__main__":
    main()