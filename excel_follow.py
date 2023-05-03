from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


id_insta = "..."
mdp = "..."



class excel_insta:
	def __init__(self):						
		self.login(id_insta, mdp)
		self.account(id_insta)
		return
		

	def login(self, username, pw):					#log in
		self.driver = webdriver.Chrome()																		#open Chrome
		self.driver.get("https://instagram.com")																#load instagram.com
		sleep(5)
		#self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()							#click on Log in
		sleep(5)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)					#insert username
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)							#insert password
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()									#click log in
		sleep(30)
		self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()									#click Not Now for notifications
		sleep(5)
		return


	def account(self, id_insta):					
		driver = self.driver
		driver.get("https://instagram.com/" + id_insta)															#load instagram
		sleep(2)
		driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()								# click on the first picture
		sleep(3)
		while x < nb_like:
			if len(driver.find_elements_by_xpath('//span[@class="fr66n"]')): 									#check if like present
				driver.find_element_by_xpath('//span[@class="fr66n"]').click()									#click on like
				sleep(7)
				print(x, "likes")
			if len(driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]')):
				driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
				print("Too much likes, come back later (", x,"likes)")											#													
			sleep(5)
			driver.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()		#next picture
			sleep(2)
			x += 1

excel_insta()
