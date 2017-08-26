from selenium import webdriver

class Parser:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_name(self, keywords=None):
        if keywords:
            name = ''
        else:
            self.driver.get('https://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=yes')
            name = self.driver.find_element_by_class_name('plain').text
        return name
