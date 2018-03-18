from time import gmtime, strftime    #importar libreria de fecha y hora


km_salida = int(input("kilometros a la salida? \n"))    #ingresar variable
km_entrada = int(input("kilometros a la entrada? \n"))  #"""""

km_total = km_entrada - km_salida   #kilometros realizados del viaje
list  = [km_total];                 #kilometros guardados en lista

print ("kilometros totales recoridos!");
#print (km_total);
print (list[0] , "Km.");

eu = list[0] * 0.12                 #calculo del precio por kilometro

print ("Euros a cobrar: \n" , eu , "euros")

file=open("Cartera.txt","a")       #escritura en archivo

file.write('\n')
file.write(strftime("%Y-%m-%d", gmtime()))     #escritura de fecha
file.write('! ')                    #escritura del dinero
file.write(str(list[0]))
file.write(' / ')
file.write(str(eu))                 #escritura de ganancia
file.write(' euros!')


file.close()                        #cerar el archivo
