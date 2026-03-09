from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import requests
import os


def get_articles():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    wait = WebDriverWait(driver, 10)

    driver.get("https://elpais.com/opinion/")

    # Accept cookies
    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]"))
        )
        cookie_button.click()
    except:
        pass

    # Wait for article titles
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2 a")))

    article_elements = driver.find_elements(By.CSS_SELECTOR, "h2 a")

    links = []

    for element in article_elements:
        link = element.get_attribute("href")

        if link and "elpais.com" in link:
            links.append(link)

        if len(links) == 5:
            break

    titles = []

    for i, link in enumerate(links):

        driver.get(link)

        try:
            title = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            ).text.strip()
        except:
            title = "No title found"

        print("\nSpanish Title:", title)

        try:

            paragraphs = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article p"))
            )

            content_list = []

            for p in paragraphs:
                try:
                    text = p.text.strip()
                    if text:
                        content_list.append(text)
                except:
                    continue

            content = " ".join(content_list)

        except:
            content = "Content not available for this article"

        print("\nSpanish Content:", content[:500])

        # Download image
        try:

            img = driver.find_element(By.CSS_SELECTOR, "figure img")
            img_url = img.get_attribute("src")

            if not os.path.exists("images"):
                os.makedirs("images")

            img_data = requests.get(img_url).content

            with open(f"images/article_{i}.jpg", "wb") as f:
                f.write(img_data)

            print("Image downloaded")

        except:
            print("No image found")

        titles.append(title)

    driver.quit()

    return titles