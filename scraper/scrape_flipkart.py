from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def scrape_flipkart(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    search_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(3)

    # Close login popup if it appears
    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
    except:
        pass

    products = []
    results = driver.find_elements(By.XPATH, "//div[contains(@class, '_1AtVbE')]//a")[:5]

    for item in results:
        try:
            title = item.find_element(By.CLASS_NAME, "_4rR01T").text if item.find_elements(By.CLASS_NAME, "_4rR01T") else item.text
            link = item.get_attribute("href")
            image = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            description = title
            reviews = "Reviews not available"
            products.append({
                "title": title,
                "link": link,
                "image": image,
                "description": description,
                "reviews": reviews,
                "source": "Flipkart"
            })
        except:
            continue

    driver.quit()
    return products
