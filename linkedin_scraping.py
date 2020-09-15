# import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv

# arquivo csv
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])


# Chrome diver
driver = webdriver.Chrome('./chromedriver')

# maximizar janela
driver.maximize_window()

# LINKEDIN

# acessar LinkedIn
driver.get('https://www.linkedin.com/')
sleep(1)

# clicar no botão de login
# driver.find_element_by_css_selector('a.nav__button-secondary').click()
driver.find_element_by_xpath('/html/body/nav/a[3]').click()
sleep(3)

# preencher usuario
# usuario_input = driver.find_element_by_css_selector('input#username')
usuario_input = driver.find_element_by_name('session_key')
usuario_input.send_keys('seuemail')

# preencher senha
senha_input = driver.find_element_by_name('session_password')
senha_input.send_keys('suasenha')

# clicar para logar
# driver.find_element_by_css_selector("button.btn__primary--large").click()
# driver.find_element_by_xpath('//button[text()="Sign in"]').click()
senha_input.send_keys(Keys.RETURN)
sleep(3)

# GOOGLE
driver.get('https://google.com')
sleep(1)

# selecionar campo de busca
# campo_busca = driver.find_element_by_xpath('//input[@name="q"]')
busca_input = driver.find_element_by_name('q')

# fazer busca no google
busca_input.send_keys('site:linkedin.com/in/ AND "Data Scientist" and "São paulo"')
busca_input.send_keys(Keys.RETURN)
sleep(2)

# extrair lista de perfis
lista_perfil = driver.find_elements_by_xpath('//div[@class="r"]/a')
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

# conectar com usuários
i = 0
for perfil in lista_perfil:
    
    if i%2 == 0:
        driver.get('https://www.youtube.com/')
        sleep(3)
        driver.execute_script("window.scrollTo(0, 630)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 15)")
        sleep(2)
        driver.execute_script("window.scrollTo(0, 45)")
        sleep(2)
    else:
        driver.get('https://medium.com/')
        sleep(3)
        driver.execute_script("window.scrollTo(0, 630)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 15)")
        sleep(2)
        driver.execute_script("window.scrollTo(0, 45)")
        sleep(2)
    
    driver.get(perfil)
    driver.execute_script("window.scrollTo(0, 630)")
    sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    sleep(1)
    driver.execute_script("window.scrollTo(0, 15)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, 45)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, 550)")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 10)")
    sleep(2)
    
    try:
        driver.find_element_by_xpath('//button[normalize-space()="Conectar"]').click()
        sleep(1)
    except: NoSuchElementException
    # handle the element not existing
    
    try:
        driver.find_element_by_xpath('//button[normalize-space()="Concluído"]') .click()
        sleep(3)
    except: NoSuchElementException
    
    if i%2 == 0:
        driver.get('https://www.uol.com.br/')
        sleep(3)
        driver.execute_script("window.scrollTo(0, 630)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 15)")
        sleep(2)
        driver.execute_script("window.scrollTo(0, 305)")
        sleep(2)
    else:
        driver.get('https://www.globo.com/')
        sleep(3)
        driver.execute_script("window.scrollTo(0, 630)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 150)")
        sleep(2)
        driver.execute_script("window.scrollTo(0, 45)")
        sleep(2)   
    i = i+1



# sair do driver
driver.quit()
