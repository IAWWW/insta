import random, os, shutil
from time import sleep
from instabot import Bot

bot = Bot()
bot.login(username="...", password="...")



path_photo = "/Users/iar/Pictures/insta/europe"
path_photo_done = "/Users/iar/Pictures/insta/europe/fait"

#choose random pic
random_photo = random.choice([
	x for x in os.listdir(path_photo)
	if os.path.isfile(os.path.join(path_photo, x))
])
random_photo = path_photo+"/"+random_photo

#choose random caption
list_captions = [
	"Better than my wildest dreams.", 
	"If sky is the limit, then go there.", 
	"This view is cheaper than therapy.",
	"Sometimes, all you need is a change in scenery.",
	"Perfect view.",
	"This view makes my heart beat faster.",
	"Where in the world do you call home?",
	"Where is your favorite place ?",
	"What’s the weather like where you are?",
	"What’s one thing on your mind today?",
	"Who do you admire and why?",
	"What motivates you the most?",
	"“How do I create something out of nothing?” -Amy Tan",
]
hashtag = "#beautifuldestinations #photographytime #travelmoments #viewpoints #photolifestyle #building #europe"

caption = random.choice(list_captions) + "\nFollow for more content !\n-----------------------\n\n\n\n\n\n\n\n-----------------------\n" + hashtag

bot.upload_photo(random_photo, caption = caption)


#move photo to fait
shutil.move(random_photo, path_photo_done)
