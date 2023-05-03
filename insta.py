from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


id_insta = "..."
mdp = "..."


class instabot:
	def __init__(self, choice):						#choice option
		if choice == "1":
			hashtag = input("Which hashtag ? : ")
			self.login(id_insta, mdp)
			self.like_photo(hashtag)
		elif choice == "2":
			guy = input("Which account ? : ")
			self.login(id_insta, mdp)
			self.follow(guy)
		elif choice == "3":
			self.login(id_insta, mdp)
			self.unfollow(id_insta)
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


	def like_photo(self, hashtag):					#like photos
		nb_like = 2000
		x = 1
		driver = self.driver
		driver.get("https://instagram.com/explore/tags/" + hashtag + "/")										#load instagram with hashtag
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

	def follow(self, guy):							#follow followers
		x = 1
		driver = self.driver
		driver.get("https://instagram.com/" + guy + "/")														#load page guy
		sleep(2)
		driver.find_element_by_xpath('//a[@class="-nal3 "]').click()											#click on followers
		sleep(6)
		popup = self.driver.find_element_by_xpath('//div[@class="isgrP"]')   									#popup with all followers
		sleep(2)
		for i in range(1, 10):
			self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', popup)			#scroll down in popup
			sleep(2)
		for div in driver.find_elements_by_xpath('//*[@class="Pkbci"]'):
			div.click()
			print("follow :", x)
			x += 1
			sleep(10)
	

	def unfollow(self,guy2):						#unfollow
		x = 1
		z = 1
		driver = self.driver
		while True:
			driver.get("https://instagram.com/" + id_insta + "/")
			sleep(3)
			driver.find_element_by_xpath('//a[@href="/' + id_insta + '/following/"]').click()
			sleep(3)
			popup = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
			for i in range(1, 15):
				self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', popup)		#scroll down in popup
				sleep(2)
			for div in driver.find_elements_by_xpath('//*[@class="Pkbci"]'):
				div.click()
				a = random.randint(4, 7)
				print("sleep", a)
				sleep(a)
				self.driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()					#agree unfollow
				print(x, "unfollows")
				x += 1
				y = random.randint(300, 500)
				print("sleep", y)
				sleep(y)
				if x == z * 9:
					z += 1
					print("z =", z, "break")
					sleep(5)
					break



#choice like or follow or unfollow
choix = input("What do you want to do ? :\n1) Like photo\n2) Follow followers\n3) Unfollow\n1 or 2 or 3 ? : ")
instabot(choix)
