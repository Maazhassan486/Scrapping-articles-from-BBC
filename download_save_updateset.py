import os
import requests
import pandas as pd
from urllib.parse import urlparse

# Read the Excel file
df = pd.read_csv(r'C:\Users\maazg\PyCharmMiscProject\Data2.csv')


# Create a folder to save the images
image_folder = (r'C:\Users\maazg\PyCharmMiscProject\images2')
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Function to download and save the image
def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Extract the image name from the URL
            image_name = os.path.basename(urlparse(url).path)
            image_path = os.path.join(folder, image_name)
            # Save the image
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return image_path
        else:
            print(f"Failed to download image from {url}")
            return None
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        return None

# Loop through the 'images' column (adjust column name as per your file)
df['local_images'] = df['images'].apply(lambda x: download_image(x, image_folder) if isinstance(x, str) else None)

# Save the updated DataFrame with the local image paths
df.to_csv(r'C:\Users\maazg\PyCharmMiscProject\Updated_Data3.csv', index=False)
print("CSV file saved at C:\\Users\\maazg\\PyCharmMiscProject.")

