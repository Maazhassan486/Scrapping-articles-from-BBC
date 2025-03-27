from PIL import Image
import os
import pandas as pd

# Paths
image_folder = r"C:\Users\maazg\PyCharmMiscProject\images2"
csv_path = r"C:\Users\maazg\PyCharmMiscProject\Updated_Data3.csv"

# Load dataset
df = pd.read_csv(csv_path)

# Process each image
for index, row in df.iterrows():
    local_image_path = row['local_images']

    if os.path.exists(local_image_path):
        try:
            # Open image
            img = Image.open(local_image_path)

            # Resize image to 224x224
            img = img.resize((224, 224))

            # Convert to RGB if necessary (e.g., for .webp)
            img = img.convert("RGB")

            # Generate new file path with .jpg extension
            new_image_path = local_image_path.replace(".webp", ".jpg")

            # Save the processed image as .jpg
            img.save(new_image_path, "JPEG")
            img.save(r'C:\Users\maazg\PyCharmMiscProject\images3', "JPEG")

            # Update the dataset with the new path
            df.at[index, 'local_images'] = new_image_path

        except Exception as e:
            print(f"Error processing {local_image_path}: {e}")

# Save the updated dataset
updated_csv_path = r"C:\Users\maazg\PyCharmMiscProject\updated_data44.csv"
df.to_csv(updated_csv_path, index=False)

print(f"Image preprocessing completed. Updated dataset saved to {updated_csv_path}.")
