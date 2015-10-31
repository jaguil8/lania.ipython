import android
import csv
droide=android.Android()
# 100ms entre lecturas
dt = 100
# duracion de la muestras
fin = 30000
tiempo = 0
droide.startSensingTimed(2,dt)
droide.sensorsReadAccelerometer()
lecturas = []
import time
while tiempo <= fin:
    lecturas.append(droide.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    tiempo += dt
    
droide.stopSensing();
with open('resultados.csv', 'w') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(lecturas)