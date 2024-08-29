
# from Modulo_De_Log import *

import os

from datetime import datetime
import glob
from time import sleep
import random



# print(os.linesep)
# print('Aqui estaremos testando o modulo de Log')

# logging.warning('Teste....')
# logging.info('Aqui e um logg de Informação')
# logging.critical('Este serviço esta critico...')

# logging.info(f'Aqui e um logg de Informação{os.linesep}')

print(os.linesep)
# horario_Atual = datetime.now().strftime('%H:%M %d/%m/%Y ')

# print(f' Horario de Brasilia, DF é: {horario_Atual}')
# print(os.linesep)

# Horario_da_Automacao = str(input('Qual Horario você deseja rodar a Automacao?:: '))

# print(f'Iremos rodar Atomação as: {Horario_da_Automacao}')
# print(os.linesep)
# print(os.linesep)

   def attach_files(self):             # Anexar arquivos 
        print(f'**********CONFIGURADOR DE ANEXO DE LOGS **********{os.linesep}')
        
        attachment_dir = os.path.join(os.getcwd(), 'LOGS_ARQUIVOS')  # Anexar arquivos de Logs
        files = glob.glob(os.path.join(attachment_dir, '*'))  
        for file_path in files:
            with open(file_path, 'rb') as file:
                self.message.add_attachment(
                    file.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(file_path))
        print(f'⏳ Acabamos de fazer a Manipulação dos arquivos...... ⏳{os.linesep}....Aguarde{os.linesep}')
        sleep(random.randint(1,2))   




# schedule.every().day.at({Horario_da_Automacao}).do(executar_automacao)

