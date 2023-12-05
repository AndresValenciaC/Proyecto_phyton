from clases import Dispositivos, Mision
from funciones import fecha_solicitada,status
import logging

# CLASE DEL REPORTE PRINCIPAL
class Apolo_11:
    def __init__(self,mision_instancia,dispositivos_instancia):
        self.date = fecha_solicitada()
        self.mission = mision_instancia.mission
        self.device_type = dispositivos_instancia.tipo_dispositivo
        self.device_status = status()
    
    def hash(self):
        return f"{self.date}_{self.mission}_{self.device_type}_{self.device_status}"


# INSTANCIAS DE LAS CLASES IMPORTADAS
dispositivos_instancia = Dispositivos()
mision_instancia = Mision()
apolo_11 = Apolo_11(mision_instancia,dispositivos_instancia)

# FUNCIONALIDAD DE LOGGIN
current_time = fecha_solicitada()
logging.basicConfig(
                    level=logging.DEBUG,
                    format='%(message)s',
                    datefmt='%d%m%y%H%M%S',
                    filename=f'./DEVICES/ARCHIVOS_GENERADOS/APLSTATS-[REPORTE]-{current_time}.log',
                    filemode='a'
                    )
                    

# VALIDACIONES
logging.info("date: %s", apolo_11.date)
logging.info("mission: %s", apolo_11.mission)
logging.info("device_type: %s", apolo_11.device_type)
logging.info("device_status: %s", apolo_11.device_status)
logging.info("hash: %s", apolo_11.hash())


