from datetime import date
from datetime import datetime
import random
import sys

print ("Hello everybody!")

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)
print(sys.argv[1])


resultado = random.randint(1,int(sys.argv[2]))
print("El dado giro y obtuvo: ", resultado)