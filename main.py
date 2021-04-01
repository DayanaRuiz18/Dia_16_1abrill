#Crear un archivo y escribir en este varias lineas

a=open("archivo.txt","w") 
a.write("Hola\n") 
a.write("Buenos días\n") 
a.write("Espero que tengas un buen día\n")  
a.close()

#Leer el archivo

a=open("archivo.txt","r") 
print(a.read())
a.close()

#Adicionar una nueva linea de texto al final

a=open("archivo.txt","a") 
a.write(":)\n") 
a.close()

#Mostrar el nuevo archivo

a=open("archivo.txt","r") 
print(a.read())
a.close()

#Conocer el contenido linea a linea

a=open("archivo.txt","r") 
print("El contenido de cada linea es",a.readlines(),"\n")
a.close()

#Conocer si podemos escribir en el archivo

a=open("archivo.txt","a") 
print("Podemos escribir en este archivo:",a.writable(),"\n") 
a.close()

#Conocer si podemos escribir en el archivo

a=open("archivo.txt","a") 
print("El flujo de archivos es interactivo:",a.isatty(),"\n") 
a.close()