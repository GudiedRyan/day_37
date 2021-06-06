from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\development\chromedriver.exe"
TWITTER_EMAIL = "yesmanvong@gmail.com"
TWITTER_PASS = os.environ["yesmantwitterpass"]


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element_by_class_name("start-text")
        start.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://twitter.com/login/")
        time.sleep(5)
        user = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(f"My Internet speed is {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up. ;-;")
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
        time.sleep(3)
        self.driver.quit()

speed_test = InternetSpeedTwitterBot()
speed_test.get_internet_speed()
speed_test.tweet_at_provider()