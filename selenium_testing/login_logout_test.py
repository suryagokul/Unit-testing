from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class Check_Login_Logout(unittest.TestCase):

# Here setup and closing is same for all tests like login and logout.so we are using setup class method and teardown class method
	
	@classmethod
	def setUpClass(cls):
		
		global driver
		
		driver = webdriver.Chrome('C:\\Users\\SURYA\\Downloads\\installers\\chromedriver.exe')

		driver.get("http://www.seleniumbymahesh.com/")

		driver.maximize_window()

# checking login functionality of Sample Hospital Management System.

	def test_login(self):

		driver.find_element(By.LINK_TEXT,"HMS").click()         # to get text of link i.e <a href> we use LINK_TEXT.we are clicking that link for login
		
		time.sleep(5)

		driver.find_element_by_name('username').send_keys('admin')          # sending admin username

		time.sleep(5)

		driver.find_element_by_name('password').send_keys('admin')		# sending admin password

		time.sleep(5)

		driver.find_element_by_name('submit').click()                    # clicking submit button

		time.sleep(10)
	
	def test_logout(self):
		
		driver.find_element(By.LINK_TEXT,'Logout').click()                  # clicking logout link using LINK-TEXT

		time.sleep(10)
		
	@classmethod
	def tearDownClass(cls):
		driver.quit()
		

unittest.main()
		
