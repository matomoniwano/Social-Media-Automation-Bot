from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

f = open("credential.txt", "r")
credential = []
for x in f:
  print(x)
  credential.append(x)


webdriver = webdriver.Chrome(ChromeDriverManager().install())
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

#credentials
username = webdriver.find_element("name", "username")
username.send_keys(credential[0])
password = webdriver.find_element("name", "password")
password.send_keys(credential[1])

sleep(5)

button_login = webdriver.find_element("css selector",'#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(5)


# notnow = webdriver.find_element("css selector",'body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['kpop', 'anime', 'texas', 'animegirl', 'weeb']

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0
follow_count = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element("xpath","//div[@class='_aagw']")
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    username = webdriver.find_element("xpath",'//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _acan _acao _acat _acaw _a6hd"]')
    username.click()
    sleep(5)
    follower = webdriver.find_element("xpath", '//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd"]') 
    follower.click()
    sleep(5)

    followers = webdriver.find_elements("xpath", '//div[@class="_aacl _aaco _aacw _adda _aad6 _aade"]')
    print(len(followers))
    sleep(5)

    for i in range(1, len(followers)):
        followers[i].click()
        follow_count = follow_count + 1
        sleep(randint(2,14))

print("You followed", follow_count)
