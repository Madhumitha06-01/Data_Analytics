import os
import cloudinary
import cloudinary.uploader
import pandas as pd
from datetime import datetime

# Configure Cloudinary with your credentials
cloudinary.config(
    cloud_name='disrluwwh',  # Replace with your Cloudinary cloud name
    api_key='838139876834731',  # Replace with your Cloudinary API key
    api_secret='VJS-1hD4HP7nlJRP-JzvV4oGpsY'  # Replace with your Cloudinary API secret
)

# Function to upload an image file
def upload_image(file_path):
    try:
        response = cloudinary.uploader.upload(file_path)
        print("Upload successful for:", file_path)
        print("Image URL:", response['secure_url'])  # Get the secure URL of the uploaded image
        return response['secure_url']
    except Exception as e:
        print("Error during upload of", file_path, ":", str(e))
        return None

# Function to upload all images from a specified folder in creation date order
def upload_images_from_folder(folder_path):
    image_urls = []
    
    # Retrieve image filenames and their creation time
    image_files = []
    
    for f in os.listdir(folder_path):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(folder_path, f)
            creation_time = os.path.getctime(file_path)  # Gets the creation time of the file
            image_files.append((f, creation_time))

    # Sort files by creation time
    image_files.sort(key=lambda x: x[1])  # Sort by creation time

    # Iterate through the sorted file list and upload each image
    for filename, _ in image_files:
        file_path = os.path.join(folder_path, filename)
        url = upload_image(file_path)
        if url:
            image_urls.append({'filename': filename, 'url': url})

    # Save the URLs to an Excel file
    if image_urls:  # Check if there are any URLs to save
        df = pd.DataFrame(image_urls)
        excel_path = os.path.join(folder_path, 'Url_images.xlsx')
        df.to_excel(excel_path, index=False)
        print(f"Image URLs saved to {excel_path}")
    else:
        print("No images were uploaded, so no Excel file was created.")

# Path to your folder containing images
folder_path = r'C:\selenium2\new_image'  # Replace with the path to your folder

# Call the upload function
upload_images_from_folder(folder_path)