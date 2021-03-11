import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class LogOutUser(unittest.TestCase):

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
        title0 = "ImagenLogOut0"
        self.driver.get_screenshot_as_file(f"./{title0}.png")

        email_address.send_keys('prueba4@gmail.com') 
        password.send_keys('1234')
        title4 = "ImagenLogOut1"
        self.driver.get_screenshot_as_file(f"./{title4}.png")
        log_in_button.click()
        title5 = "ImagenLogOut2"
        self.driver.get_screenshot_as_file(f"./{title5}.png")
    
        Log_out_link = driver.find_element_by_xpath('/html/body/nav/div/ul[2]/li[2]/a')
        Log_out_link.click()
        title6 = "ImagenLogOut3"
        self.driver.get_screenshot_as_file(f"./{title6}.png")                
        


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #return super().tearDown() 

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'test-Log-out-report'))       