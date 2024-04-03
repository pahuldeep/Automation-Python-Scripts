from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def youtube(playlist_url):

    driver = webdriver.Edge()
    # driver.get('https://www.youtube.com/')
    driver.get(playlist_url)

    scrolls = 5
    for _ in range(scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

    # Find all the video elements on the page
    video_elements = driver.find_elements(By.CSS_SELECTOR, 'ytd-playlist-video-renderer')

    data = {}
    # Loop through each video element and extract the duration
    for video_element in video_elements:
        video_title = video_element.find_element(By.CSS_SELECTOR, 'h3').text
        video_duration = video_element.find_element(By.CSS_SELECTOR, 'ytd-thumbnail-overlay-time-status-renderer').text
        print(f'Title: {video_title} - Duration: {video_duration}')
        
        data[video_title] = video_duration

    return data

# playlist_url = 'https://www.youtube.com/playlist?list=PLsHvWYTWngjUE2sLC8qzEdS8aS1qmgJxR'
# result = youtube(playlist_url)
