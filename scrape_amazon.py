from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def scrape_amazon(query):
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    search_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(3)

    products = []
    results = driver.find_elements(By.XPATH, "//div[contains(@data-component-type, 's-search-result')]")[:5]

    for item in results:
        try:
            title = item.find_element(By.TAG_NAME, "h2").text
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            image = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            description = title
            reviews = item.find_element(By.CLASS_NAME, "a-size-base").text
            products.append({
                "title": title,
                "link": link,
                "image": image,
                "description": description,
                "reviews": reviews,
                "source": "Amazon"
            })
        except Exception:
            continue

    driver.quit()
    return products

