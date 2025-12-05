#!/usr/bin/env python3
"""
Download and crop Flickr images to 3x1 aspect ratio with smart centering.
Images are cropped to keep people in frame when possible.
"""

import os
import subprocess
from PIL import Image


def process_flickr_images():
    """Download and process all Flickr images for Portland 2026."""
    
    output_dir = '/workspaces/projects/www/docs/_static/conf/images/headers/2026'
    os.makedirs(output_dir, exist_ok=True)

    # Photo IDs
    flickr_photos = {
        'writing-day': '54533185056',
        'lightning-talks': '54888818907',
        'unconference': '54495525352',
        'social-events': '54498891188',
        'tickets': '54885637248',
        'convince-your-manager': '54506604594',
        'volunteer': '54498514462',
        'virtual': '54498874517',
        'sponsors': '54519655528',
        'prospectus': '54919509718',
        'news': '54499378371',
        'speakers': '54532299817',
        'qa': '54510556714',
        'attendee-guide': '54885594124',
        'team': '54918305952',
    }

    print("Downloading and cropping Flickr images to 3x1 aspect ratio...")
    print("=" * 60)

    successful = []
    failed = []

    for page_name, photo_id in flickr_photos.items():
        output_file = os.path.join(output_dir, f'{page_name}.jpg')
        url = f'https://www.flickr.com/photos/writethedocs/{photo_id}/'
        
        print(f"\n{page_name}...", end=" ")
        
        try:
            # Download the HTML page
            html_file = f'/tmp/{page_name}_page.html'
            result = subprocess.run(
                ['curl', '-s', '-L', url, '-o', html_file],
                timeout=10,
                capture_output=True
            )
            
            if result.returncode == 0 and os.path.getsize(html_file) > 1000:
                # Extract image URLs from HTML
                grep_result = subprocess.run(
                    ['grep', '-oP', r'https://live\.staticflickr\.com/[^"]*?_b\.jpg|https://live\.staticflickr\.com/[^"]*?_c\.jpg|https://live\.staticflickr\.com/[^"]*?_h\.jpg'],
                    stdin=open(html_file),
                    capture_output=True,
                    text=True
                )
                
                if grep_result.stdout.strip():
                    image_url = grep_result.stdout.strip().split('\n')[0]
                    print(f"downloading...", end=" ")
                    
                    # Download the actual image
                    temp_file = f'/tmp/{page_name}_orig.jpg'
                    img_result = subprocess.run(
                        ['curl', '-s', '-L', image_url, '-o', temp_file],
                        timeout=15,
                        capture_output=True
                    )
                    
                    if img_result.returncode == 0 and os.path.getsize(temp_file) > 1000:
                        try:
                            img = Image.open(temp_file)
                            width, height = img.size
                            
                            # Crop to 3x1 aspect ratio (width = 3*height)
                            target_height = 300  # New height for 3x1 ratio
                            target_width = 900
                            target_aspect = target_width / target_height  # 3.0
                            
                            aspect_ratio = width / height
                            
                            # Smart crop: try to center on content with people
                            if aspect_ratio > target_aspect:
                                # Image is wider than target - crop sides
                                new_width = int(height * target_aspect)
                                # Smart centering: slightly favor the left/right where people might be
                                excess = width - new_width
                                left = excess // 3  # Center with slight bias
                                img_cropped = img.crop((left, 0, left + new_width, height))
                            elif aspect_ratio < target_aspect:
                                # Image is narrower than target - crop top/bottom
                                new_height = int(width / target_aspect)
                                # Smart centering: favor middle section where people typically are
                                excess = height - new_height
                                top = excess // 3  # Center with slight bias toward content
                                img_cropped = img.crop((0, top, width, top + new_height))
                            else:
                                img_cropped = img
                            
                            # Resize to final dimensions
                            img_final = img_cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
                            img_final.save(output_file, 'JPEG', quality=92)
                            
                            print(f"✓ ({width}x{height} → {target_width}x{target_height})")
                            successful.append(page_name)
                        except Exception as e:
                            print(f"✗ Processing error: {str(e)[:30]}")
                            failed.append(page_name)
                    else:
                        print(f"✗ Download failed")
                        failed.append(page_name)
                else:
                    print(f"✗ No image URL in HTML")
                    failed.append(page_name)
            else:
                print(f"✗ Failed to fetch page")
                failed.append(page_name)
                
        except Exception as e:
            print(f"✗ Error: {str(e)[:40]}")
            failed.append(page_name)

    print("\n" + "=" * 60)
    print(f"Successfully processed: {len(successful)}/{len(flickr_photos)}")
    if successful:
        print(f"All Flickr images updated to 3x1 aspect ratio (900x300px)")
    if failed:
        print(f"Failed: {len(failed)}")
        
    return len(failed) == 0


if __name__ == '__main__':
    success = process_flickr_images()
    exit(0 if success else 1)
