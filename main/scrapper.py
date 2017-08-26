from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Parser:
    def __init__(self):
       # path = "C:\\Programm Files\\geckodriver.exe"
        self.driver = webdriver.Firefox()

    def get_name(self):
        self.driver.get('https://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=yes')
        name = self.driver.find_element_by_class_name('plain').text
        return name

    def get_slogan(self, keyword):
        self.driver.get('http://xn--90aihhxfgb.xn--p1ai/slogan/')
        textInput = self.driver.find_element_by_class_name('Slogan')
        textInput.send_keys(keyword)
        button = self.driver.find_element_by_xpath('//*[@id="bodyText"]/center[1]/p[3]/button')
        button.send_keys(Keys.ENTER)
        slogan = ''
        while(slogan==''):
            slogan = self.driver.find_element_by_id('slog').text
        return slogan
