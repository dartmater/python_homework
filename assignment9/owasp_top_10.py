from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")


links = []


top_10_h2 = driver.find_element(By.CSS_SELECTOR, '[id="top-10-web-application-security-risks"]')

if top_10_h2:
   
    ul_element = top_10_h2.find_element(By.XPATH, 'following-sibling::ul[1]')
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')

    for li in li_elements:
        try:
            a_tag = li.find_element(By.TAG_NAME, 'a')
            strong_tag = a_tag.find_element(By.TAG_NAME, 'strong')
            name = strong_tag.text.strip()
            url = a_tag.get_attribute("href")
            if name and url:
                print(f"{name}: {url}")
                links.append({"name": name, "url": url})
        except Exception as e:
            print(f"Error processing list item: {e}")

with open('owasp_top_10.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Link"])
    for link in links:
        writer.writerow([link["name"], link["url"]])


driver.quit()
