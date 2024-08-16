
from Modulo_De_Log import *

import os





print(os.linesep)
print('Aqui estaremos testando o modulo de Log')

logging.warning('Teste....')
logging.info('Aqui e um logg de Informação')
logging.critical('Este serviço esta critico...')

logging.info(f'Aqui e um logg de Informação{os.linesep}')



