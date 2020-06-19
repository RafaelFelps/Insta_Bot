from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()

chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)


#  Faz o Login
username = webdriver.find_element_by_name('username')
username.send_keys('rafaelfelps62')
password = webdriver.find_element_by_name('password')
password.send_keys('R@sfaeu123')

# Clica no botão de fazer login
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button') 
button_login.click()
sleep(3)




#  Faz a busca na barra de pesquisa
search_bar = webdriver.find_element_by_css_selector('#react-root > section > nav > div:nth-child(2) > div > div > div:nth-child(2) > input')
search_bar.send_keys('popugramsg')
sleep(2)
keyboard.press(Key.enter)
sleep(1)
keyboard.press(Key.enter)
sleep(3)

# Clica nos seguidores da página
following = webdriver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a[href*='/popugramsg/following/']")
following.click()
sleep(5)


#scroll down modal de seguidores
l = 0
while (l < 4):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        l = l + 1

sleep(2) 

n = 0
while(n <= 5):
        keyboard.press(Key.down) 
        keyboard.release(Key.down) 
        sleep(0.2)
        n = n+1
sleep(1)

l = 0
while (l < 4):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        l = l + 1

sleep(1)   
n = 0
while(n < 400):
        keyboard.press(Key.down) 
        keyboard.release(Key.down) 
        sleep(0.1)
        n = n+1

while True:
        # Loop que segue todos os seguidores da página
        j = 1
        while (j < 170):
                follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(j) +']/div/div[2]/button')
                follow.click()
                j = j+1
                sleep(30)
        print("Fim do primeiro loop")
        sleep(5)

        # Deixa de seguir todo mundo
        k = 1
        while (k < 170):
                follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(k) +']/div/div[2]/button')
                follow.click()
                k = k+1
                sleep(30)
                unfollow = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                unfollow.click()
                sleep(0.3)
        print("Fim do segundo loop") 




