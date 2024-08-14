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
from dotenv import load_dotenv,find_dotenv
from rich import print

print(os.linesep)
print("[italic blue]=================================================================================")
print("[italic red]======           AUTOMAÇÃO                 ==============")
print("[italic blue]=================================================================================")
print("[italic blue]=================================================================================")
print("[italic red]======   Author= Regis Silva              ================")


'''Rich é uma biblioteca Python para escrever texto enriquecido (com cor e estilo) no terminal 
e para exibir conteúdo avançado, como tabelas, markdown e código com destaque de sintaxe.'''

print(os.linesep)

load_dotenv(find_dotenv())

class Tempo_Atual:
    def __init__(self):

        eder_Options = Options()
        eder_Options.add_argument('--lang=pt-BR')
        eder_Options.add_argument('--headless')
        eder_Options.add_argument('disable-notifications')
        eder_Options.add_argument('ignore-certificate-errors')
        eder_Options.add_argument('--ignore-ssl-errors')
        eder_Options.add_argument('--ignore-certificate-errors')
        eder_Options.add_argument('--ignore-ssl-errors')
        # # CONFIGURAÇÃO PARA EXECUTAR O NOSSO NAVEGADOR EM SEGUNDO PLANO
        # eder_Options.add_argument("--headless=new")
        self.webdriver = webdriver.Edge(service=Service(
            EdgeChromiumDriverManager().install()), options=eder_Options)

        self.wait = WebDriverWait(
            driver=self.webdriver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )
        print('[italic green] O Dotenv é uma biblioteca Python que permite carregar variáveis de ambiente a partir de um arquivo .env.')
        print(f'[italic green] Configuração de Login {os.linesep}')
        # self.E_mail_address    = os.environ.get('email_address')
        # self.Password          = os.environ.get('password')
        # self.recipients         = 'regis@servgas.com', 'regenilsom.vcdevaprender@gmail.com'

    def Inicio(self):

        self.webdriver.maximize_window()
        self.webdriver.get("https://www.tempo.com/guarulhos-civ-mil.htm")
        self.Condicoes_Meteorologicas()
        self.Previsoes_Proximo_5_dias()
        self.Modulo_De_Envio()

    def Condicoes_Meteorologicas(self):
        print(os.linesep)
        try:
            
            self.Condicoes_Meteorologicas_Cidade = self.webdriver.find_elements(
                'xpath', ' //*[starts-with(text(),"Previsão do tempo Guarulhos - SP")]'
                )
            
            if 	self.Condicoes_Meteorologicas_Cidade is not None:
                print(os.linesep)
                print('[italic green]  Encontramos....🎙️')
                print('[italic green]  🪟  Estamos Efetivamente dentro das Condições meteorológicas Da sua Cidade.')
                print(f'[italic green] Sua Cidade é 🇧🇷 : {self.Condicoes_Meteorologicas_Cidade[0].text}')
                print(os.linesep)

            self.Temperatura_Atual = self.webdriver.find_elements(
                'xpath','//span[@class="dato-temperatura changeUnitT"]'
            )

            self.Sencacao_termica = self.webdriver.find_elements(
                'xpath','//span[@class="sensacion changeUnitT"]'
            )
            
            if self.Temperatura_Atual and self.Sencacao_termica is not None:
                print(os.linesep)
                print('[italic green]  🌡️ Encontramos. -> TEMPERATURA ATUAL 🌡️')
                print(f'[italic green] 🌞 Hoje a Temperatura Atual da sua Cidade é: {self.Temperatura_Atual[0].text} Graus')
                print(f'[italic green] ⛅ Sensação Termica da sua Cidade é 🌡️ de : {self.Sencacao_termica[0].text} Graus')
                print(os.linesep)
        except:  
            print('[italic red]  🥵  Erro ao Verificar as Condições Atual.....')
            print('[italic red]  🥹  Que tristeza.....')      

    def Previsoes_Proximo_5_dias(self):

        try:
            
            self.webdriver.execute_script("window.scrollTo(0, 200);")
            sleep(3)

            # Criamos uma LISTA vazia, que irá receber a partir do 'FOR' as previsões futuras, Depois iremos disponibilizar no Campo de Envio de E-mails
            self.previsoes_proximo_3_dias = []

            for indice in range(2,7):

                self.previsao_para_os_proximos_dias = self.webdriver.find_elements(
                    'xpath','//span[@class="subtitle-m"]'
                )
                
                self.Temperatura_Maxima = self.webdriver.find_elements(
                    'xpath','//span[@class="max changeUnitT"]'
                )

                self.Temperatura_Minim = self.webdriver.find_elements(
                    'xpath','//span[@class="min changeUnitT"]'
                )
                
                self.nova_linha =f' 🌡️ Previsão para o Próximo dia: {self.previsao_para_os_proximos_dias[indice].text}, Maxíma de: {self.Temperatura_Maxima[indice].text}Graus, Miníma de: {self.Temperatura_Minim[indice].text}Graus'
                print(self.nova_linha + os.linesep)
                #  Iremos 
                self.previsoes_proximo_3_dias.append(self.nova_linha + os.linesep +os.linesep )
                #  Iremos Subdvidir as informações acima 
                print(os.linesep)
                self.X1_Para_Novo_Dia = f' 🌡️ Previsão para o Próximo dia: {self.previsao_para_os_proximos_dias[indice].text}'
                self.X2_Maxima_do_Dia = f' 🌡️ Maxíma de: {self.Temperatura_Maxima[indice].text}Graus'
                self.X3_Minima_do_Dia = f' 🌡️ Miníma de: {self.Temperatura_Minim[indice].text}Graus'

            print(f'[italic yellow] 🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖 ')
            print(os.linesep) 
        except:

            print('[italic red] 🥹 🥵 Erro Ao verificar as Previsões para os Próximos Dias.. 🥹 🥵')  
           
         
    # # Enviar previsão do tempo Via E-mail.
    def Modulo_De_Envio(self):
        
        self.Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
        self.Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')
   

        print(f'[italic green]  🌞 Enviar previsão do 🌞 tempo Via E-mail 📧.{self.Mostrando_o_horario_que_enviou}')
        print('[italic green]   Criando configurações para o Envio de E-mail....')
        EMAIL_ADDRESS  = os.getenv('EMAIL_ADDRESS')
        print(f'Vamos Buscar as informações do 📧 E-mail via Dont Env...')
        EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
        destinatario   = 'regis@servgas.com', 'regenilsom.vcdevaprender@gmail.com'

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise EnvironmentError("[italic red]  🥵 Variáveis de ambiente EMAIL_ADDRESS e EMAIL_PASSWORD não foram definidas 🥵")
        mail = EmailMessage()
        mail['subject'] = f'Previsão do ⛈️ Tempo Chegou do Dia {self.Mostra_a_data_do_ano}'

        print("[italic green] Iremos formatar o envio do E-mail via HTML...")
        
        try:
            mensagem= f'''
            <!Doctype html>
            <html lang="pt-BR">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0"
            <title> Previsão do ⛈️ Tempo!!!! </title>
            <style>
                body {{
                    font-family:             Arial, sans-serif;
                    background-color:        #f4f4f4;
                    color:                   #333;
                    padding:                 20px;
                    }}

                .container {{
                        background-color:  #fff;
                        border-radius:     8px;
                        box-shadow:        0 0 10px rgba(0, 0, 0, 0.1);
                        padding:           20px;
                        max-width:         600px;
                        margin:            auto;
                        position:          relative;
                        min-height:        100vh;
                        }}

                h1{{
                        color:             #1a73e8;
                
                }}   

                .forecast {{
                        margin-top:       20px;
                }}    

                .day{{
                    margin-bottom:       15px;

                }}

                .footer{{
                    position:           absolute;
                    bottom:             20px;
                    left:               50%;
                    transform:          translateX(-50%);
                    text-align:         center;
                    width:              100;
                }}
                .fotter .content-block {{
                    font-size:           12px;
                    color:               #999;
                }}
                .fotter .content-block a{{
                    color:                #999;
                    text-decoration:      none;
                }}
                .fotter .powered-by {{
                    margin-top:           10px;
                }}
            </style>
            </head>
            <body>
            

                <div class="container">
                <h1>Previsão do Tempo para a Cidade de Guarulhos </h1>
                <p>Temperatura:       {self.Temperatura_Atual[0].text} Graus <p/>
                <p> ⛅Sensação Termica da sua Cidade é 🌡️ de : {self.Sencacao_termica[0].text} Graus </p>
                <div class="forecast">
                    <h2> Previsão do Tempo para os próximos 5 dias....</h2>
                    <p>Previsão:  {self.X1_Para_Novo_Dia}  <p/>
                    <p>Previsão:  {self.X2_Maxima_do_Dia}  <p/>
                    <p>Previsão:  {self.X3_Minima_do_Dia}  <p/>
                    <h3>==========***************************************************************=======<h3/>
                    <p>Previsão:  {self.previsoes_proximo_3_dias} <p/>
                    
                    
                </div>
            </div>
            <!-- START FOOTER -->    
            <div class="footer">
                <table role="presentation" boder="0" cellpadding="0" cellspacing="0" align="center">
                    <tr>
                        <td class="content-block">
                            <span class="apple-link"> @Regis 2024 Automatizador de E-maiils..</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="content-block powered-by">
                        Desenvolvido por <a href="https://github.com/RegenilsomSilva/skysaner_passagem"> @Regis Silva - Canal do Dev Aprender Jhontas </a>.
                        </td> 
                    </tr>
                </table>
            </div>
                <!-- END FOOTER -->
            </body>
            </html>
            '''
            print(f'[italic yellow]🙌🙌 Finalizamos a Configuração do Envio de E-mail via HTML & CSS 🙌🙌',os.linesep)
        
        except: 
            print('[italic red] 🥹🥵Erro Ao Formatar a Página em Html e Css...🥹🥵') 

        try:
            mail['From'] = EMAIL_ADDRESS
            mail['To']   = destinatario
            mail.add_header('Content-Type', 'text/html')
            mail.set_payload(mensagem.encode('utf-8'))

            print(f'[italic yellow]  🙌 Vamos Configura o Gmail -> SMPT e SSL 🙌',os.linesep)    
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(mail)
                sleep(random.randint(4, 8))
                print(f'[italic yellow]  🙌E-mail enviado com sucesso 🙌',os.linesep)
            print(f'[italic yellow]   🙌🙌 E-mail enviado com sucesso 🙌 as {self.Mostrando_o_horario_que_enviou[10:]} do Dia {self.Mostra_a_data_do_ano}{os.linesep}......Aguarde{os.linesep}')    
            print('[italic yellow]    Finalizamos as configurações de E-mails.... ',os.linesep)
            print('[italic yellow]  🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖 ',os.linesep)
        
        except:
            print('[italic red] 🥹🥵 Erro ao montar a Configuração de Envio de E-mails....🥹🥵')    

        
rn7 = Tempo_Atual()
rn7.Inicio()
