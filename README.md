BBC Articles Scraping and Image Processing Project
This project demonstrates how to scrape articles from BBC, download related images, update datasets with image locations, and preprocess those images for model training. It consists of several scripts that work in sequence to generate and update datasets and image files.

Project Overview
Scraping Articles (scrapping.py):

This script scrapes 1000 articles from BBC.

It collects article metadata (e.g., title, URL, publication date) and saves the data into Data.csv.

Downloading Article Images & Updating Dataset (download_save_updateset.py):

This script reads Data.csv to extract article links.

It downloads the corresponding article images and saves them to a specified location on your PC.

It updates the dataset to include the local file paths for the images and outputs a new dataset named updateddata_44.csv.

Resizing Images (resize.py):

This script takes the downloaded images and resizes them to a standard size.

The resized images are then ready for model training.

File Descriptions
scrapping.py
Scrapes BBC articles and generates Data.csv with the collected metadata.

Data.csv
Contains metadata for the scraped articles (e.g., title, URL, publication date).

download_save_updateset.py
Downloads article images based on links in Data.csv, saves them locally, and updates the dataset with the image file locations. The updated dataset is saved as updateddata_44.csv.

updateddata_44.csv
The dataset updated with local image paths after downloading the images.

resize.py
Resizes all downloaded images to a standard format suitable for model training.

Prerequisites
Python 3.x installed

Required Python libraries (install via pip):

requests

beautifulsoup4

pandas

Pillow (for image processing)

A stable internet connection for scraping and downloading images

Setup & Usage
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Maazhassan486/programming-fundamentals.git
cd programming-fundamentals
Scrape Articles:

Run the scrapping.py script to scrape articles from BBC:

bash
Copy
Edit
python scrapping.py
This will generate a Data.csv file in your project folder.

Download Images & Update Dataset:

Run the download_save_updateset.py script to download article images and update the dataset:

bash
Copy
Edit
python download_save_updateset.py
After execution, check for the new dataset file updateddata_44.csv which now includes local image paths.

Resize Images:

Run the resize.py script to resize the downloaded images to the required dimensions for model training:

bash
Copy
Edit
python resize.py
The resized images will be saved to the designated folder specified in the script.

Notes
Customization:
You may need to adjust file paths and parameters (such as image dimensions) in the scripts based on your local environment and requirements.

Error Handling:
Ensure your internet connection is stable when running the scraping and downloading scripts. If any errors occur, check the logs printed to the console for troubleshooting.

Ethical Considerations:
This project is for educational purposes. When scraping websites, ensure you comply with the site's terms of use and avoid overwhelming their servers.

Contributing
Contributions to improve the scripts or add additional functionality are welcome! Feel free to fork the repository and submit a pull request.

License
This project is provided for educational purposes. Please review the license file for more details.
