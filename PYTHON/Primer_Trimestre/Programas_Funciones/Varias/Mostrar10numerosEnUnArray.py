datos = [None]*6
for i in range(0,len(datos)+1):
    datos[i-1] = int( input( "Dime el dato numero: "))
print ("Los datos al reves son: ")
for i in range(len(datos)-1,0,-1):
    print ( datos[i-1], end="|" )