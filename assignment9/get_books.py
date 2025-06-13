from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep(2)

li_elements = driver.find_elements(By.CSS_SELECTOR, "li.cp-list-item")
print(f"Found {len(li_elements)} books")

results = []


li_class = "row cp-search-result-item" 
title_class = "cp-title"
author_class = "cp-author-link"   
format_div_class = "cp-format-info" 
format_span="display-info-primary"

items = driver.find_elements(By.CLASS_NAME, li_class)
print(f"Found {len(items)} search results")

for item in items:
    try:
        title = item.find_element(By.CLASS_NAME, title_class).text
        authors = item.find_elements(By.CLASS_NAME, author_class)
        author_names = '; '.join([a.text for a in authors])
        format_div = item.find_element(By.CLASS_NAME, format_div_class)
        format_year = format_div.find_element(By.CLASS_NAME, format_span).text

        book = {
            "Title": title,
            "Author": author_names,
            "Format-Year": format_year
        }
        results.append(book)

    except Exception as e:
        print("Error processing item:", e)

driver.quit()

# Task 4
df = pd.DataFrame(results)
print(df)

df.to_csv("assignment9/get_books.csv", index=False)

with open("assignment9/get_books.json", "w") as f:
    json.dump(results, f, indent=2)

    