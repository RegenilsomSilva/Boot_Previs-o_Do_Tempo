from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
# ---------- SELENIUM 4 TRABALHO SERVGAS -------------
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ---------- SELENIUM 4 TRABALHO SERVGAS -------------
import random
from time import sleep
import os
import time

print(os.linesep)
print("=================================================================================")
print("======          AUTOMAÇÃO BUSCARDOR DE SOM  LG XBOOM RN7                  =======")
print("=================================================================================")
print("=================================================================================")
print("======                         BUSCADOR MELHOR PREÇO      trrrrr                =======")

print(os.linesep)

# ENCONTRAR SELENIUM EM QUALQUER NAVEGADOR ==== https://pypi.org/project/webdriver-manager/

class testeChromium:
    def __init__(self):

        eder_Options = Options()
        eder_Options.add_argument('--lang=pt-BR')
        eder_Options.add_argument('--headless')
        eder_Options.add_argument('disable-notifications')
        eder_Options.add_argument('ignore-certificate-errors')
        eder_Options.add_argument('--ignore-ssl-errors')
        eder_Options.add_argument('--ignore-certificate-errors')
        # # CONFIGURAÇÃO PARA EXECUTAR O NOSSO NAVEGADOR EM SEGUNDO PLANO
        eder_Options.add_argument("--headless=new")
        # selenium 4 TRABALHO - SERVGAS 
        self.webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=eder_Options)


        self.wait = WebDriverWait(
            driver=self.webdriver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )

    def Inicio(self):

        try:
            self.webdriver.maximize_window()
            self.webdriver.get("https://www.google.com")
            campo_Pesquisa = self.webdriver.find_element(
                'xpath', '//textarea[@title="Pesquisar"]')
            if campo_Pesquisa is not None:
                print('Econtramos o Campo de pesquisa......')
                sleep(random.randint(2, 3))
                campo_Pesquisa.click()
                campo_Pesquisa.send_keys('caixa de som acustica lg xboom rn7')
                campo_Pesquisa.send_keys(Keys.ENTER)
                print('Demos um Enter no Campo de Pesquisa....')
                print(os.linesep)

        except:
            print('⚠️ Não Foi possível Pesquisa o seu produto... ❌ ')
            print(os.linesep)

        Patrocinado = self.webdriver.find_elements(
            'xpath', '//*[starts-with(text(),"Patrocinado")]')

        if Patrocinado is not None:
            print('Encontramos....🎙️')
            print('🪟  Estamos Efetivamente dentro de Patrocinio')
        try:
            sleep(random.randint(5, 6))
            self.webdriver.find_element(
                'xpath', '//div[@class="top-pla-group-inner"]')
           
        except:
            print('Não foi possivél encontra-ló')
            pass  
        try:
            sleep(6)
            Campo_Patrocinado = self.webdriver.find_element(
                'xpath', '//div[@class="DALGre"]')

            if Campo_Patrocinado is not None:
                print('Estamos aqui...')
                print('Vamos dar Início a buscar por Produto e Precos ')
                print(os.linesep)
            sleep(random.randint(5, 6))
            
            precos_do_Produto = self.webdriver.find_elements(
                'xpath', '//div[@class="pla-unit-container"]')
            if precos_do_Produto is not None:
                print(f'🌐 Encontramos os Produtos e preços...{os.linesep}')
                for produtos in precos_do_Produto:
                    print(produtos.text)
                    print(os.linesep)
                    print(
                        f'❤️ Vamos fazer um laço de Repetição para buscar o Conteudo da página ❤️ {os.linesep} ')
        except:
            print('⚠️ Não Foi possível Encontra o Campo_Patrocinado  ❌ ')
            print(os.linesep)


promo = testeChromium()
promo.Inicio()