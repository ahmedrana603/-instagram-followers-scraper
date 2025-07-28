from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

wait = WebDriverWait(driver, 20)

driver.get("https://www.instagram.com/")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))).send_keys("Enter your Username")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))).send_keys("Enter your Password")
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_btn.click()
time.sleep(25)

profile_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//span[text()="Profile"]/ancestor::a[@role="link"]')
))
driver.execute_script("arguments[0].click();", profile_btn)
time.sleep(5)

time.sleep(5)  
time.sleep(10)

profile_image = wait.until(EC.presence_of_element_located((By.XPATH, '//img[contains(@alt, "profile picture")]')))
profile_image.find_element(By.XPATH, './ancestor::span').click()

time.sleep(10)

followers_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "follower")]')))
followers_link.click()

time.sleep(10)

usernames = driver.find_elements(By.XPATH, '//span[contains(@class, "_aaco") and @dir="auto"]')

time.sleep(10)
for user in usernames:
    print(user.text)
