
import logging
from rich.logging import RichHandler
from rich import print
import os 


class LogModulo():
    
    # Configurando o formato do log via Rich loggin 
    '''Rich é uma biblioteca Python para escrever texto enriquecido (com cor e estilo) no terminal 
    e para exibir conteúdo avançado, como tabelas, markdown e código com destaque de sintaxe.'''

    FORMAT = "%(asctime)s - %(message)s"
    logging.basicConfig(
        level="NOTSET",
        format=FORMAT,
        datefmt="[%d/%m/%Y %H:%M]",  # Configuração de Data e Hora, Brasil
        
        handlers=[
            RichHandler(),                        # Exibe as mensagens no console
            logging.FileHandler(r'LOGS_ARQUIVOS' + os.sep + "arquivoDeLog.log",mode='w')    # Salva as mensagens no arquivo de log
            #  logging.FileHandler("arquivoDeLog.log",mode='w')    # Salva as mensagens no arquivo de log
        ]
    )
registro =LogModulo()


