import random
from datetime import datetime
# from .CONFIG.config import status_options

# ****************************ARCHIVOS***********************************************
# CICLO DE SIMULACIÓN (INICIALMENTE CADA 20 SEG)
def ciclo_de_simulacion():
    """Esta función tendrá como objetivo generar el ciclo de la simulación que irá inicialmente hasta 20 segundos"""
    pass

# GENERACIÓN ALEATORIA DE 1 A 100 REPORTES POR ITERACIÓN
def numero_de_reportes():
    """Esta función tendrá como objetivo generar un numero aleatorio de 1 a 100 reportes por iteación"""
        
    pass


# FECHA DEL ARCHIVOS
def fecha_solicitada():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

# STATUS DEL ARCHIVOS 
def status():
    return random.choice(["excellent", "good", "warning", "faulty", "killed"])

status_dispositivos = status()

# HASH DEL ARCHIVOS
def hash(date,mission,device_type,device_status):
    return date+"_"+mission+"_"+device_type+"_"+device_status


