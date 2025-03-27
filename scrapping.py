from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://www.bbc.com/")
    driver.implicitly_wait(10)

    # Open search bar
    search_button = driver.find_element(By.XPATH, '//button[@aria-label="Search BBC"]')
    search_button.click()

    # Enter search query
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[6]/div/div[1]/div/input')
    search_input.send_keys("crime")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)  # Allow search results to load

    # Initialize data dictionary
    data_dict = {"time_ago": [], "titles": [], "subtitles": [], "location": [], "images": [], "links": []}

    # Limit scraping to the first three pages
    max_pages = 2
    current_page = 1

    # Loop through pages
    while current_page <= max_pages:
        try:
            # Get the content of the current page
            tech_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/div')
            data = tech_element.get_attribute("outerHTML")
            soup = BeautifulSoup(data, "html.parser")

            # Extract data
            time_ago = [t.get_text().strip() for t in soup.find_all("span", attrs={'class': 'sc-4e537b1-1 dkFuVs'})]
            titles = [ti.get_text().strip() for ti in soup.find_all("h2")]
            subtitles = [s.get_text().strip() for s in soup.find_all("p")]
            location = [l.get_text().strip() for l in soup.find_all("span", attrs={'class': 'sc-4e537b1-2 eRsxHt'})]
            images = [img['src'] for img in soup.find_all("img", src=True) if 'placeholder' not in img['src']]
            links = ["https://www.bbc.com" + link['href'] for link in soup.find_all("a", href=True) if link['href'].startswith("/")]

            # Normalize lengths by filling shorter lists with empty strings
            max_len = max(len(time_ago), len(titles), len(subtitles), len(location), len(images), len(links))
            time_ago.extend([""] * (max_len - len(time_ago)))
            titles.extend([""] * (max_len - len(titles)))
            subtitles.extend([""] * (max_len - len(subtitles)))
            location.extend([""] * (max_len - len(location)))
            images.extend([""] * (max_len - len(images)))
            links.extend([""] * (max_len - len(links)))

            # Append data to dictionary
            data_dict["time_ago"].extend(time_ago)
            data_dict["titles"].extend(titles)
            data_dict["subtitles"].extend(subtitles)
            data_dict["location"].extend(location)
            data_dict["images"].extend(images)
            data_dict["links"].extend(links)

            # Increment the page counter
            current_page += 1

            # Check for "Next Page" button and click it if we haven't reached max_pages
            if current_page <= max_pages:
                next_page = driver.find_element(By.XPATH, '//button[@aria-label="Next Page"]')
                next_page.click()
                time.sleep(3)  # Allow next page to load
        except Exception as e:
            print(f"Error or no more pages: {e}")
            break

    # Save data to CSV
    df = pd.DataFrame(data_dict)
    df.to_csv("Data2.csv", index=False)
    print("Scraping completed. Data saved to Data2.csv.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
