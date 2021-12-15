# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)/chromedriver.exe"  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")  # Otvorite website koriscenjem web drajvera
print(driver.title)
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)  # vratiti ime kljuceva

# print("\ntype is: {}\n".format(driver.page_source))
# print(driver.page_source)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))  # Trazimo naslove preko main id-a i ceakamo dok se stranica ne ucita pre toga
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
    # print(main.text)
finally:
    driver.quit()

# main = driver.find_element_by_id("main")  # Trazime element preko id-a(id je u nasem slucaju "main")


