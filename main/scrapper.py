from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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


    def get_logo(self, name, keyword):
        self.driver.get('https://www.logoshuffle.com/Logo#SelectedIcons=&Name={}&Slogan=&Keywords={}&IgnoreIcons=&SelectedIcons=&allSelectedText=Alle+ausgew%C3%A4hlt&fontFamilies%5B%5D=Serif&fontFamilies%5B%5D=SansSerif&fontFamilies%5B%5D=Handwriting&fontFamilies%5B%5D=Other&Color1=%23000010&Color2=%23757575&Color3=%23ABABAB&ColorBg=%23FFFFFF&ColorSchemeParams=1&ResetConstraints=True'.format(name, keyword))
        #while(image==0):
        try:
            time.sleep(15)
            image  = self.driver.find_element_by_id('ls-logo_0')
        except Exception as e:
            image = 0
            print(e)
        link = image.get_attribute('src')
       # return 'https://www.logoshuffle.com()'.format(link)
        return link