from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pynput
from pynput.keyboard import Key, Controller
import os
import sys

keyboard = Controller()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))


sleep(2)
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)

def session_login():
        #  Faz o Login
        print("=============")
        print("=== LOGIN ===")
        print("=============")

        username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys('your_username')
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys('your_password')

        # Clica no botão de fazer login
        button_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button_login.click()
        sleep(3)



def search_page():
        #  Faz a busca na barra de pesquisa
        print("=============")
        print("=== BUSCA ===")
        print("=============")
        search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys('portalcontabeis')
        sleep(3)
        keyboard.press(Key.enter)
        sleep(2)
        keyboard.press(Key.enter)
        sleep(10)


        # Clica nos seguidores da página
        # following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        sleep(5)

def scroll_down_followers():
        print("==============")
        print("=== SCROLL ===")
        print("==============")
        #scroll down modal de seguidores
        l = 0
        while (l <= 10):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                l = l + 1

        sleep(1) 

        n = 0
        while(n <= 10):
                keyboard.press(Key.page_down) 
                keyboard.release(Key.page_down) 
                sleep(0.2)
                n = n+1
        sleep(1)

        l = 0
        while (l <=10):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                l = l + 1

        sleep(1)   
        n = 0
        while(n < 200):
                keyboard.press(Key.page_down) 
                keyboard.release(Key.page_down) 
                sleep(0.1)
                n = n+1


def follow(cont=20):
        print("==============")
        print("=== FOLLOW ===")
        print("==============")
        print("Seguir: " + str(cont))
        x = 1
        while (x <= cont):
                try:
                        timer = randint(10, 80)
                        sleep(timer)
                        follow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(x) + ']/div/div[2]/button')
                        follow.click()
        
                except:
                        sleep(4)
                        cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                        cancel.click()
                        x = x - 1
            
                print(x)
                x = x + 1


                        



def unfollow(cont=20): 
        print("================")
        print("=== UNFOLLOW ===")
        print("================")
        print("Deixar de seguir: " + str(cont))
        # Deixa de seguir todo mundo
        k = 1

        while (k < cont):
                try:
                        follow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(k) +']/div/div[2]/button')
                        follow.click()
                        k = k+1
                        timer = randint(1,50)

                        sleep(timer)
                        unfollow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                        unfollow.click()
                        sleep(3)
                        print(k)
                except:
                        follow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(k) +']/div/div[3]/button')
                        follow.click()
                        k = k+1
                        timer = randint(1,50)

                        sleep(timer)
                        unfollow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                        unfollow.click()
                        sleep(3)
                        print(k)
        print("Fim do segundo loop") 


#Faz o login
session_login()

#Busca a pagina
search_page()

#Percorre o modal de seguidores
scroll_down_followers()
#
while True:
        # Segue X pessoas
        follow()

        #Deixa de seguir X pessoas
        unfollow()

# unfollow()


