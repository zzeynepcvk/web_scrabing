from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'}) 
        
        # Tam dosya yolu 
        service = Service('/Users/zeynepcevik/Downloads/chromedriver-mac-arm64/chromedriver')
        self.browser = webdriver.Chrome(service=service, options=self.browserProfile)

        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(10)
        
        usernameInput = self.browser.find_element(By.CSS_SELECTOR, "input[name='text']")

        usernameInput.send_keys(self.username)  
        time.sleep(5)
        usernameInput.send_keys(Keys.ENTER)
        
        
        time.sleep(5)
        
        passwordInput = self.browser.find_element(By.NAME, "password")
        
        passwordInput.send_keys(self.password)
        
        time.sleep(5)
        
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(10)
        
        
        
    def search(self, hashtag):
        searchInput = self.browser.find_element(By.CLASS_NAME, "r-30o5oe")
        searchInput.send_keys(hashtag)
        time.sleep(5)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(5)
        
        results = []
        
        list = self.browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
        print("count : ",str(len(list)))
        
        for i in list:
            results.append(i.text)
        
        
        loopCounter = 0
        lastHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            newHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
            if newHeight == lastHeight:
                break
            lastHeight = newHeight
            loopCounter += 1
            
            list = self.browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
            print("count : ",str(len(list)))
            for i in list:
                results.append(i.text)
        
        list = self.browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
        print("count : ",str(len(list)))    
        
        count = 1
        with open("stajyer.txt", "w", encoding="utf-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count += 1
            
# Twitter botu başlat
twitter = Twitter(username, password)
twitter.signIn()
twitter.search("stajyer")