from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#Using Headless Chrome
option.add_argument("--headless")
	
# Opening YouTube
browser = webdriver.Chrome('./chromedriver', options = option)
browser.get('https://www.youtube.com/')
#browser.find_element_by_link_text('Download')


#Wait 20 seconds for page to load 
timeout = 20

try:
	WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "search")))	
	
except TimeoutException:
	print("Timed out waiting for page to load")
	browser.quit()



searchBar = browser.find_element_by_id('search')
searchBar.send_keys('Travel Blogs')

searchBar.send_keys(Keys.ENTER)

elem = browser.find_element_by_link_text('FILTER')
elem.click()
elem = browser.find_element_by_link_text('Video')
elem.click()


# How to find the titles of various elements

titles_element = browser.find_elements_by_xpath("//a[@class='yt-simple-endpoint style-scope ytd-video-renderer']")


# Use list comprehension to get the actual repo titles and not the selenium
# objects.

titles = [x.text for x in titles_element]

# print out all the titles.

print('titles:')
print(titles, '\n')

print(len(titles))



#titles = browser.find_element_by_id('video-title')

#print(titles.text)
video_links = browser.find_elements_by_xpath("//a[@href]")


elem = browser.find_elements_by_xpath("//a[@class='yt-simple-endpoint style-scope ytd-video-renderer']	")

# My aim was to go to each video, then scrape the title description
# and the video id, and then return to the previous search page
# and then scrape the next video ,through a loop. I had to implement
# with selenium new page in youtube/ or page scrolling.

# Can Also use the requests package, didn't try that first, sadly.


for el in elem:
	browser.get(el.get_attribute("href"))
	#browser.find_element_by_link_text('SHOW MORE').click()
	print(browser.get(el.get_attribute("href")))


