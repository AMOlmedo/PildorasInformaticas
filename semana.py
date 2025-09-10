from io import open

semana=open("semana.txt", "w")

dias="lunes \n martes\n miercoles\n jueves\n viernes" 

semana.write(dias)

semana.close()
