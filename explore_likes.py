from selenium import webdriver
from selenium.webdriver.common.by import By

import argparse
import pyautogui
import time

def login_to_instagram(username, password):

    driver = webdriver.Edge() # or any other browser driver you prefer
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
    time.sleep(5)
    
    return driver

def explore_instagram_likes(driver, max_scroll_count = 5):

    driver.get("https://www.instagram.com/explore/")
    time.sleep(2)

    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = 0

    while scroll_count < max_scroll_count:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height
        scroll_count += 1

    image_elements = driver.find_elements(By.CSS_SELECTOR, "div div div img")
    image_elements = image_elements[2:]

    for image_element in image_elements:

        driver.execute_script("arguments[0].click();", image_element)
        time.sleep(0.5)

        pyautogui.click(clicks=2, button='left')
        time.sleep(0.5)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Instagram Image Liker")

    parser.add_argument("username", help="Your Instagram username")
    parser.add_argument("password", help="Your Instagram password")

    parser.add_argument("--count", type=int, default=1, help="Number of times to explore Instagram likes (default: 1)")

    args = parser.parse_args()

    # Login to Instagram
    driver = login_to_instagram(args.username, args.password)

    # Explore Instagram likes
    for _ in range(args.count):
        print("THIS IS THE COUNT NUMBER: ", _)
        explore_instagram_likes(driver)