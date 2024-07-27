from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
import time

# insta credentials
username = "username"
password = "password"
target_user = "target username"

chrome_driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.instagram.com/")
print(driver.title)


def human_typing(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


try:
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, "username"))
    )

    username_field = driver.find_element(By.NAME, "username")
    human_typing(username_field, username, delay=0.3)

    # Input password
    password_field = driver.find_element(By.NAME, "password")
    human_typing(password_field, password, delay=0.3)

    password_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 40).until(
        ec.presence_of_element_located((By.XPATH, "//*[@aria-label='Search']"))
    )

    search_svg = driver.find_element(By.XPATH, "//*[@aria-label='Search']")
    search_svg.click()
    time.sleep(1)

    search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search input']")
    human_typing(search_box, target_user, delay=0.3)
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/{target_user}/')]"))
    )
    driver.find_element(By.XPATH, f"//a[contains(@href, '/{target_user}/')]").click()

    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//div[contains(@class, '_aagw')]"))
    )
    first_post = driver.find_element(By.XPATH, "//div[contains(@class, '_aagw')]")
    first_post.click()

    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//div[@role='button' and contains(@class, 'x6s0dn4')]"))
    )

    # Ensure the element is visible and clickable
    like_button = driver.find_element(By.XPATH, "//div[@role='button' and contains(@class, 'x6s0dn4')]")
    driver.execute_script("arguments[0].scrollIntoView();", like_button)
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(@class, 'x6s0dn4')]")))

    driver.execute_script("arguments[0].click();", like_button)

    time.sleep(2)
    print("First post liked successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    time.sleep(5)
    driver.quit()
