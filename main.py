# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:26:42 2020

@author: kingslayer
"""

from selenium import webdriver
from tinder_bot import TinderBot
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.tinder.com")
sleep(2)

bot=TinderBot(driver)       
bot.login_path_selector()
bot.login_path_forward()
sleep(7)
bot.login()
while bot.auto==True:
    bot.bot_at_work()
else:
    bot.close()