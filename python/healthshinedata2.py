from pypdf import PdfReader  # Use 'type: ignore' if necessary

# Specify the path to your PDF file
file_path = r"C:\selenium2\Healthshine Catalogue.pdf"  # Use raw string

try:
    # Open the PDF file
    reader = PdfReader(file_path)
    
    print(f"Total pages: {len(reader.pages)}")
    
    # Loop through the pages to extract text and images
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        
        # Extract and print text
        text = page.extract_text()
        if text:
            print(f"Text from page {i + 1}:\n{text}\n")
        else:
            print(f"No text found on page {i + 1}.\n")

        # Extract images
        images = page.images
        for img_index, image in enumerate(images):
            # Save each image
            img_data = image.data
            img_name = f"image_page_{i + 1}_{img_index + 1}.png"  # Create a unique name
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f"Saved image: {img_name}")

except FileNotFoundError:
    print(f"The file {file_path} was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

