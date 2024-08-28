import schedule
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from time import sleep
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
import random
from dotenv import load_dotenv, find_dotenv
from rich import print
from Modulo_De_Log import log
import glob


# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

'''
pip install pigar

È uma Uma ferramenta para gerar requisitos.txt para projeto Python. 
1º pigar
2° Generate requirements.txt 
EX: C/user/..[seu nome]/projeto/ pigar generate 
automaticamente ele criar o arquivo requerimente 

'''

def executar_automacao():
    class Tempo_Atual:
        def __init__(self):
            eder_Options = Options()
            eder_Options.add_argument('--lang=pt-BR')
            eder_Options.add_argument('--headless')
            eder_Options.add_argument('disable-notifications')
            eder_Options.add_argument('ignore-certificate-errors')
            eder_Options.add_argument('--ignore-ssl-errors')
            self.webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=eder_Options)

            self.wait = WebDriverWait(
                driver=self.webdriver,
                timeout=10,
                poll_frequency=1,
                ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]
            )
            log.info('O Dotenv é uma biblioteca Python que permite carregar variáveis de ambiente a partir de um arquivo .env.')
            print('[italic green] O Dotenv é uma biblioteca Python que permite carregar variáveis de ambiente a partir de um arquivo .env.')
            print(f'[italic green] Configuração de Login {os.linesep}')
            log.info(f'Configuração de Login {os.linesep}')

        def Inicio(self):
            self.webdriver.maximize_window()
            self.webdriver.get("https://www.tempo.com/guarulhos-civ-mil.htm")
            self.Condicoes_Meteorologicas()
            self.Previsoes_Proximo_5_dias()
            self.Modulo_De_Envio()

        def Condicoes_Meteorologicas(self):
            try:
                log.info('Dentro de Condições Meteorológicas')
                self.Condicoes_Meteorologicas_Cidade = self.webdriver.find_elements(
                    'xpath', '//*[starts-with(text(),"Previsão do tempo Guarulhos - SP")]'
                )

                if self.Condicoes_Meteorologicas_Cidade:
                    print('[italic green]  Encontramos....🎙️')
                    log.info('Encontramos....🎙️')
                    print('[italic green]  🪟  Estamos Efetivamente dentro das Condições meteorológicas Da sua Cidade.')
                    log.info(f'Sua Cidade é 🇧🇷 : {self.Condicoes_Meteorologicas_Cidade[0].text}')
                    log.info(os.linesep)

                self.Temperatura_Atual = self.webdriver.find_elements(
                    'xpath', '//span[@class="dato-temperatura changeUnitT"]'
                )

                self.Sencacao_termica = self.webdriver.find_elements(
                    'xpath', '//span[@class="sensacion changeUnitT"]'
                )

                if self.Temperatura_Atual and self.Sencacao_termica:
                    print('[italic green]  🌡️ Encontramos. -> TEMPERATURA ATUAL 🌡️')
                    log.info(f'🌡️ Encontramos. -> TEMPERATURA ATUAL 🌡️')
                    print(f'[italic green] 🌞 Hoje a Temperatura Atual da sua Cidade é: {self.Temperatura_Atual[0].text} Graus')
                    log.info(f'🌞 Hoje a Temperatura Atual da sua Cidade é: {self.Temperatura_Atual[0].text} Graus')
                    print(f'[italic green] ⛅ Sensação Termica da sua Cidade é 🌡️ de : {self.Sencacao_termica[0].text} Graus')
                    log.info(f'⛅ Sensação Termica da sua Cidade é 🌡️ de : {self.Sencacao_termica[0].text} Graus')
                    print(os.linesep)
                    log.info(os.linesep)
            except Exception as e:
                print('[italic red]  🥵  Erro ao Verificar as Condições Atual.....')
                log.critical(f'🥵  Erro ao Verificar as Condições Atual: {e}')
                print('[italic red]  🥹  Que tristeza.....')     
                log.critical(f' 🥹  Que tristeza.....')

        def Previsoes_Proximo_5_dias(self):
            try:
                self.webdriver.execute_script("window.scrollTo(0, 200);")
                sleep(3)

                log.warning("Criamos uma LISTA vazia, que irá receber as previsões futuras.")
                self.previsoes_proximo_3_dias = []

                for indice in range(2, 7):
                    self.previsao_para_os_proximos_dias = self.webdriver.find_elements(
                        'xpath', '//span[@class="subtitle-m"]'
                    )

                    self.Temperatura_Maxima = self.webdriver.find_elements(
                        'xpath', '//span[@class="max changeUnitT"]'
                    )

                    self.Temperatura_Minim = self.webdriver.find_elements(
                        'xpath', '//span[@class="min changeUnitT"]'
                    )

                    self.nova_linha = f'🌡️ Previsão para o Próximo dia: {self.previsao_para_os_proximos_dias[indice].text}, Máxima de: {self.Temperatura_Maxima[indice].text}Graus, Mínima de: {self.Temperatura_Minim[indice].text}Graus'
                    print(self.nova_linha + os.linesep)
                    log.info(self.nova_linha + os.linesep)

                    self.previsoes_proximo_3_dias.append(self.nova_linha + os.linesep)

                    self.X1_Para_Novo_Dia = f'🌡️ Previsão para o Próximo dia: {self.previsao_para_os_proximos_dias[indice].text}'
                    self.X2_Maxima_do_Dia = f'🌡️ Máxima de: {self.Temperatura_Maxima[indice].text}Graus'
                    self.X3_Minima_do_Dia = f'🌡️ Mínima de: {self.Temperatura_Minim[indice].text}Graus'

                print(f'[italic yellow] 🤖🤖Obrigado por usar o Nosso Bot🤖🤖')
                log.info(f'🤖🤖Obrigado por usar o Nosso Bot🤖🤖')
                print(os.linesep) 
                log.info(os.linesep)
            except Exception as e:
                print('[italic red] 🥹 🥵 Erro Ao verificar as Previsões para os Próximos Dias.. 🥹 🥵')
                log.warning(f'🥹 🥵 Erro Ao verificar as Previsões para os Próximos Dias: {e}')

        def Modulo_De_Envio(self):
            self.Mostrando_o_horario_que_enviou = datetime.now().strftime('%d/%m/%Y %H:%M')
            self.Mostra_a_data_do_ano = datetime.now().strftime('%d/%m/%Y')

            print(f'[italic green]  🌞 Enviar previsão do 🌞 tempo Via E-mail 📧.{self.Mostrando_o_horario_que_enviou}')
            log.info(f'🌞 Enviar previsão do 🌞 tempo Via E-mail 📧.{self.Mostrando_o_horario_que_enviou}')
            print('[italic green]   Criando configurações para o Envio de E-mail....')
            log.info('Criando configurações para o Envio de E-mail....')
            EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
            EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
            destinatario = ['regis@servgas.com', 'regenilsom.vcdevaprender@gmail.com']

            if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
                raise EnvironmentError("  🥵 Variáveis de ambiente EMAIL_ADDRESS e EMAIL_PASSWORD não foram definidas 🥵")
            mail = EmailMessage()
            mail['subject'] = f'Previsão do ⛈️ Tempo Chegou do Dia {self.Mostra_a_data_do_ano}'

            try:
                mensagem = f'''
                <!Doctype html>
                <html lang="pt-BR">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Previsão do ⛈️ Tempo!!!!</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                    }}
                    .container {{
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        max-width: 600px;
                        margin: auto;
                        position: relative;
                        min-height: 100vh;
                    }}
                    h1 {{
                        color: #007bff;
                    }}
                    p {{
                        line-height: 1.6;
                    }}
                    .signature {{
                        margin-top: 40px;
                        text-align: center;
                    }}
                </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Previsão do Tempo para Hoje 🌥️</h1>
                        <p>🌡️ Temperatura Atual: {self.Temperatura_Atual[0].text} Graus</p>
                        <p>🌞 Sensação Térmica: {self.Sencacao_termica[0].text} Graus</p>
                        <p>🔮 Previsão para os Próximos 5 dias:</p>
                        <ul>
                            {"".join([f"<li>{prev}</li>" for prev in self.previsoes_proximo_3_dias])}
                        </ul>
                        <div class="signature">
                            <p>Enviado por:@Regis Silva Seu Bot de Previsão do Tempo</p>
                            Desenvolvido por <a href="https://github.com/RegenilsomSilva/skysaner_passagem"> @Regis Silva -Aprender não é o Limite, mais perserverar isso te faz um vencedor !!! </a>
                        </div>
                    </div>
                </body>
                </html>
                '''
                mail.set_content(mensagem, subtype='html')
# -----------------------------------------------------------------------------------------------
                print(f'**********CONFIGURADOR DE ANEXO DE LOGS **********{os.linesep}')
                    
                attachment_dir = os.path.join(os.getcwd(), 'LOGS_ARQUIVOS')  # Anexar arquivos de Logs
                files = glob.glob(os.path.join(attachment_dir, '*'))  
                for file_path in files:
                    with open(file_path, 'rb') as file:
                        mail.add_attachment(
                            file.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(file_path))
                print(f'⏳ Acabamos de fazer a Manipulação dos arquivos...... ⏳{os.linesep}....Aguarde{os.linesep}')
                sleep(random.randint(1,2))   


# -----------------------------------------------------------------------------------------------
                log.info('Preparando a mensagem com a previsão do tempo.')
                for destinatario in destinatario:
                    mail['to'] = destinatario
                    mail['from'] = EMAIL_ADDRESS
                    log.info(f'Enviando E-mail para {destinatario}')
                    print(f'[italic yellow] Enviando E-mail para {destinatario}')
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        smtp.send_message(mail)
                    print('[italic green]  Email Enviado com sucesso!')
                    log.info(f'Email Enviado com sucesso!')
            except Exception as e:
               
                print('[italic green]  Email Enviado com sucesso!')
                log.info(f'Email foi enviado com sucesso!{e}')

    rn7 = Tempo_Atual()
    rn7.Inicio()

# Agendando a tarefa para rodar Dimanicamente Pelo Usuários ......
print('Agendandor de tarefa para rodar Dimanicamente.......',os.linesep)
print(os.linesep)
horario_Atual = datetime.now().strftime('%H:%M %d/%m/%Y ')

print(f' Horario de Brasilia, DF é: {horario_Atual}')
print(os.linesep)

Horario_da_Automacao = str(input('Qual Horario você deseja rodar a Automacao?:: '))

print(f'Iremos rodar Automação as: {Horario_da_Automacao}')
print(os.linesep)

schedule.every().day.at(f'{Horario_da_Automacao}').do(executar_automacao)

while True:
    schedule.run_pending()
    time.sleep(60)  # Aguarda um minuto para checar novamente
