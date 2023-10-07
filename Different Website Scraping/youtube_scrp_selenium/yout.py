

from selenium import webdriver

url = 'https://www.youtube.com/c/HBAServices/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
driver.get(url)



videos = driver.find_elements("xpath", '//*[@id="dismissible"]')
for video in videos:
    title = video.find_element("xpath", './/*[@id="video-title"]').text.encode('utf8')
    views = video.find_element("xpath", './/*[@id="metadata-line"]/span[1]').text
    when = video.find_element("xpath", './/*[@id="metadata-line"]/span[2]').text
    print(title, views, when)






