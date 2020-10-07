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
webdriver.get('https://www.instagram.com/accounts/login/')
sleep(3)

def session_login():
        #  Faz o Login
        print("===============")
        print("=====LOGIN=====")
        print("===============")

        username = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys('rafaelfelps62')
        password = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys('R@sfaeu123')

        # Clica no botão de fazer login
        button_login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button_login.click()
        sleep(3)



def search_page():
        print("================")
        print("=====SEARCH=====")
        print("================")
        #  Faz a busca na barra de pesquisa
        search_bar = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys('contabilizei')
        sleep(2)
        keyboard.press(Key.enter)
        sleep(1)
        keyboard.press(Key.enter)
        sleep(3)


        # Clica nos seguidores da página
        following = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        following.click()
        sleep(5)

def scroll_down_followers():
        print("================")
        print("=====SCROLL=====")
        print("================")
        #scroll down modal de seguidores
        l = 0
        while (l <= 2):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                l = l + 1

        sleep(1) 

        n = 0
        while(n <= 2):
                keyboard.press(Key.page_down) 
                keyboard.release(Key.page_down) 
                sleep(0.2)
                n = n+1
        sleep(1)

        l = 0
        while (l <= 2):
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


def follow():
        print("================")
        print("=====FOLLOW=====")
        print("================")
        x = 1
        while (x <= 200):
                try:
                        timer = randint(10, 80)
                        sleep(timer)
                        follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(x) + ']/div/div[2]/button')
                        follow.click()
        
                except:
                        sleep(4)
                        cancel = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                        cancel.click()
                        x = x - 1
                print(str(x))
                x = x + 1


                        



def unfollow():
        print("==================")
        print("=====UNFOLLOW=====")
        print("==================")
        # Deixa de seguir todo mundo
        k = 1
        while (k <= 200):
                follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(k) +']/div/div[2]/button')
                follow.click()
                k = k+1
                timer = randint(1,50)

                sleep(timer)
                unfollow = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                unfollow.click()
                sleep(0.3)
                print(str(k))


#Faz o login
session_login()

#Busca a pagina
search_page()

#Percorre o modal de seguidores
scroll_down_followers()

while True:
        # Segue X pessoas
        follow()

        #Deixa de seguir X pessoas
        unfollow()
