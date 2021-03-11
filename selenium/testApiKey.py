import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class CrearApiUser(unittest.TestCase):

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
        title0 = "ImagenApiKey0"
        self.driver.get_screenshot_as_file(f"./{title0}.png")    



        email_address.send_keys('prueba4@gmail.com') 
        password.send_keys('1234')
        title1 = "ImagenApiKey1"
        self.driver.get_screenshot_as_file(f"./{title1}.png")
        log_in_button.click()
        title2 = "ImagenApiKey2"
        self.driver.get_screenshot_as_file(f"./{title2}.png")


    def test_new_api(self):
        driver = self.driver
        api_keys_link=driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[2]/a')
        api_keys_link.click()
        title3 = "ImagenApiKey3"
        self.driver.get_screenshot_as_file(f"./{title3}.png")
        
        new_api_key_button = driver.find_element_by_xpath('/html/body/main/div/form/input[1]')
        new_api_key_button.click()
        title4 = "ImagenApiKey4"
        self.driver.get_screenshot_as_file(f"./{title4}.png")   

        
    
        destroy_button = driver.find_element_by_xpath('/html/body/main/div/table/tbody/tr/td[2]/a')
        destroy_button.click()                        

        alert = driver.switch_to_alert()
        alert_text = alert.text 

        self.assertEqual('Are you sure?', alert_text)
        alert.accept()
        title5 = "ImagenApiKey5"
        self.driver.get_screenshot_as_file(f"./{title5}.png")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #return super().tearDown() 

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'test-Api-Key-report'))       