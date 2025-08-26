#!/usr/bin/env python3
import base64
import sys
import os

def image_to_base64(image_path):
    """Convert image to base64 string"""
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def update_html(html_path, maxime_base64, charlotte_base64):
    """Update HTML file with base64 images"""
    with open(html_path, 'r') as file:
        content = file.read()
    
    # Replace placeholders with actual base64 data
    content = content.replace('MAXIME_BASE64_HIER_EINFÜGEN', maxime_base64)
    content = content.replace('CHARLOTTE_BASE64_HIER_EINFÜGEN', charlotte_base64)
    
    with open(html_path, 'w') as file:
        file.write(content)
    
    print("✅ Images successfully added to HTML file!")

if __name__ == "__main__":
    # Paths
    html_file = "eltern_flyer.html"
    maxime_image = "IMG_20250817_180913_447.jpg"  # Maxime's image
    charlotte_image = "2025-07-02 15.02.29 projekte.zameit.com 5b277a260737.png"  # Charlotte's image
    
    # Check if files exist
    if not os.path.exists(maxime_image):
        print(f"❌ Error: {maxime_image} not found")
        sys.exit(1)
    if not os.path.exists(charlotte_image):
        print(f"❌ Error: {charlotte_image} not found")
        sys.exit(1)
    if not os.path.exists(html_file):
        print(f"❌ Error: {html_file} not found")
        sys.exit(1)
    
    # Convert images to base64
    print("Converting images to base64...")
    maxime_base64 = image_to_base64(maxime_image)
    charlotte_base64 = image_to_base64(charlotte_image)
    
    # Update HTML
    print("Updating HTML file...")
    update_html(html_file, maxime_base64, charlotte_base64)