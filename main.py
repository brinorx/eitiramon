# primeiro que eu instalei as bibliotecas necessárias, selenium, pygame, sys, time do python.
# criei um html com uma caixa vermelha escrito exemplo: itjm.eitisolucoes.local em referencia a um desastre encontrado no zabbix
# o robo aparece após identificar a caixa vermelha, dando um click e apresentando o robo na tela

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Carregue a página da web com o retângulo vermelho
driver.get("file:///C:/Users/Bruno/Downloads/eiti-main/eiti-main/ramon.html") # trocar o caminho para o da sua máquina

# Aguardar até a caixa vermelha aparecer na tela
try:
    '''    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "exemplo: itjm.eitisolucoes.local"))
        )
    '''
    driver.implicitly_wait(5)

    # Encontre as coordenadas da caixa vermelha
    '''rect = element.rect

    # Clique na posição do retângulo vermelho
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, rect['x'] + rect['width'] / 2, rect['y'] + rect['height'] / 2)
    action.click()
    action.perform()'''
    time.sleep(2)
    elemento =  driver.find_element(By.XPATH, "/html/body/div[1]").click() # inspencionar a pagina html e pegar o xpath (copiar o full)


except Exception as e:
    print("Erro ao encontrar o elemento:", e)
