# How to Locate Web Elements

"""
driver.find_element_by_id('id')
driver.find_element_by_name('name')
driver.find_element_by_xpath('xpath')
driver.find_element_by_css_selector('css')
driver.find_element_by_link_test('text')
 
OR

driver.find_element(By.ID,'id')
driver.find_element(By.NAME,'name')
driver.find_element(By.XPATH,'xpath')
driver.find_element(By.CSS,'css')
driver.find_element(By.LINK_TEXT,'text')

"""

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By


class GoogleClassDemo(unittest.TestCase):
	
	def setUp(self):
		
		global driver
		
		driver = webdriver.Chrome('C:\\Users\\SURYA\\Downloads\\installers\\chromedriver.exe')

		driver.get("https://www.google.com")

		driver.maximize_window()

	def test(self):
		driver.find_element_by_name('q').send_keys('Allu Arjun')
		time.sleep(5)
		driver.find_element_by_name('btnK').click()
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
		time.sleep(10)

	def tearDown(self):
		driver.quit()
		
		

unittest.main()
		


