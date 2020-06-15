# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:03:08 2020

@author: kingslayer
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random



class TinderBot:
    
    def __init__(self,driver):
        self.driver=driver
        self.auto=True
        self.base_window=self.driver.window_handles[0]
        
    def login_path_selector(self):
        li=[1,2]
        self.path=input("""How to you want to Login?
                        1.Google
                        2.Facebook
                        Type 1 or 2:\n""")
        try:
            self.path=int(self.path)
        except Exception:
            print("Please give a valid input...")
            self.path=input("""How to you want to Login?
                        1.Google
                        2.Facebook
                        Type 1 or 2:\n""")
            
            while int(self.path) not in li:
                print("Please give a valid input...")
                self.path=input("""How to you want to Login?
                            1.Google
                            2.Facebook
                            Type 1 or 2:\n""")
            else:
                self.path=int(self.path)
    
    def login_path_forward(self):
        try:
            x=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            x.click()
        except Exception:
            try:
                paths=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
                paths.click()
                
            except Exception:
                p=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
                p.click()
                paths=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
                paths.click()
            
    def login(self):
                try:
                    x=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
                    x.click()
                    self.login_path_forward()
                    
                except Exception:
                    pass
                if self.path==1:
                    login_path=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button')
                    login_path.click()
                    sleep(2)
                    from gmail import username,password
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    username_space=self.driver.find_element_by_xpath('//*[@id="identifierId"]')
                    username_space.send_keys(username)
                    next_=self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
                    next_.click()
                    sleep(2)
                    psw_space=self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                    psw_space.send_keys(password)
                    next_=self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
                    next_.click()
                    self.driver.switch_to_window(self.base_window)
                    sleep(10)
                    allow=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                    allow.click()
                    sleep(2)
                    notification=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
                    notification.click()
                    accept=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
                    accept.click()
                   
                    
                else:
                    login_path=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
                    login_path.click()
                    sleep(2)
                    from facebook import username,password
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    username_space=self.driver.find_element_by_xpath('//*[@id="email"]')
                    username_space.send_keys(username)
                    psw_space=self.driver.find_element_by_xpath('//*[@id="pass"]')
                    psw_space.send_keys(password)
                    next_=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
                    next_.click()
                    self.driver.switch_to_window(self.base_window)
                    sleep(10)
                    allow=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                    allow.click()
                    sleep(2)
                    notification=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
                    notification.click()  
                    accept=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
                    accept.click()
    

    def like(self):
        
        like=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
        sleep(2)
        
    
    def dislike(self):
        
        dislike=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()
        sleep(2)
        
    def removepopup1(self):
        
        popup=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
        popup.click()
        sleep(2)

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        sleep(2)
        
    def action_selection(self):
        choice=random.randint(0,1)
        if choice==0:
            self.dislike()
        else:
            self.like()
    
    def bot_at_work(self):
            sleep(3)
            try:
                self.action_selection()
                sleep(2)
            except Exception:
                try:
                    self.removepopup1()
                except Exception:
                    try:
                        self.close_math()
                    except Exception:
                        self.auto=False
    
    def close(self):
        self.driver.close()        
