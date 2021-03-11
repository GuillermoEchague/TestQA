import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import time

class RegisterNewUserError(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\guill\Desktop\selenium\Driver\chromedriver.exe')
        driver = cls.driver
        driver.get('https://routing-test-qa.herokuapp.com/login')
        driver.maximize_window()


    def test_new_user(self):
        driver = self.driver
        title = "ImagenSignUpError"
        self.driver.get_screenshot_as_file(f"./{title}.png")
        create_account_button=driver.find_element_by_xpath('/html/body/nav/div/ul/li/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        driver.implicitly_wait(5)
        

        email_address = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_password')
        confirm_password = driver.find_element_by_id('user_password_confirmation')
        sign_up_button = driver.find_element_by_xpath('/html/body/main/div/form/div[4]/input')

        #email_address.clear()
        #password.clear()
        #confirm_password.clear()


        self.assertTrue(email_address.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and sign_up_button.is_enabled())   
            
        email_address.send_keys('Prueba1@gmail.com') 
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        title2 = "ImagenSignUpError2"
        self.driver.get_screenshot_as_file(f"./{title2}.png")
        sign_up_button.click()
        title3 = "ImagenSignUpError3"
        self.driver.get_screenshot_as_file(f"./{title3}.png")
        
        #driver.get_screenshot_as_file(f"./{"title1"}.png")

        #email_address.clear()
        email_address.send_keys('Prueba02@gmail.com') 
        password.send_keys('Test')
        confirm_password.send_keys('Test')

        title4 = "ImagenSignUpError4"
        self.driver.get_screenshot_as_file(f"./{title4}.png")
        sign_up_button.click()
        title5 = "ImagenSignUpError5"
        self.driver.get_screenshot_as_file(f"./{title5}.png")
        
        




    




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #return super().tearDown() 

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'test-sign-up-report'))       