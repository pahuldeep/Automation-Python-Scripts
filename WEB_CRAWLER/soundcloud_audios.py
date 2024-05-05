from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def soundcloud(playlist_url):
    
    driver = webdriver.Edge()
    driver.get(playlist_url)

    # Scroll down the page to load all playlist items
    scrolls = 5
    for _ in range(scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

    # Find all the playlist item elements on the page
    playlist_items = driver.find_elements(By.CSS_SELECTOR, '.trackItem__content')

    # Loop through each playlist item and extract
    song_links = {}
    for item in playlist_items:    
        anchor_tag = item.find_element(By.CSS_SELECTOR, ".trackItem__trackTitle")

        # Extract the attribute
        song_title = anchor_tag.text
        song_link = anchor_tag.get_attribute('href')
        print(f'Title: {song_title} - Link: {song_link}')

        song_links[song_title] = song_link

    return song_links

