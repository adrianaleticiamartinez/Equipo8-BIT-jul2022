import os
import pandas as pd
from getpass import getpass
import base64
from cryptography.fernet import Fernet
import hashlib

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(admin)

def consulta(rol):
	try:
		datos = pd.read_csv('Datos_Descifrados.csv', header=0)
		if(rol == "manager"):
			s = True
			while(s == True):
				search = input("\nIngresa el ID del registro: ")
				ide = datos[datos['idCliente']==search]
				if(ide.empty):
					print("\nNada que mostrar\n")
				else:
					ide.columns = ['ID', 'Nombre', 'ApellidoP', 'ApellidoM', 'FechaN', 'Sexo', 'Segmento', 'Nacionalidad', 'RFC', 'TipoID', 'NumeroID', 'Cuenta', 'Email']
					ide.index = [""]
					print("\n",ide, "\n")

				decision = input("¿Desea buscar otro registro?\nS. Sí\nN. No\n")
				if(decision == "n" or decision == "N"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
					print("\nHasta pronto!\n")
					os.system("rm Datos_Descifrados.csv")
					os.system("rm Admin_Descifrado.csv")
					break
				elif(decision == "s" or decision == "S"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
				else:
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows

		elif(rol == "validador"):
			s = True
			while(s == True):
				search = input("Ingresa el ID del registro: ")
				ide = datos[datos['idCliente']==search]
				if(ide.empty):
					print("\nNada que mostrar\n")
				else:
					iD = ide['idCliente']
					nombre = ide['nombre']
					apellidoP = ide['apellidoPaterno'].astype(str).str[0:3]+"****"
					apellidoM = ide['apellidoMaterno'].astype(str).str[0:3]+"****"
					fechaN = ide['fechaNacimiento'].astype(str).str[0:3]+"****"
					sexo = ide['sexo']
					segmento = ide['segmento']
					nacionalidad = ide['nacionalidad'].astype(str).str[0:3]+"****"
					rfc = ide['rfc'].astype(str).str[0:3]+"****"
					tipoID = ide['tipoID'].astype(str).str[0:3]+"****"
					numeroID = ide['numeroID'].astype(str).str[0:3]+"****"
					cuenta = ide['cuenta']
					email = ide['email'].astype(str).str[0:3]+"****"

					dff = pd.DataFrame({'ID':iD, 'Nombre':nombre, 'ApellidoP':apellidoP, 'ApellidoM': apellidoM, 
						'FechaN': fechaN, 'Sexo': sexo, 'Segmento': segmento, 'Nacionalidad': nacionalidad, 
						'RFC':rfc, 'TipoID': tipoID, 'NumeroID': numeroID, 'Cuenta': cuenta, 'Email':email})
					dff.index = [""]

					print("\n",dff,"\n")
				decision = input("¿Desea buscar otro registro?\nS. Sí\nN. No\n")
				if(decision == "n" or decision == "N"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
					os.system("rm Datos_Descifrados.csv")
					os.system("rm Admin_Descifrado.csv")
					print("\nHasta pronto!\n")
					break
				elif(decision == "s" or decision == "S"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
				else:
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows

		elif(rol == "restringido"):
			s = True
			while(s == True):
				search = input("\nIngresa el ID del registro: ")
				ide = datos[datos['idCliente']==search]
				if(ide.empty):
					print("\nNada que mostrar\n")
				else:
					iD = ide['idCliente']
					nombre = ide['nombre']
					sexo = ide['sexo']
					segmento = ide['segmento']
					cuenta = ide['cuenta']
					dff = pd.DataFrame({'ID':iD, 'Nombre':nombre, 'Sexo':sexo, 'Segmento': segmento, 'Cuenta': cuenta})
					dff.index = [""]

					print("\n",dff,"\n")
				decision = input("¿Desea buscar otro registro?\nS. Sí\nN. No\n")
				if(decision == "n" or decision == "N"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
					os.system("rm Datos_Descifrados.csv")
					os.system("rm Admin_Descifrado.csv")
					print("\nHasta pronto!\n")
					break
				elif(decision == "s" or decision == "S"):
					os.system ("clear") #macOS, Linux
					#os.system("cls") #Windows
				else:
					os.system ("clear") #macOS, Linux
					break
					#os.system("cls") #Windows
		return
	except:
		os.system("clear")
		os.system("rm Datos_Descifrados.csv")
		os.system("rm Admin_Descifrado.csv")
		os.system("clear")
		print("\nHa ocurrido un error, ejecuta nuevamente el programa...\n")

def main():
	llave = "pYZhZwoMj26d-RrW-RKtjynRV6AjVcs7-c0VVFf0HrI="
	descrifrarDocumento2("Admin_Cifrado.txt",llave)
	admin = pd.read_csv('Admin_Descifrado.csv', header=0)
	try:
		p = True
		intentos = 0
		while(p == True):
			user = input("\nIngrese nombre de usuario: ")
			passwd = getpass("Ingrese contraseña: ")
			if(intentos != 3):
				for i in range(0, len(admin["usuario"])):
					if (admin["usuario"][i] == user and admin["auth"][i] == passwd):
						os.system ("clear") #macOS, Linux
						#os.system("cls") #Windows
						print("Bienvenid@ " + user + "\n")
						descrifrarDocumento1("Datos_Cifrado.txt", llave)
						consulta(str(admin['perfil'][i]).lower())
						p = False
						break
				if(p==True):
					intentos = intentos + 1
					print("Contraseña o nombre de usuario inválidos, intenta de nuevo...\n\n")

			if(intentos == 3):
				p = False
				os.system("clear")
				os.system("rm Datos_Descifrados.csv")
				os.system("rm Admin_Descifrado.csv")
				os.system("clear")
				print("\nDemasiados intentos, inténtalo de nuevo en 5 minutos...\n\n")
	except:
		os.system("clear")
		os.system("rm Datos_Descifrados.csv")
		os.system("rm Admin_Descifrado.csv")
		os.system("clear")
		print("\nHa ocurrido un error, ejecuta nuevamente el programa...\n")

def descrifrarDocumento1(nombreArchivo, llave):
    try:
        llave = llave.encode()
        llave = hashlib.sha256(llave)
        key = llave.digest()
        key = base64.urlsafe_b64encode(key)
        f2 = Fernet(key)
        
        with open(nombreArchivo, "rb") as archivo:
            datosArchivo = archivo.read()

        datosDescifrados = f2.decrypt(datosArchivo)

        with open("Datos_Descifrados.csv", "wb") as archivoDescifrado:
            archivoDescifrado.write(datosDescifrados)
        
    except:
    	os.system("clear")
    	os.system("rm Datos_Descifrados.csv")
    	os.system("rm Admin_Descifrado.csv")
    	os.system("clear")
    	print("\nHa ocurrido un error, ejecuta nuevamente el programa...\n")

def descrifrarDocumento2(nombreArchivo, llave):
    try:
        llave = llave.encode()
        llave = hashlib.sha256(llave)
        key = llave.digest()
        key = base64.urlsafe_b64encode(key)
        f2 = Fernet(key)
        
        with open(nombreArchivo, "rb") as archivo:
            datosArchivo = archivo.read()

        datosDescifrados = f2.decrypt(datosArchivo)

        with open("Admin_Descifrado.csv", "wb") as archivoDescifrado:
            archivoDescifrado.write(datosDescifrados)
        
    except:
    	os.system("clear")
    	os.system("rm Admin_Descifrado.csv")
    	os.system("rm Datos_Descifrados.csv")
    	os.system("clear")
    	print("\nHa ocurrido un error, ejecuta nuevamente el programa...\n")

def crifrarDocumento(nombreArchivo1, nombreArchivo2, llave):
	try:
	    llave = llave.encode()
	    llave = hashlib.sha256(llave)
	    key = llave.digest()
	    key = base64.urlsafe_b64encode(key)
	    f = Fernet(key)

	    with open(nombreArchivo1, "rb") as archivo:
	        datos1 = archivo.read()

	    docCifrado1 = f.encrypt(datos1)

	    with open("Datos_Cifrado.txt", "wb") as archivoCifrado1:
	        archivoCifrado1.write(docCifrado1)

	    with open(nombreArchivo2, "rb") as archivo:
	        datos2 = archivo.read()

	    docCifrado2 = f.encrypt(datos2)

	    with open("Admin_Cifrado.txt", "wb") as archivoCifrado2:
	        archivoCifrado2.write(docCifrado2)

	    os.system("clear")
	    os.system("rm baseClientesHackaton2022.csv")
	    os.system("rm baseUsuarios.csv")
	    os.system("clear")
	    main()

	except:
		os.system("clear")
		os.system("rm baseClientesHackaton2022.csv")
		os.system("rm baseUsuarios.csv")
		os.system("clear")
		main()

llave = "pYZhZwoMj26d-RrW-RKtjynRV6AjVcs7-c0VVFf0HrI="
crifrarDocumento("baseClientesHackaton2022.csv", "baseUsuarios.csv", llave)

