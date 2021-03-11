import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class CrearNewArticle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\guill\Desktop\selenium\Driver\chromedriver.exe')
        driver = cls.driver
        driver.get('https://routing-test-qa.herokuapp.com/login')
        driver.maximize_window()


    def test_login_user(self):
        driver = self.driver
        email_address = driver.find_element_by_id('email')
        password = driver.find_element_by_id('password')
        log_in_button = driver.find_element_by_name('button')

        self.assertTrue(email_address.is_enabled()
        and password.is_enabled())   
        email_address.clear()
        password.clear()
        title0 = "ImagenNewArticle0"
        self.driver.get_screenshot_as_file(f"./{title0}.png")  



        email_address.send_keys('prueba4@gmail.com') 
        password.send_keys('1234')
        title4 = "ImagenNewArticle2"
        self.driver.get_screenshot_as_file(f"./{title4}.png")
        log_in_button.click()
        title5 = "ImagenNewArticle3"
        self.driver.get_screenshot_as_file(f"./{title5}.png")


    def test_new_article(self):
        driver = self.driver
        new_article_button = driver.find_element_by_link_text('NEW ARTICLE')
        new_article_button.click()                
        title6 = "ImagenNewArticle4"
        self.driver.get_screenshot_as_file(f"./{title6}.png")
        time.sleep(1)
        new_title = driver.find_element_by_id('article_title')
        new_body = driver.find_element_by_id('article_body')
        self.assertTrue(new_title.is_enabled() and new_body.is_enabled())

        new_title.send_keys('Titulo prueba 1')
        new_body.send_keys('Lorem desum 1')
        title7 = "ImagenNewArticle5"
        self.driver.get_screenshot_as_file(f"./{title7}.png")
        driver.find_element_by_name('button').click()

        title8 = "ImagenNewArticle6"
        self.driver.get_screenshot_as_file(f"./{title8}.png")

        destroy_button = driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[2]/a[2]')
        destroy_button.click()                        

        alert = driver.switch_to_alert()
        alert_text = alert.text 

        self.assertEqual('Are you sure?', alert_text)
        alert.accept()
        title9 = "ImagenNewArticle7"
        self.driver.get_screenshot_as_file(f"./{title9}.png")

                         

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #return super().tearDown() 

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'test-Log-In-report'))       