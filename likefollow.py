from selenium import webdriver
from time import sleep
import random


id_insta = "..."
mdp = "..."




class instabot:
	def __init__(self):
		hashtag = input("Which hashtag ? : ")
		self.login(id_insta, mdp)
		self.like_photo(hashtag)
		return
		

	def login(self, username, pw):					#log in
		self.driver = webdriver.Chrome()																		#open Chrome
		self.driver.get("https://instagram.com")																#load instagram.com
		#sleep(2)
		#self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()							#click on Log in
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)					#insert username
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)							#insert password
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()									#click log in
		sleep(5)
		self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()									#click Not Now for notifications
		sleep(3)
		return


	def like_photo(self, hashtag):					#like & follow
		nb_like = 1500
		x = 1
		driver = self.driver
		driver.get("https://instagram.com/explore/tags/" + hashtag + "/")										#load instagram with hashtag
		sleep(3)
		driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()					# click on the first picture
		sleep(2)
		"""if len(driver.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]')):
			driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()							#see post
			print("clicked on See post")
		sleep(3)"""
		while x < nb_like:
			if len(driver.find_elements_by_xpath('//span[@class="fr66n"]')): 									#check if like present
				if random.randint(0, 100) < 80:
					driver.find_element_by_xpath('//span[@class="fr66n"]').click()								#click on like
					print('like')
				sleep(5)
				print(x, "likes")
			if len(driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]')):
				driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]').click()						#popup too many
				print("Too much likes, come back later (", x,"likes)")
			sleep(3)
			if random.randint(0, 100) < 50:
				if len(driver.find_elements_by_xpath('//button[@class="oW_lN sqdOP yWX7d    y3zKF     "]')):	#check if can follow
					driver.find_element_by_xpath('//button[@class="oW_lN sqdOP yWX7d    y3zKF     "]').click()	#follow											
					print('follow')
			sleep(5)
			driver.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()		#next picture
			sleep(2)
			x += 1

instabot()