import random
from datetime import datetime

def fecha_solicitada():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

# formato_legible = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
# fecha_actual = fecha_solicitada()
# print(fecha_actual)

def status():
    return random.choice(["excellent", "good", "warning", "faulty", "killed"])

status_dispositivos = status()
# print(status_dispositivos)


def hash(date,mission,device_type,device_status):
    return date+"_"+mission+"_"+device_type+"_"+device_status

# hash_1 = hash("04122023202911","ORBONE","vehículos","good")
# print(hash_1)