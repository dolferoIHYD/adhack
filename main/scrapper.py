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

    def get_picture(self, quwery):
        self.driver.get('https://www.google.ru/search?q={}&newwindow=1&rlz=1C1CHWL_ruRU751RU752&tbs=isz:l,itp:photo,sur:fmc&tbm=isch&source=lnt&sa=X&ved=0ahUKEwjfq-28ivbVAhUqS5oKHdpGCfoQpwUIHQ&biw=1242&bih=636&dpr=1.1'.format(quwery))
        try:
            time.sleep(2)
            gimage = self.driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a/img').click()
        except:
            print ('fuck it')

        try:
            time.sleep(5)
            button = self.driver.find_element_by_xpath('//*[@id="irc_cc"]/div[2]/div[3]/div[1]/div/div[2]/table[1]/tbody/tr/td[2]/a')
            lnk =   button.get_attribute('href')
            print(lnk)
        except:
            print("except")
        return lnk

    def create_card(self, company):
        self.driver.get('http://www.lemonprint.ru/vizitki/edit.aspx?template_id=Man03')
        close = self.driver.find_element_by_xpath('//*[@id="CityPopContent"]/span').click()
        input_name = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[1]/textarea')
        input_name.send_keys('')
        time.sleep(0.2)
        input_name.send_keys('Pavel')
        input_surname = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[2]/textarea')
        input_surname.send_keys('Technique')
        input_company = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[3]/textarea')
        input_company.send_keys(company)
        input_adress = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[4]/textarea')
        input_adress.send_keys('Lefortovo')
        input_adress_empty =self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[5]/textarea')
        input_adress_empty.send_keys('')
        input_phone = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[6]/textarea')
        input_phone.send_keys('+79999999999')
        input_email = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[7]/textarea')
        input_email.send_keys('xanax@cunteinyr.com')
        input_site = self.driver.find_element_by_xpath('//*[@id="TextInputArea"]/li[8]/textarea')
        input_site.send_keys('www.rap.com')
        btn_next = self.driver.find_element_by_xpath('//*[@id="btnSave"]')
        btn_next.send_keys(Keys.ENTER)
        time.sleep(4)
        card = self.driver.find_element_by_xpath('//*[@id="DocumentView"]/a[2]/img')
        link = card.get_attribute('src')
        return link
