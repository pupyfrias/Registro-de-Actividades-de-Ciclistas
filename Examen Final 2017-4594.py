import os
from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import date
import webbrowser
import folium


    

#BASE DE DATOS
baseDeDatos = sqlite3.connect('Base de Datos.db')
cursor = baseDeDatos.cursor()
if(os.path.isfile('Base de Datos.db')):
    pass
else:
    cursor.execute('CREATE TABLE Ciclistas (Cédula int primary key, Nombre varchar(30), Apellido varchar(50), FechaDeNacimiento varchar(15),TipoDeSangre varchar(10),SizeDeBicicleta varchar(4),SizeDeUniforme varchar(4),Teléfono varchar(12),Celular varchar(12), Email varchar(40), Dirección varchar (60), PersonaDeContacto varchar(50), TeléfonoDeContacto varchar(12))')
    cursor.execute("CREATE TABLE RegistroActividad (Cédula int ,Ciclita varchar(50), FechaDeLaActividad varchar(12), Distancia varchar(15), Lugar varchar(30), Latitud float (15), Longitud float (15), Dificultad varchar(1),foreign key (Cédula) references Ciclistas (Cédula) on delete cascade )")
    baseDeDatos.commit()


        
#FUNCIONES
def limpiar():
    os.system('cls')
    
def soloTexto(texto):
    if '0' in texto or '1' in texto or '2' in texto or '3' in texto or '4' in texto or '5' in texto or '6' in texto or '7' in texto or '8' in texto or '9' in texto:
        return False
    elif '`' in texto or '!' in texto or '@' in texto or '$' in texto or '%' in texto or '^' in texto or '&' in texto or '*' in texto or '(' in texto or ')' in texto or '_' in texto or '-' in texto or '+' in texto or '=' in texto or '[' in texto or ']' in texto or '{' in texto or '}' in texto or '|' in texto or ',' in texto or '.' in texto or '/' in texto or '?' in texto or '¿' in texto or '¡' in texto or ':' in texto or ';' in texto or '<' in texto or  '>' in texto:
        return False    
    
def soloNumero(numero):
    try:
        numero = float(numero)
    except:
        return False     
  
def abrirVentana():
    
    try:
        ventana.deiconify() 
    except:
        pass
    try:
        ventana2.withdraw()
    except:
        pass
    try:
        ventana6.withdraw()
    except:
        pass
    try:
        ventana7.withdraw()
    except:
        pass
       
def abrirVentana2():
    
    try:
        ventana2.deiconify() 
    except:
        pass
    try:
        ventana3.withdraw()
    except:
        pass
    try:
        ventana4.withdraw()
    except:
        pass
    try:
        ventana5.withdraw()
    except:
        pass

def GuardarAgregado(): 
     
    eliminarErroresAgregar()
    Cedula = cedula.get()
    Nombre = nombre.get()
    Apellido = apellido.get()
    FechaNacimiento = fechaNacimiento.get()
    TipoSangre = tipoSangre.get()
    SizeBici = sizeBici.get()
    SizeUniforme = sizeUniforme.get()
    Telefono = telefono.get()
    Celular = celular.get()
    Email = email.get()
    Direccion = direccion.get()
    PersonaContacto = personaContacto.get()
    TelPersonaContacto = telPersonaContacto.get()
    
   
    global errorAgregar1
    global errorAgregar2
    global errorAgregar3
    global errorAgregar4
    global errorAgregar5
    global errorAgregar6
    global errorAgregar7
    global errorAgregar8
    global errorAgregar9
    global errorAgregar10
    global errorAgregar11
    global errorAgregar12
    global DatosAgregados
    
    
    verificador = 0
    
    #OBTENIENDO TODAS LAS CEDULAS 
    
    ListaCedula = []

    TodosCedula = cursor.execute('SELECT Cédula FROM Ciclistas')
    for cedula_ in TodosCedula:
        ListaCedula.append(cedula_[0])
    
    if Cedula in ListaCedula:
        verificador += 1
        errorAgregar1 = Label(contenedor3, text='Esa Cédula ya está registrada',fg="red")
        errorAgregar1.grid(row=3,column=1,sticky=W+N)

    elif Cedula == '':
        verificador += 1
        
        errorAgregar1 =Label(contenedor3, text='Este campo no puede estar vacio',fg="red")
        errorAgregar1.grid(row=3,column=1,sticky=W+N)
        
    elif soloNumero(Cedula) == False:
        
        verificador += 1
        errorAgregar1 = Label(contenedor3, text='En este campo solo se admiten número',fg="red")
        errorAgregar1.grid(row=3,column=1,sticky=W+N)
    
    elif len(Cedula) != 11:
        
        verificador += 1
        errorAgregar1 = Label(contenedor3, text='La Cédula debe tener 11 digitos',fg="red")
        errorAgregar1.grid(row=3,column=1,sticky=W+N)
        
    
    
    if Nombre == '':
        verificador += 1
        errorAgregar2 =Label(contenedor3, text='Este campo no puede estar vacio',fg="red")
        errorAgregar2.grid(row=3,column=2,sticky=W+N)
        
    elif soloTexto(Nombre) == False:
        verificador += 1
        errorAgregar2 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar2.grid(row=3,column=2,sticky=W+N)
    
    if Apellido == '':
        verificador += 1
        errorAgregar3 =Label(contenedor3, text='Este campo no puede estar vacio',fg="red")
        errorAgregar3.grid(row=6,column=1,sticky=W+N)
    elif soloTexto(Apellido) == False:
        verificador += 1
        errorAgregar3 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar3.grid(row=6,column=1,sticky=W+N)
    
    if FechaNacimiento == '':
        verificador += 1
        errorAgregar4 =Label(contenedor3, text='Este campo no puede estar vacio',fg="red")
        errorAgregar4.grid(row=6,column=2,sticky=W+N)
    else:
        try:
            Fecha= FechaNacimiento.split('/')
            FechaNacimiento = date(int(Fecha[2]),int(Fecha[1]),int(Fecha[0]))
            if FechaNacimiento > date.today():
                verificador += 1
                errorAgregar4 =Label(contenedor3, text= 'Aún no hemos legado a esta fecha',fg="red")
                errorAgregar4.grid(row=6,column=2,sticky=W+N)
                
    
        except :
            verificador += 1
            errorAgregar4 =Label(contenedor3, text= 'Fecha Incorrecta',fg="red")
            errorAgregar4.grid(row=6,column=2,sticky=W+N)
        
            
  
    if '`' in TipoSangre  or '!' in TipoSangre  or '@' in TipoSangre  or '$' in TipoSangre  or '%' in TipoSangre  or '^' in TipoSangre  or '&' in TipoSangre  or '*' in TipoSangre  or '(' in TipoSangre  or ')' in TipoSangre  or '_' in TipoSangre  or '=' in TipoSangre  or '[' in TipoSangre  or ']' in TipoSangre  or '{' in TipoSangre  or '}' in TipoSangre  or '|' in TipoSangre  or ',' in TipoSangre  or '.' in TipoSangre  or '/' in TipoSangre  or '?' in TipoSangre  or '¿' in TipoSangre  or '¡' in TipoSangre  or ':' in TipoSangre  or ';' in TipoSangre  or '<' in TipoSangre  or  '>' in TipoSangre  or '0' in TipoSangre  or '1' in TipoSangre  or '2' in TipoSangre  or '3' in TipoSangre  or '4' in TipoSangre  or '5' in TipoSangre  or '6' in TipoSangre  or '7' in TipoSangre  or '8' in TipoSangre  or '9' in TipoSangre :
        verificador += 1
        errorAgregar5 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar5.grid(row=9,column=1,sticky=W+N)
    

    
    if  '' == SizeBici or  's' == SizeBici.lower() or 'm' ==  SizeBici.lower() or 'l' ==  SizeBici.lower() or  'xl' ==  SizeBici.lower() or  '2xl' ==  SizeBici.lower() or '3xl' ==  SizeBici.lower() or '4xl' ==  SizeBici.lower() or  '5xl' ==  SizeBici.lower():
        pass
    else:
        verificador += 1
        errorAgregar6 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar6.grid(row=9,column=2,sticky=W+N) 
    
    if  '' == SizeUniforme or  's' == SizeUniforme.lower() or 'm' ==  SizeUniforme.lower() or 'l' ==  SizeUniforme.lower() or  'xl' ==  SizeUniforme.lower() or  '2xl' ==  SizeUniforme.lower() or '3xl' ==  SizeUniforme.lower() or '4xl' ==  SizeUniforme.lower() or  '5xl' ==  SizeUniforme.lower():
        pass
    else:
        verificador += 1
        errorAgregar7 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar7.grid(row=12,column=1,sticky=W+N) 
        
    if Telefono == '':
        pass
    elif soloNumero(Telefono) == False:
        
        verificador += 1
        errorAgregar8 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar8.grid(row=12,column=2,sticky=W+N)
        
    if Celular == '':
        pass
    elif soloNumero(Celular) == False:
        
        verificador += 1
        errorAgregar9 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar9.grid(row=15,column=1,sticky=W+N)
        
    if Email == '':
        pass
    elif not '@' in Email:
        
        verificador += 1
        errorAgregar10 =Label(contenedor3, text='Correo Incorrecto',fg="red")
        errorAgregar10.grid(row=15,column=2,sticky=W+N)
        
    if soloTexto(PersonaContacto) == False:
        verificador += 1
        errorAgregar11 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar11.grid(row=18,column=2,sticky=W+N)
        
    if TelPersonaContacto == '':
        pass
    elif soloNumero(TelPersonaContacto) == False:
        verificador += 1
        errorAgregar12 =Label(contenedor3, text='Caracteres Incorrectos',fg="red")
        errorAgregar12.grid(row=21,column=1,columnspan=2)
        
    #LIMPIANDO LAS CAJAS DE ENTRADA DE DATOS        
    if verificador == 0:
        
        
        cursor.execute(f"INSERT INTO Ciclistas values ({str(Cedula)},'{Nombre}','{Apellido}','{FechaNacimiento}','{TipoSangre}','{SizeBici}','{SizeUniforme}','{Telefono}','{Celular}','{Email}','{Direccion}','{PersonaContacto}','{TelPersonaContacto}')")
        baseDeDatos.commit()
        ventana3.withdraw()
        Agregar()
        DatosAgregados = Label(contenedor3, text = 'Datos Agregados Correctamente', font= 'bold', fg='green')
        DatosAgregados.grid(row=23, column=1, columnspan=2,pady=(20,0))
    
    
def GuardarActividad():
    
    eliminarErroresActividad()
    
    ciclista = CiclistaA.get()
    fecha = fechaActividad.get()
    distancia = Distacia.get()
    lugar = Lugar.get()
    latitud = Latitud.get()
    longitud = Longitud.get()
    dificultad = Dificultad.get()
    
    
    global errorActividad1
    global errorActividad2
    global errorActividad3
    global errorActividad4
    global errorActividad5
    global errorActividad6
    global errorActividad7
    global DatosCorrectos
   

    
    
    verificador = 0
    
   

    if ciclista == '':
        verificador += 1
        
        errorActividad1 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad1.grid(row=4,column=0,sticky=W+N)
        
    elif soloTexto(ciclista) == False:
        
        verificador += 1
        errorActividad1 = Label(contenedor6, text='En este campo solo se admiten número',fg="red")
        errorActividad1.grid(row=4,column=0,sticky=W+N)
        
        
    if fecha == '':
        verificador += 1
        errorActividad2 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad2.grid(row=4,column=1,sticky=W+N)
        
    else:
        try:
            actividadFecha = fecha.split('/')
            fecha = date(int(actividadFecha[2]),int(actividadFecha[1]),int(actividadFecha[0]))
            if fecha > date.today():
                verificador += 1
                errorActividad2 =Label(contenedor6, text= 'Aún no hemos legado a esta fecha',fg="red")
                errorActividad2.grid(row=4,column=1,sticky=W+N)
                
    
        except :
            verificador += 1
            errorActividad2 =Label(contenedor6, text= 'Fecha Incorrecta',fg="red")
            errorActividad2.grid(row=4,column=1,sticky=W+N)    
    
    
    

    
    if distancia == '':
        verificador += 1
        errorActividad3 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad3.grid(row=4,column=2,sticky=W+N)
    elif soloNumero(distancia) == False:
        verificador += 1
        errorActividad3 =Label(contenedor6, text='Caracteres Incorrectos',fg="red")
        errorActividad3.grid(row=4,column=2,sticky=W+N)
    
  
    if lugar == '':
        verificador += 1
        errorActividad4 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad4.grid(row=7,column=0,sticky=W+N)
    
            
  
    if latitud == '':
        verificador += 1
        errorActividad5 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad5.grid(row=7,column=1,sticky=W+N)
    elif soloNumero(latitud) == False:
        verificador += 1
        errorActividad5 =Label(contenedor6, text='Caracteres Incorrectos',fg="red")
        errorActividad5.grid(row=7,column=1,sticky=W+N)
        
    elif float(latitud) < 17.6 or float(latitud) >19.96:
        verificador += 1
        errorActividad5 =Label(contenedor6, text='La Latitud debe estar entre 17.6 y 19.96',fg="red")
        errorActividad5.grid(row=7,column=1,sticky=W+N)
        
    
    if longitud == '':
        verificador += 1
        errorActividad6 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad6.grid(row=7,column=2,sticky=W+N)
        
    elif soloNumero(longitud) == False:
        verificador += 1
        errorActividad6 =Label(contenedor6, text='Caracteres Incorrectos',fg="red")
        errorActividad6.grid(row=7,column=2,sticky=W+N)
        
    elif float(longitud) > -68.31 or float(longitud) <-72.01:
        verificador += 1
        errorActividad6 =Label(contenedor6, text='La Longuitudd debe estar entre -68.31 y -72.01 ',fg="red")
        errorActividad6.grid(row=7,column=2,sticky=W+N)
        
        
        
        
    if dificultad== '':
        verificador += 1
        errorActividad7 =Label(contenedor6, text='Este campo no puede estar vacio',fg="red")
        errorActividad7.grid(row=10,column=0,columnspan=3)
    else:
        if '1' == dificultad or  '2' == dificultad or '3' == dificultad:
            pass
        else:
            verificador += 1
            errorActividad7 =Label(contenedor6, text='Caracteres Incorrectos',fg="red")
            errorActividad7.grid(row=10,column=0,columnspan=3)
    
    if verificador ==0:
        cursor.execute(f"insert into RegistroActividad values({CedulaActividad},'{NombreCiclista}','{fecha}','{distancia}','{lugar}',{latitud},{longitud},'{dificultad}')")
        baseDeDatos.commit()
        ventana6.withdraw()
        GestionarActividades()
        
        DatosCorrectos =Label(contenedor6, text='Datos Agregados Correctamente', font='bold', fg='green')
        DatosCorrectos.grid(row= 13, column=0, columnspan=3, pady=20)
        
def  GuadarModificar():
    
    eliminarErroresModificar() 
    Cedula = cedulaM.get()
    Nombre = nombreM.get()
    Apellido = apellidoM.get()
    FechaNacimiento = fechaNacimientoM.get()
    TipoSangre = tipoSangreM.get()
    SizeBici = sizeBiciM.get()
    SizeUniforme = sizeUniformeM.get()
    Telefono = telefonoM.get()
    Celular = celularM.get()
    Email = emailM.get()
    Direccion = direccionM.get()
    PersonaContacto = personaContactoM.get()
    TelPersonaContacto = telPersonaContactoM.get()
    
    global errorModificar1
    global errorModificar2
    global errorModificar3
    global errorModificar4
    global errorModificar5
    global errorModificar6
    global errorModificar7
    global errorModificar8
    global errorModificar9
    global errorModificar10
    global errorModificar11
    global errorModificar12
    global DatosAgregadosM

    
    
    verificador = 0
    
   

    if Cedula == '':
        verificador += 1
        
        errorModificar1 =Label(contenedor4, text='Este campo no puede estar vacio',fg="red")
        errorModificar1.grid(row=5,column=0,sticky=W+N)
        
    elif soloNumero(Cedula) == False:
        
        verificador += 1
        errorModificar1 = Label(contenedor4, text='En este campo solo se admiten número',fg="red")
        errorModificar1.grid(row=5,column=0,sticky=W+N)
        
    elif len(Cedula) != 11:
        
        verificador += 1
        errorAgregar1 = Label(contenedor4, text='La Cédula debe tener 11 digitos',fg="red")
        errorAgregar1.grid(row=5,column=0,sticky=W+N)
    
    
    if Nombre == '':
        verificador += 1
        errorModificar2 =Label(contenedor4, text='Este campo no puede estar vacio',fg="red")
        errorModificar2.grid(row=5,column=1,sticky=W+N)
        
    elif soloTexto(Nombre) == False:
        verificador += 1
        errorModificar2 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar2.grid(row=5,column=1,sticky=W+N)
    
    if Apellido == '':
        verificador += 1
        errorModificar3 =Label(contenedor4, text='Este campo no puede estar vacio',fg="red")
        errorModificar3.grid(row=5,column=2,sticky=W+N)
    elif soloTexto(Apellido) == False:
        verificador += 1
        errorModificar3 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar3.grid(row=5,column=2,sticky=W+N)
    
    if FechaNacimiento == '':
        verificador += 1
        errorModificar4 =Label(contenedor4, text='Este campo no puede estar vacio',fg="red")
        errorModificar4.grid(row=8,column=0,sticky=W+N)
    else:
        try:
            Fecha= FechaNacimiento.split('/')
            FechaNacimiento = date(int(Fecha[2]),int(Fecha[1]),int(Fecha[0]))
            if FechaNacimiento > date.today():
                verificador += 1
                errorModificar4 =Label(contenedor4, text= 'Aún no hemos legado a esta fecha',fg="red")
                errorModificar4.grid(row=8,column=0,sticky=W+N)
                
    
        except :
            verificador += 1
            errorModificar4 =Label(contenedor4, text= 'Fecha Incorrecta',fg="red")
            errorModificar4.grid(row=8,column=0,sticky=W+N)
        
            
  
    if '`' in TipoSangre  or '!' in TipoSangre  or '@' in TipoSangre  or '$' in TipoSangre  or '%' in TipoSangre  or '^' in TipoSangre  or '&' in TipoSangre  or '*' in TipoSangre  or '(' in TipoSangre  or ')' in TipoSangre  or '_' in TipoSangre  or '=' in TipoSangre  or '[' in TipoSangre  or ']' in TipoSangre  or '{' in TipoSangre  or '}' in TipoSangre  or '|' in TipoSangre  or ',' in TipoSangre  or '.' in TipoSangre  or '/' in TipoSangre  or '?' in TipoSangre  or '¿' in TipoSangre  or '¡' in TipoSangre  or ':' in TipoSangre  or ';' in TipoSangre  or '<' in TipoSangre  or  '>' in TipoSangre  or '0' in TipoSangre  or '1' in TipoSangre  or '2' in TipoSangre  or '3' in TipoSangre  or '4' in TipoSangre  or '5' in TipoSangre  or '6' in TipoSangre  or '7' in TipoSangre  or '8' in TipoSangre  or '9' in TipoSangre :
        verificador += 1
        errorModificar5 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar5.grid(row=8,column=1,sticky=W+N)
    

    
    if  '' == SizeBici or  's' == SizeBici.lower() or 'm' ==  SizeBici.lower() or 'l' ==  SizeBici.lower() or  'xl' ==  SizeBici.lower() or  '2xl' ==  SizeBici.lower() or '3xl' ==  SizeBici.lower() or '4xl' ==  SizeBici.lower() or  '5xl' ==  SizeBici.lower():
        pass
    else:
        verificador += 1
        errorModificar6 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar6.grid(row=8,column=2,sticky=W+N) 
    
    if  '' == SizeUniforme or  's' == SizeUniforme.lower() or 'm' ==  SizeUniforme.lower() or 'l' ==  SizeUniforme.lower() or  'xl' ==  SizeUniforme.lower() or  '2xl' ==  SizeUniforme.lower() or '3xl' ==  SizeUniforme.lower() or '4xl' ==  SizeUniforme.lower() or  '5xl' ==  SizeUniforme.lower():
        pass
    else:
        verificador += 1
        errorModificar7 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar7.grid(row=11,column=0,sticky=W+N) 
        
    if Telefono == '':
        pass
    elif soloNumero(Telefono) == False:
        
        verificador += 1
        errorModificar8 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar8.grid(row=11,column=1,sticky=W+N)
        
    if Celular == '':
        pass
    elif soloNumero(Celular) == False:
        
        verificador += 1
        errorModificar9 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar9.grid(row=11,column=2,sticky=W+N)
        
    if Email == '':
        pass
    elif not '@' in Email:
        
        verificador += 1
        errorModificar10 =Label(contenedor4, text='Correo Incorrecto',fg="red")
        errorModificar10.grid(row=14,column=0,sticky=W+N)
        
    if soloTexto(PersonaContacto) == False:
        verificador += 1
        errorModificar11 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar11.grid(row=14,column=1,sticky=W+N)
        
    if TelPersonaContacto == '':
        pass
    elif soloNumero(TelPersonaContacto) == False:
        verificador += 1
        errorModificar12 =Label(contenedor4, text='Caracteres Incorrectos',fg="red")
        errorModificar12.grid(row=14,column=2,columnspan=2)
        
       
    if verificador == 0:
                                                                                                                                                                                                                                                                                                           
        cursor.execute(f"UPDATE Ciclistas SET Cédula ={str(Cedula)}, Nombre='{Nombre}',Apellido ='{Apellido}',FechaDeNacimiento = '{FechaNacimiento}',TipoDeSangre = '{TipoSangre}',SizeDeBicicleta ='{SizeBici}',SizeDeUniforme = '{SizeUniforme}',Teléfono = '{Telefono}',Celular ='{Celular}',Email= '{Email}',Dirección = '{Direccion}',PersonaDeContacto ='{PersonaContacto}',TeléfonoDeContacto ='{TelPersonaContacto}' WHERE Cédula ={cedulaNueva}")
        baseDeDatos.commit()
        ventana4.withdraw()
        Modificar()
        DatosAgregadosM = Label(contenedor4, text = 'Datos Agregados Correctamente', font= 'bold', fg='green')
        DatosAgregadosM.grid(row=18, column=1, columnspan=1,pady=(20,0))

def EliminarRegistro():
    cursor.execute(f'delete from Ciclistas where Cédula = {int(cedulaEliminar)}')
    try:
        cursor.execute(f'delete from RegistroActividad where Cédula = {int(cedulaEliminar)}')
    except:
        pass
    baseDeDatos.commit()
    ventana5.withdraw()
    Eliminar()
    Label(contenedor5,text = 'REGISTRO ELIMINADO CORRECTAMENTE', fg='green').grid(row=18, column=1,pady=30)
      
def SelecionarEliminar():
    global cedulaEliminar
    Seleccion = tabla2.focus()
    Valores = tabla2.item( Seleccion)
    cedulaEliminar = Valores['text']
    BotonEliminar.config(state = NORMAL)
    
def SelecionarActividad():
    eliminarErroresActividad()
    global CedulaActividad
    global NombreCiclista
    Seleccion = tabla3.focus()
    Valores = tabla3.item( Seleccion)
    CedulaActividad = Valores['text']
    NombreCiclista = Valores['values'][0]+' '+Valores['values'][1]
    
    CiclistaA.delete(0,END)
    CiclistaA.insert(0,NombreCiclista)
    
def SelecionarModificar():
    
    eliminarErroresModificar()
    Seleccion = tabla.focus()
    Valores = tabla.item( Seleccion)
    cedulaM.insert(0,Valores['text'])
    
    
    
    
    #BORRAR ENTRADAS
    
    cedulaM.delete(0,END)
    nombreM.delete(0,END)
    apellidoM.delete(0,END)
    fechaNacimientoM.delete(0,END)
    tipoSangreM.delete(0,END)
    sizeBiciM.delete(0,END)
    sizeUniformeM.delete(0,END)
    telefonoM.delete(0,END)
    celularM.delete(0,END)
    emailM.delete(0,END)
    direccionM.delete(0,END)
    personaContactoM.delete(0,END)
    telPersonaContactoM.delete(0,END)
    
    #ENTRADAS
    global cedulaNueva
    
    if Valores['text'] !='':
        
        cedulaNueva = Valores['text']
        
    cedulaM.insert(0,Valores['text'])
    nombreM.insert(0,Valores['values'][0])
    apellidoM.insert(0,Valores['values'][1])
    Fecha= (Valores['values'][2]).split('-')
    FechaFormatiada = f'{Fecha[2]}/{Fecha[1]}/{Fecha[0]}'
    fechaNacimientoM.insert(0,FechaFormatiada)
    tipoSangreM.insert(0,Valores['values'][3])
    sizeBiciM.insert(0,Valores['values'][4])
    sizeUniformeM.insert(0,Valores['values'][5])
    telefonoM.insert(0,Valores['values'][6])
    celularM.insert(0,Valores['values'][7])
    emailM.insert(0,Valores['values'][8])
    direccionM.insert(0,Valores['values'][9])
    personaContactoM.insert(0,Valores['values'][10])
    telPersonaContactoM.insert(0,Valores['values'][11])
    BotonrGuadar.config(state = NORMAL)

def SelecionarExportar():
    
  
    Seleccion = tabla7.focus()
    Valores = tabla7.item( Seleccion)
    Fecha= (Valores['values'][2]).split('-')
    FechaFormatiada = f'{Fecha[2]}/{Fecha[1]}/{Fecha[0]}'
    cedula = Valores['text']
    
    info = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Bootstrap Example</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        </head>
        <body>

        <div class="container">
        <h2>Datos Personales</h2>
                    
        <table class="table">
            <thead>
            <tr>
                <th>Nombres</th>
                <th>Apellidos</th>
                <th>Cédula</th>
                <th>Fecha de Nacimiento</th>
                <th>Tipo de Sangre</th>
                <th>Size de Bicicleta</th>
                <th>Size de Uniforme</th>
                <th>Teléfono</th>
                <th>Celular</th>
                <th>Email</th>
                <th>Dirección</th>
                <th>Persona de Contacto</th>
                <th>Teléfono de Contacto</th>
                
            </tr>
            </thead>
            <tbody>
            <tr>
                
                <td>{Valores['values'][0]}</td>
                <td>{Valores['values'][1]}</td>
                <td>{Valores['text']}</td>
                <td>{FechaFormatiada}</td>
                <td>{Valores['values'][3]}</td>
                <td>{Valores['values'][4]}</td>
                <td>{Valores['values'][5]}</td>
                <td>{Valores['values'][6]}</td>
                <td>{Valores['values'][7]}</td>
                <td>{Valores['values'][8]}</td>
                <td>{Valores['values'][9]}</td>
                <td>{Valores['values'][10]}</td>
                <td>{Valores['values'][11]}</td>
            
            
            </tbody>
        </table>
        </div>

        </body>
        </html>"""
    if os.path.isdir('FELIZ'):
        
        pass
    else:
        os.system('mkdir C:\FELIZ')
    limpiar()
    imprimir = open(f'C:\\FELIZ\{cedula}.html','w',encoding='utf-8')
    imprimir.write(info)
    imprimir.close()
    webbrowser.open(f'C:\\FELIZ\{cedula}.html')

def video():
    webbrowser.open('https://youtu.be/hPCq_9l-D08')
#ELIMANACION DE ETIQUETAS DE ERRORES

def eliminarErroresActividad():
   
    try:
        errorActividad1.destroy()
    except:
        pass
    try:
        errorActividad2.destroy()
    except:
        pass
    try:
        errorActividad3.destroy()
    except:
        pass
    try:
        errorActividad4.destroy()
    except:
        pass
    try:
        errorActividad5.destroy()
    except:
        pass
    try:
        errorActividad6.destroy()
    except:
        pass
    try:
        errorActividad7.destroy()
    except:
        pass
    try:
        DatosCorrectos.destroy()
    except:
        pass

def eliminarErroresAgregar():
   
    try:
        errorAgregar1.destroy()
    except:
        pass
    try:
        errorAgregar2.destroy()
    except:
        pass
    try:
        errorAgregar3.destroy()
    except:
        pass
    try:
        errorAgregar4.destroy()
    except:
        pass
    try:
        errorAgregar5.destroy()
    except:
        pass
    try:
        errorAgregar6.destroy()
    except:
        pass
    try:
        errorAgregar7.destroy()
    except:
        pass
    try:
        errorAgregar8.destroy()
    except:
        pass
    try:
        errorAgregar9.destroy()
    except:
        pass
    try:
        errorAgregar10.destroy()
    except:
        pass
    try:
        errorAgregar11.destroy()
    except:
        pass
    try:
        errorAgregar12.destroy()
    except:
        pass
    try:
        DatosAgregados.destroy()
    except:
        pass
    
def eliminarErroresModificar():
   
    try:
        errorModificar1.destroy()
    except:
        pass
    try:
        errorModificar2.destroy()
    except:
        pass
    try:
        errorModificar3.destroy()
    except:
        pass
    try:
        errorModificar4.destroy()
    except:
        pass
    try:
        errorModificar5.destroy()
    except:
        pass
    try:
        errorModificar6.destroy()
    except:
        pass
    try:
        errorModificar7.destroy()
    except:
        pass
    try:
        errorModificar8.destroy()
    except:
        pass
    try:
        errorModificar9.destroy()
    except:
        pass
    try:
        errorModificar10.destroy()
    except:
        pass
    try:
        errorModificar11.destroy()
    except:
        pass
    try:
        errorModificar12.destroy()
    except:
        pass
    try:
        DatosAgregadosM.destroy()
    except:
        pass

#VENTANA 2
def GestionarCiclistas():
    global ventana2
    
    ventana.withdraw()
    
    ventana2= Toplevel()
    ventana2.title('Menu Gestionar Ciclistas')
    ventana2.geometry('1366x768')
    contenedor = Frame(ventana2)
    contenedor.pack(pady =20, padx=20)
    
    #ETIQUETAS
    MenuGestianarCiclistas = Label(contenedor, text='Menu Gestionar Ciclistas', font= 'bold').grid(row= 0, column=2,pady=(100,20))
    #BOTONES
    BotonAgregar = Button(contenedor, text='Agregar',font = 'bold',width=20,command=Agregar).grid(row= 1, column=2,pady=(0,15))
    BotonModificar = Button(contenedor, text='Modificar',font = 'bold',width=20,command=Modificar).grid(row= 2, column=2,pady=(0,15))
    BotonEliminar = Button(contenedor, text='Eliminar',font = 'bold',width=20,command=Eliminar).grid(row= 3, column=2,pady=(0,15))
    BotonMenuPrincipal= Button(contenedor, text='Menu Principal',font = 'bold',width=20,command=abrirVentana).grid(row= 4, column=2,pady=(0,15))

#VENTAN 3 
def Agregar():
       
    global cedula
    global nombre
    global apellido
    global fechaNacimiento
    global tipoSangre
    global sizeBici 
    global sizeUniforme
    global telefono
    global celular
    global email
    global direccion
    global personaContacto
    global telPersonaContacto 
    global contenedor3
    
    
    ventana.withdraw()
    ventana2.withdraw()
    global ventana3
    ventana3= Toplevel()
    ventana3.title('Agregar')
    ventana3.geometry('1366x768')
    contenedor3 = Frame(ventana3)
    contenedor3.pack(pady =100, padx=20)
    
    #ETIQUETA


    Label(contenedor3, text='Cedula' ,font='bold').grid(row=1,column=1,sticky=W)
    Label(contenedor3, text='Nombre' ,font='bold').grid(row=1,column=2,sticky=W)
    Label(contenedor3, text='Apellido' ,font='bold').grid(row=4,column=1,sticky=W)
    Label(contenedor3, text='Fecha de Nacimiento (DD/MM/AAAA)' ,font='bold').grid(row=4,column=2,sticky=W)
    Label(contenedor3, text='Tipo de Sangre' ,font='bold').grid(row=7,column=1,sticky=W)
    Label(contenedor3, text='Size de Bicicleta' ,font='bold').grid(row=7,column=2,sticky=W)
    Label(contenedor3, text='Size de Uniforme' ,font='bold').grid(row=10,column=1,sticky=W)
    Label(contenedor3, text='Telefono' ,font='bold').grid(row=10,column=2,sticky=W)
    Label(contenedor3, text='Celular' ,font='bold').grid(row=13,column=1,sticky=W)
    Label(contenedor3, text='Email' ,font='bold').grid(row=13,column=2,sticky=W)
    Label(contenedor3, text='Direccion' ,font='bold').grid(row=16,column=1,sticky=W)
    Label(contenedor3, text='Persona de Contacto' ,font='bold').grid(row=16,column=2,sticky=W)
    Label(contenedor3, text='Tel. de la Persona de Contacto' ,font='bold').grid(row=19,column=1,columnspan=2)
    
    #ENTRADA DE DATOS
    
    cedula = Entry(contenedor3,width=25, font = 'bold')
    cedula.grid(row=2,column=1,sticky=W, pady=(0,10),padx=(0,25))
    nombre = Entry(contenedor3,width=25, font = 'bold')
    nombre.grid(row=2,column=2,sticky=W, pady=(0,10),padx=(0,25))
    apellido = Entry(contenedor3,width=25, font = 'bold')
    apellido.grid(row=5,column=1,sticky=W, pady=(0,10),padx=(0,25))
    fechaNacimiento = Entry(contenedor3,width=25, font = 'bold')
    fechaNacimiento.grid(row=5,column=2,sticky=W, pady=(0,10),padx=(0,25))
    tipoSangre = Entry(contenedor3,width=25, font = 'bold')
    tipoSangre.grid(row=8,column=1,sticky=W, pady=(0,10),padx=(0,25))
    sizeBici = Entry(contenedor3,width=25, font = 'bold')
    sizeBici.grid(row=8,column=2,sticky=W, pady=(0,10),padx=(0,25))
    sizeUniforme = Entry(contenedor3,width=25, font = 'bold')
    sizeUniforme.grid(row=11,column=1,sticky=W, pady=(0,10),padx=(0,25))
    telefono = Entry(contenedor3,width=25, font = 'bold')
    telefono.grid(row=11,column=2,sticky=W, pady=(0,10),padx=(0,25))
    celular = Entry(contenedor3,width=25, font = 'bold')
    celular.grid(row=14,column=1,sticky=W, pady=(0,10),padx=(0,25))
    email = Entry(contenedor3,width=25, font = 'bold')
    email.grid(row=14,column=2,sticky=W, pady=(0,10),padx=(0,25))
    direccion = Entry(contenedor3,width=25, font = 'bold')
    direccion.grid(row=17,column=1,sticky=W, pady=(0,10),padx=(0,25))
    personaContacto = Entry(contenedor3,width=25, font = 'bold')
    personaContacto.grid(row=17,column=2,sticky=W, pady=(0,10),padx=(0,25))
    telPersonaContacto = Entry(contenedor3,width=25, font = 'bold')
    telPersonaContacto.grid(row=20,column=1, pady=(0,10),columnspan=2)

    #BOTON
    
    BotonAtras= Button(contenedor3, text='Atras',font = 'bold',width=20, command=abrirVentana2).grid(row=22, column=1)
    BotonAgregar= Button(contenedor3, text='Agregar',font = 'bold',width=20, command=GuardarAgregado).grid(row=22, column=2)

    
#VENTANA 4    
def Modificar():
    
   
    global ventana4
    global contenedor4
    
    ventana2.withdraw()
    
    ventana4= Toplevel()
    ventana4.title('Modificar')
    ventana4.geometry('1366x768')
    contenedor4 = Frame(ventana4)
    contenedor4.pack()
    
    #ETIQUETAS
    
    
    #TABLA
    global tabla
    tablaFrame = Frame(contenedor4)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla.pack()
    tablaScroll.config(command=tabla.yview)

    tabla['column']=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11')
    tabla.column('#0',width=75,anchor =W)
    tabla.column('#1',width=75,anchor =W)
    tabla.column('#2',width=75,anchor =W)
    tabla.column('#3',width=125,anchor =W)
    tabla.column('#4',width=90,anchor =W)
    tabla.column('#5',width=90,anchor =W)
    tabla.column('#6',width=100,anchor =W)
    tabla.column('#7',width=75,anchor =W)
    tabla.column('#8',width=75,anchor =W)
    tabla.column('#9',width=125,anchor =W)
    tabla.column('#10',width=75,anchor =W)
    tabla.column('#11',width=75,anchor =W)
    tabla.column('#12',width=75,anchor =W)
    

    tabla.heading('#0',text='Cédula',anchor= W)
    tabla.heading('#1',text='Nombre',anchor= W)
    tabla.heading('#2',text='Apellido',anchor= W)
    tabla.heading('#3',text='Fecha de Nacimiento',anchor= W)
    tabla.heading('#4',text='Tipo de Sangre',anchor= W)
    tabla.heading('#5',text='Size Bicicleta',anchor= W)
    tabla.heading('#6',text='Sise Uniforme',anchor= W)
    tabla.heading('#7',text='Teléfono',anchor= W)
    tabla.heading('#8',text='Celular',anchor= W)
    tabla.heading('#9',text='Email',anchor= W)
    tabla.heading('#10',text='Dirección',anchor= W)
    tabla.heading('#11',text='Persona de Contacto',anchor= W)
    tabla.heading('#12',text='Tel. Persona de Contacto',anchor= W)
    
    
    Registro = cursor.execute('select * from Ciclistas')
    VerificarTabla = []
    
    for Ciclista in Registro:
        tabla.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Ciclista[3],Ciclista[4],Ciclista[5],Ciclista[6],Ciclista[7],Ciclista[8],Ciclista[9],Ciclista[10],Ciclista[11],Ciclista[12]))
        VerificarTabla.append(Ciclista)
    #ETIQUETAS
    Titulo= Label(contenedor4,text = 'SELECIONE EL CICLISTA QUE QUIERE MODIFICAR',font='bold').grid(row=0, column=1,pady=(0,30))
    
    #BOTONES
   
    BotonAtras= Button(contenedor4, text='Atras',font = 'bold',width=20, command=abrirVentana2).grid(row=17,column=0,pady=20)
    BotonSelecionar= Button(contenedor4, text='Selecionar',font = 'bold',width=20, command=SelecionarModificar)
    BotonSelecionar.grid(row=17,column=1,pady=20)
    global BotonrGuadar
    BotonrGuadar= Button(contenedor4, text='Guardar',font = 'bold',width=20, command= GuadarModificar,state=DISABLED)
    BotonrGuadar.grid(row=17,column=2,pady=20)
    if VerificarTabla == []:
        BotonSelecionar.config(state=DISABLED)
    



    Label(contenedor4, text='Cedula' ,font='bold').grid(row=3,column=0,sticky=W)
    Label(contenedor4, text='Nombre' ,font='bold').grid(row=3,column=1,sticky=W)
    Label(contenedor4, text='Apellido' ,font='bold').grid(row=3,column=2,sticky=W)
    Label(contenedor4, text='Fecha de Nacimiento (DD/MM/AAAA)' ,font='bold').grid(row=6,column=0,sticky=W)
    Label(contenedor4, text='Tipo de Sangre' ,font='bold').grid(row=6,column=1,sticky=W)
    Label(contenedor4, text='Size de Bicicleta' ,font='bold').grid(row=6,column=2,sticky=W)
    Label(contenedor4, text='Size de Uniforme' ,font='bold').grid(row=9,column=0,sticky=W)
    Label(contenedor4, text='Telefono' ,font='bold').grid(row=9,column=1,sticky=W)
    Label(contenedor4, text=' Celular' ,font='bold').grid(row=9,column=2,sticky=W)
    Label(contenedor4, text='Email' ,font='bold').grid(row=12,column=0,sticky=W)
    Label(contenedor4, text='Direccion' ,font='bold').grid(row=12,column=1,sticky=W)
    Label(contenedor4, text='Persona de Contacto' ,font='bold').grid(row=12,column=2,sticky=W)
    Label(contenedor4, text='Tel. de la Persona de Contacto' ,font='bold').grid(row=15,column=1,sticky=W)
    
    #ENTRADA DE DATOS
    
    global cedulaM
    global nombreM
    global apellidoM
    global fechaNacimientoM
    global tipoSangreM
    global sizeBiciM
    global sizeUniformeM
    global telefonoM
    global celularM
    global emailM
    global direccionM
    global personaContactoM
    global telPersonaContactoM
    
    cedulaM = Entry(contenedor4, font = 'bold',width=25)
    cedulaM.grid(row=4,column=0, pady=(0,5),padx=(0,25),sticky=W)
    nombreM = Entry(contenedor4,width=25, font = 'bold')
    nombreM.grid(row=4,column=1, pady=(0,5),padx=(0,25),sticky=W)
    apellidoM = Entry(contenedor4,width=25, font = 'bold')
    apellidoM.grid(row=4,column=2, pady=(0,5),padx=(0,25),sticky=W)
    fechaNacimientoM = Entry(contenedor4,width=25, font = 'bold')
    fechaNacimientoM.grid(row=7,column=0, pady=(0,5),padx=(0,25),sticky=W)
    tipoSangreM = Entry(contenedor4,width=25, font = 'bold')
    tipoSangreM.grid(row=7,column=1, pady=(0,5),padx=(0,25),sticky=W)
    sizeBiciM = Entry(contenedor4,width=25, font = 'bold')
    sizeBiciM.grid(row=7,column=2, pady=(0,5),padx=(0,25),sticky=W)
    sizeUniformeM = Entry(contenedor4,width=25, font = 'bold')
    sizeUniformeM.grid(row=10,column=0, pady=(0,5),padx=(0,25),sticky=W)
    telefonoM = Entry(contenedor4,width=25, font = 'bold')
    telefonoM.grid(row=10,column=1, pady=(0,5),padx=(0,25),sticky=W)
    celularM = Entry(contenedor4,width=25, font = 'bold')
    celularM.grid(row=10,column=2, pady=(0,5),padx=(0,25),sticky=W)
    emailM = Entry(contenedor4,width=25, font = 'bold')
    emailM.grid(row=13,column=0, pady=(0,5),padx=(0,25),sticky=W)
    direccionM = Entry(contenedor4,width=25, font = 'bold')
    direccionM.grid(row=13,column=1, pady=(0,5),padx=(0,25),sticky=W)
    personaContactoM = Entry(contenedor4,width=25, font = 'bold')
    personaContactoM.grid(row=13,column=2, pady=(0,5),padx=(0,25),sticky=W)
    telPersonaContactoM = Entry(contenedor4,width=25, font = 'bold')
    telPersonaContactoM.grid(row=16,column=1, pady=(0,5),sticky=W)

#VENTANA 5
def Eliminar():
    
    global ventana5
    global contenedor5
    
    ventana2.withdraw()
    
    ventana5= Toplevel()
    ventana5.title('Modificar')
    ventana5.geometry('1366x768')
    contenedor5 = Frame(ventana5)
    contenedor5.pack()
    
    #ETIQUETAS
    
    
    #TABLA
    global tabla2
    tablaFrame = Frame(contenedor5)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla2 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla2.pack()
    tablaScroll.config(command=tabla2.yview)

    tabla2['column']=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11')
    tabla2.column('#0',width=75,anchor =W)
    tabla2.column('#1',width=75,anchor =W)
    tabla2.column('#2',width=75,anchor =W)
    tabla2.column('#3',width=125,anchor =W)
    tabla2.column('#4',width=90,anchor =W)
    tabla2.column('#5',width=90,anchor =W)
    tabla2.column('#6',width=100,anchor =W)
    tabla2.column('#7',width=75,anchor =W)
    tabla2.column('#8',width=75,anchor =W)
    tabla2.column('#9',width=125,anchor =W)
    tabla2.column('#10',width=75,anchor =W)
    tabla2.column('#11',width=75,anchor =W)
    tabla2.column('#12',width=75,anchor =W)
    
    


    tabla2.heading('#0',text='Cédula',anchor= W)
    tabla2.heading('#1',text='Nombre',anchor= W)
    tabla2.heading('#2',text='Apellido',anchor= W)
    tabla2.heading('#3',text='Fecha de Nacimiento',anchor= W)
    tabla2.heading('#4',text='Tipo de Sangre',anchor= W)
    tabla2.heading('#5',text='Size Bicicleta',anchor= W)
    tabla2.heading('#6',text='Sise Uniforme',anchor= W)
    tabla2.heading('#7',text='Teléfono',anchor= W)
    tabla2.heading('#8',text='Celular',anchor= W)
    tabla2.heading('#9',text='Email',anchor= W)
    tabla2.heading('#10',text='Dirección',anchor= W)
    tabla2.heading('#11',text='Persona de Contacto',anchor= W)
    tabla2.heading('#12',text='Tel. Persona de Contacto',anchor= W)
    
    
    Registro = cursor.execute('select * from Ciclistas')
    VerificarTabla = []

    for Ciclista in Registro:
        tabla2.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Ciclista[3],Ciclista[4],Ciclista[5],Ciclista[6],Ciclista[7],Ciclista[8],Ciclista[9],Ciclista[10],Ciclista[11],Ciclista[12]))
        VerificarTabla.append(Ciclista)
        
    #ETIQUETAS
    Titulo= Label(contenedor5,text = 'SELECIONE EL CICLISTA QUE QUIERES ELIMINAR',font='bold').grid(row=0, column=1,pady=30)
    
    #BOTONES
    
        
    
    BotonAtras= Button(contenedor5, text='Atras',font = 'bold',width=20, command=abrirVentana2).grid(row=17,column=0,pady=20)
    BotonSelecionar= Button(contenedor5, text='Selecionar',font = 'bold',width=20, command=SelecionarEliminar)
    BotonSelecionar.grid(row=17,column=1,pady=20)
    global BotonEliminar
    BotonEliminar= Button(contenedor5, text='Eliminar',font = 'bold',width=20, command= EliminarRegistro,state=DISABLED)
    BotonEliminar.grid(row=17,column=2,pady=20)
    if VerificarTabla == []:
        BotonSelecionar.config(state= DISABLED)

#VENTANA 6   
def GestionarActividades():
    global ventana6
    global contenedor6
    
    ventana.withdraw()
   
    
    ventana6= Toplevel()
    ventana6.title('Menu Gestionar Activadades')
    ventana6.geometry('1366x768')
    contenedor6 = Frame(ventana6)
    contenedor6.pack(pady =20, padx=20)
    
    
    #TABLA
    global tabla3
    tablaFrame = Frame(contenedor6)
    tablaFrame.grid( row=1,column=0,columnspan=3,pady=(0,30))

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla3 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla3.pack()
    tablaScroll.config(command=tabla3.yview)

    tabla3['column']=('#0','#1')
    tabla3.column('#0',width=100,anchor =W)
    tabla3.column('#1',width=100,anchor =W)
    tabla3.column('#2',width=100,anchor =W)
    

    tabla3.heading('#0',text='Cédula',anchor= W)
    tabla3.heading('#1',text='Nombre',anchor= W)
    tabla3.heading('#2',text='Apellido',anchor= W)
    
    Registro = cursor.execute('select * from Ciclistas')
    VerificarTabla = []
    
    for Ciclista in Registro:
        tabla3.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2]))
        VerificarTabla.append(Ciclista)
    #ETIQUETAS
    Titulo= Label(contenedor6,text = 'Seleccione el Ciclista de la Actividad',font='bold').grid(row=0, column=0, columnspan=3,pady=(0,30))
    
    #ETIQUETAS
    
    Label(contenedor6, text='Ciclista' ,font='bold').grid(row=2,column=0,sticky=W)
    Label(contenedor6, text='Fecha de la Actividad\n(DD/MM/AAAA)' ,font='bold').grid(row=2,column=1,sticky=W)
    Label(contenedor6, text='Distacia (KM)' ,font='bold').grid(row=2,column=2,sticky=W)
    Label(contenedor6, text='Lugar (Donde ocurrio)' ,font='bold').grid(row=5,column=0,sticky=W)
    Label(contenedor6, text='Latitud' ,font='bold').grid(row=5,column=1,sticky=W)
    Label(contenedor6, text='Longitud' ,font='bold').grid(row=5,column=2,sticky=W)
    Label(contenedor6, text='Dificultad (1,2,3)' ,font='bold').grid(row=8,column=0,columnspan=3)
    
    #ENTRADA DE DATOS
    global CiclistaA
    global fechaActividad
    global Distacia
    global Lugar
    global Latitud
    global Longitud
    global Dificultad
    
    CiclistaA = Entry(contenedor6,width=25, font = 'bold')
    CiclistaA.grid(row=3,column=0,sticky=W, pady=(0,15),padx=(0,25))
    fechaActividad = Entry(contenedor6,width=25, font = 'bold')
    fechaActividad.grid(row=3,column=1,sticky=W, pady=(0,15),padx=(0,25))
    Distacia  = Entry(contenedor6,width=25, font = 'bold')
    Distacia .grid(row=3,column=2,sticky=W, pady=(0,15),padx=(0,25))
    Lugar = Entry(contenedor6,width=25, font = 'bold')
    Lugar.grid(row=6,column=0,sticky=W, pady=(0,15),padx=(0,25))
    Latitud = Entry(contenedor6,width=25, font = 'bold')
    Latitud.grid(row=6,column=1,sticky=W, pady=(0,15),padx=(0,25))
    Longitud = Entry(contenedor6,width=25, font = 'bold')
    Longitud.grid(row=6,column=2,sticky=W, pady=(0,15),padx=(0,25))
    Dificultad = Entry(contenedor6,width=25, font = 'bold')
    Dificultad.grid(row=9,column=0,columnspan=3, pady=(0,15),padx=(0,25))


    #BOTON
    
    BotonAtras= Button(contenedor6, text='Atras',font = 'bold',width=20, command=abrirVentana).grid(row=12, column=0)
    BotonSelecionarActividad= Button(contenedor6, text='Selecionar',font = 'bold',width=20, command=SelecionarActividad)
    BotonSelecionarActividad.grid(row=12, column=1)
    BotonAgregar= Button(contenedor6, text='Agregar',font = 'bold',width=20, command=GuardarActividad)
    BotonAgregar.grid(row=12, column=2)
    
    if VerificarTabla ==[]:
        BotonSelecionarActividad.config(state=DISABLED)
        BotonAgregar.config(state=DISABLED)
        
#VENTANA 7
def Reportes():          
    global ventana7
    try:
        ventana.withdraw()
    except:
        pass
    try:
        ventana8.withdraw()
    except:
        pass
    try:
        ventana9.withdraw()
    except:
        pass
    try:
        ventana10.withdraw()
    except:
        pass
    try:
        ventana11.withdraw()
    except:
        pass
        
        
    
    ventana7= Toplevel()
    ventana7.title('Reportes')
    ventana7.geometry('1366x768')
    contenedor7 = Frame(ventana7)
    contenedor7.pack(pady =20, padx=20)
    
    #ETIQUETAS
    MenuGestianarCiclistas = Label(contenedor7, text='Menu Reportes', font= 'bold').grid(row= 0, column=2,pady=(100,20))
    #BOTONES
    BotonListaCiclistas = Button(contenedor7, text='Lista de Ciclistas',font = 'bold',width=20,command=ListaCiclista).grid(row= 1, column=2,pady=(0,15))
    BotonListaActividad = Button(contenedor7, text='Lista de Actividades ',font = 'bold',width=20,command=ListaActividad).grid(row= 2, column=2,pady=(0,15))
    BotonListaCiclistasZodiaco = Button(contenedor7, text='L.C. con Signo Zodiacal',font = 'bold',width=20,command=ListaCiclistaZodiaco).grid(row= 3, column=2,pady=(0,15))
    BotonExportar= Button(contenedor7, text='Exportar',font = 'bold',width=20,command=Exportar).grid(row= 4, column=2,pady=(0,15))
    BotonMapa= Button(contenedor7, text='Mapa',font = 'bold',width=20,command=Mapa)
    BotonMapa.grid(row= 5, column=2,pady=(0,15))
    BotonMenuPrincipal= Button(contenedor7, text='Menu Principal',font = 'bold',width=20,command=abrirVentana).grid(row= 6, column=2,pady=(0,15))
    
    #VERIFICANDO SI HAY DATOS EN LA BASE DE DATOS PARA HABLITAR O DESHABILITAR EL BOTON DEL MAPA
    verificador = []
    todasActividades = cursor.execute('select * from RegistroActividad')
    for actividad in todasActividades:
        verificador.append(actividad)
    
    if verificador == []:
        BotonMapa.config(state=DISABLED)
            
    
#VENTANA 8
def ListaCiclista():
    global ventana8
    
    ventana7.withdraw()
    ventana8= Toplevel()
    ventana8.title('Menu Gestionar Activadades')
    ventana8.geometry('1366x768')
    contenedor8 = Frame(ventana8)
    contenedor8.pack(pady =20, padx=20)
    
    #TABLA
    global tabla4
    tablaFrame = Frame(contenedor8)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla4 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla4.pack()
    tablaScroll.config(command=tabla4.yview)

    tabla4['column']=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11')
    tabla4.column('#0',width=75,anchor =W)
    tabla4.column('#1',width=75,anchor =W)
    tabla4.column('#2',width=75,anchor =W)
    tabla4.column('#3',width=125,anchor =W)
    tabla4.column('#4',width=90,anchor =W)
    tabla4.column('#5',width=90,anchor =W)
    tabla4.column('#6',width=100,anchor =W)
    tabla4.column('#7',width=75,anchor =W)
    tabla4.column('#8',width=75,anchor =W)
    tabla4.column('#9',width=125,anchor =W)
    tabla4.column('#10',width=75,anchor =W)
    tabla4.column('#11',width=75,anchor =W)
    tabla4.column('#12',width=75,anchor =W)
    
    


    tabla4.heading('#0',text='Cédula',anchor= W)
    tabla4.heading('#1',text='Nombre',anchor= W)
    tabla4.heading('#2',text='Apellido',anchor= W)
    tabla4.heading('#3',text='Fecha de Nacimiento',anchor= W)
    tabla4.heading('#4',text='Tipo de Sangre',anchor= W)
    tabla4.heading('#5',text='Size Bicicleta',anchor= W)
    tabla4.heading('#6',text='Sise Uniforme',anchor= W)
    tabla4.heading('#7',text='Teléfono',anchor= W)
    tabla4.heading('#8',text='Celular',anchor= W)
    tabla4.heading('#9',text='Email',anchor= W)
    tabla4.heading('#10',text='Dirección',anchor= W)
    tabla4.heading('#11',text='Persona de Contacto',anchor= W)
    tabla4.heading('#12',text='Tel. Persona de Contacto',anchor= W)
    
    
    Registro = cursor.execute('select * from Ciclistas')
    
    
    for Ciclista in Registro:
        tabla4.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Ciclista[3],Ciclista[4],Ciclista[5],Ciclista[6],Ciclista[7],Ciclista[8],Ciclista[9],Ciclista[10],Ciclista[11],Ciclista[12]))
        
    #ETIQUETAS
    Titulo= Label(contenedor8,text = 'Lista de Ciclistas',font='bold').grid(row=0, column=1,pady=(120,30)) 
    
    #BOTON
    Atras = Button(contenedor8,text = 'Atras',font='bold',width=25, command=Reportes).grid(row=2, column=0,pady=30, columnspan=3)  
        
#VENTANA 9
def ListaActividad():
    global ventana9
    
    ventana7.withdraw()
    ventana9= Toplevel()
    ventana9.title('Menu Gestionar Activadades')
    ventana9.geometry('1366x768')
    contenedor9 = Frame(ventana9)
    contenedor9.pack(pady =20, padx=20)
    
    #TABLA
    global tabla5
    tablaFrame = Frame(contenedor9)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla5 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla5.pack()
    tablaScroll.config(command=tabla5.yview)

    tabla5['column']=('#0','#1','#2','#3','#4','#5','#6')
    tabla5.column('#0',width=100,anchor =W)
    tabla5.column('#1',width=75,anchor =W)
    tabla5.column('#2',width=125,anchor =W)
    tabla5.column('#3',width=75,anchor =W)
    tabla5.column('#4',width=90,anchor =W)
    tabla5.column('#5',width=90,anchor =W)
    tabla5.column('#6',width=100,anchor =W)
    tabla5.column('#7',width=75,anchor =W)

    tabla5.heading('#0',text='Cédula',anchor= W)
    tabla5.heading('#1',text='Ciclista',anchor= W)
    tabla5.heading('#2',text='Fecha de la Actividad',anchor= W)
    tabla5.heading('#3',text='Distancia',anchor= W)
    tabla5.heading('#4',text='Lugar',anchor= W)
    tabla5.heading('#5',text='Latitud',anchor= W)
    tabla5.heading('#6',text='Longitud',anchor= W)
    tabla5.heading('#7',text='Dificultad',anchor= W)
   
    
    
    
    Registro = cursor.execute('select * from RegistroActividad')
    
    
    for Ciclista in Registro:
        tabla5.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Ciclista[3],Ciclista[4],Ciclista[5],Ciclista[6],Ciclista[7]))
        
    #ETIQUETAS
    Titulo= Label(contenedor9,text = 'Lista de Actividades',font='bold').grid(row=0, column=1,pady=(120,30)) 
    
    #BOTON
    Atras = Button(contenedor9,text = 'Atras',font='bold',width=25, command=Reportes).grid(row=2, column=0,pady=30, columnspan=3)  
        
#VENTANA 10
def ListaCiclistaZodiaco():
    global ventana10
    
    ventana7.withdraw()
    ventana10= Toplevel()
    ventana10.title('Menu Gestionar Activadades')
    ventana10.geometry('1366x768')
    contenedor10 = Frame(ventana10)
    contenedor10.pack(pady =20, padx=20)
    
    #TABLA
    global tabla6
    tablaFrame = Frame(contenedor10)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla6 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla6.pack()
    tablaScroll.config(command=tabla6.yview)

    tabla6['column']=('#0','#1','#2')
    tabla6.column('#0',width=100,anchor =W)
    tabla6.column('#1',width=75,anchor =W)
    tabla6.column('#2',width=75,anchor =W)
    tabla6.column('#3',width=100,anchor =W)
    


    tabla6.heading('#0',text='Cédula',anchor= W)
    tabla6.heading('#1',text='Nombre',anchor= W)
    tabla6.heading('#2',text='Apellido',anchor= W)
    tabla6.heading('#3',text='Signo Zodiacal',anchor= W)
 
    
    
    Registro = cursor.execute('select * from Ciclistas')
   
    
    for Ciclista in Registro:
        tabla6.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Zodiaco[f"{Ciclista[3][5:10]}"]))
        
        
        
  
    #ETIQUETAS
    Titulo = Label(contenedor10,text = 'Lista de Ciclistas',font='bold').grid(row=0, column=1,pady=(120,30)) 
    
    #BOTON
    Atras = Button(contenedor10,text = 'Atras',font='bold',width=25, command=Reportes).grid(row=2, column=0,pady=30, columnspan=3)  

#VENTANA 11
def Exportar():
    global ventana11
    
    ventana7.withdraw()
    ventana11= Toplevel()
    ventana11.title('Lista de Ciclistas')
    ventana11.geometry('1366x768')
    contenedor11 = Frame(ventana11)
    contenedor11.pack(pady =20, padx=20)
    
    #TABLA
    global tabla7
    tablaFrame = Frame(contenedor11)
    tablaFrame.grid( row=1,column=0,columnspan=3)

    tablaScroll = Scrollbar(tablaFrame)
    tablaScroll.pack(side=RIGHT, fill=Y)

    tabla7 = ttk.Treeview(tablaFrame, yscrollcommand=tablaScroll.set)
    tabla7.pack()
    tablaScroll.config(command=tabla7.yview)

    tabla7['column']=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11')
    tabla7.column('#0',width=75,anchor =W)
    tabla7.column('#1',width=75,anchor =W)
    tabla7.column('#2',width=75,anchor =W)
    tabla7.column('#3',width=125,anchor =W)
    tabla7.column('#4',width=90,anchor =W)
    tabla7.column('#5',width=90,anchor =W)
    tabla7.column('#6',width=100,anchor =W)
    tabla7.column('#7',width=75,anchor =W)
    tabla7.column('#8',width=75,anchor =W)
    tabla7.column('#9',width=125,anchor =W)
    tabla7.column('#10',width=75,anchor =W)
    tabla7.column('#11',width=75,anchor =W)
    tabla7.column('#12',width=75,anchor =W)
    

    tabla7.heading('#0',text='Cédula',anchor= W)
    tabla7.heading('#1',text='Nombre',anchor= W)
    tabla7.heading('#2',text='Apellido',anchor= W)
    tabla7.heading('#3',text='Fecha de Nacimiento',anchor= W)
    tabla7.heading('#4',text='Tipo de Sangre',anchor= W)
    tabla7.heading('#5',text='Size Bicicleta',anchor= W)
    tabla7.heading('#6',text='Sise Uniforme',anchor= W)
    tabla7.heading('#7',text='Teléfono',anchor= W)
    tabla7.heading('#8',text='Celular',anchor= W)
    tabla7.heading('#9',text='Email',anchor= W)
    tabla7.heading('#10',text='Dirección',anchor= W)
    tabla7.heading('#11',text='Persona de Contacto',anchor= W)
    tabla7.heading('#12',text='Tel. Persona de Contacto',anchor= W)
    
    
    Registro = cursor.execute('select * from Ciclistas')
    
    verificarListaActividad = []
    for Ciclista in Registro:
        tabla7.insert('',END,text=Ciclista[0],values=(Ciclista[1],Ciclista[2],Ciclista[3],Ciclista[4],Ciclista[5],Ciclista[6],Ciclista[7],Ciclista[8],Ciclista[9],Ciclista[10],Ciclista[11],Ciclista[12]))
        verificarListaActividad.append(Ciclista)
    
    #BOTONES
   
    Atras = Button(contenedor11,text = 'Atras',font='bold',width=25, command=Reportes).grid(row=17, column=0,pady=30,sticky=E )  
    BotonSelecionar= Button(contenedor11, text='Selecionar',font = 'bold',width=25, command=SelecionarExportar)
    BotonSelecionar.grid(row=17,column=2,pady=30,sticky = W)
    
    if verificarListaActividad == []:
        BotonSelecionar.config(state = DISABLED)
  
    #ETIQUETAS
    Titulo = Label(contenedor11,text = 'Lista de Ciclistas',font='bold').grid(row=0, column=0,pady=(120,30),columnspan=3) 


def Mapa():
    
    ciclistas = cursor.execute('SELECT * FROM  RegistroActividad')
    Mapa = folium.Map(location=[18.8748284,-71.4276553], zoom_start= 8, title= 'República Dominicana')
    for ciclista in ciclistas:
        folium.Marker(location=[ciclista[5],ciclista[6]],tooltip='Ver Información',popup=ciclista[1]).add_to(Mapa)
    Mapa.save('Mapa.html','w')
    webbrowser.open('Mapa.html')
           
def Salir():
    ventana.destroy()  
    
def fechaSignoZodiacales (inicio,fin,mes,signo):
    diccionario = {}
    if len(str(mes)) == 1:   
        if mes == 9:
            for dia in range(inicio,32):
                diccionario[str(mes)+'-'+str(dia)]= signo
            for dia in range(1,10):
                diccionario[str(mes+1)+'0-'+str(dia)]= signo
            for dia in range(10,fin+1):
                diccionario[str(mes+1)+'-'+str(dia)]= signo
     
                
        else:
            for dia in range(inicio,32):
                diccionario['0'+str(mes)+'-'+str(dia)]= signo
            for dia in range(1,10):
                diccionario['0'+str(mes+1)+'-0'+str(dia)]= signo
            for dia in range(10,fin+1):
                diccionario['0'+str(mes+1)+'-'+str(dia)]= signo
                
    elif mes == 12:
        
        for dia in range(inicio,32):
            diccionario[str(mes)+'-'+str(dia)]= signo
        for dia in range(1,10):
            diccionario['01'+'-0'+str(dia)]= signo
        for dia in range(10,fin+1):
            diccionario['01'+'-'+str(dia)]= signo
            

    else:
        for dia in range(inicio,32):
            diccionario[str(mes)+'-'+str(dia)]= signo
        for dia in range(1,10):
            diccionario[str(mes+1)+'-0'+str(dia)]= signo
        for dia in range(10,fin+1):
            diccionario[str(mes+1)+'-'+str(dia)]= signo
    return diccionario
        
            
#CREADOR DE DICCIONARIO DE LAS FECHAS DE TODOS LOS SIGNOS ZODIACALES
Zodiaco ={}
Zodiaco.update(fechaSignoZodiacales(21,20,3,'Aries'))
Zodiaco.update(fechaSignoZodiacales(21,20,4,'Tauro'))
Zodiaco.update(fechaSignoZodiacales(21,21,5,'Génesis'))
Zodiaco.update(fechaSignoZodiacales(22,22,6,'Cáncer'))
Zodiaco.update(fechaSignoZodiacales(23,22,7,'Leo'))
Zodiaco.update(fechaSignoZodiacales(23,22,8,'Virgo'))
Zodiaco.update(fechaSignoZodiacales(23,22,9,'Libra'))
Zodiaco.update(fechaSignoZodiacales(23,22,10,'Escorpio'))
Zodiaco.update(fechaSignoZodiacales(23,21,11,'Sagitario'))
Zodiaco.update(fechaSignoZodiacales(22,20,12,'Capricornio'))
Zodiaco.update(fechaSignoZodiacales(21,18,1,'Acuario'))
Zodiaco.update(fechaSignoZodiacales(19,20,2,'Pisis'))      
limpiar()


#VENTANA 1
ventana = Tk()
ventana.title('Exame Final')
ventana.geometry('1366x768')
contenedor = Frame(ventana)
contenedor.pack(pady =20, padx=20)

menu = Label(contenedor, text= 'Menu Principal',font = 'bold', width=50).grid(row= 0, column=2, pady =(100,20) )
BotonGestionarCiclistas = Button(contenedor, text='Gestionar Ciclistas',font = 'bold',width=20,command=GestionarCiclistas).grid(row= 1, column=2,pady=(0,15)) 
BotonGestionarActividades = Button(contenedor, text='Gestionar Actividades',font = 'bold',width=20,command=GestionarActividades).grid(row= 2, column=2,pady=(0,15)) 
BotonReportes = Button(contenedor, text='Reportes',font = 'bold',width=20,command=Reportes).grid(row= 3, column=2,pady=(0,15)) 
BotonAcercaDe = Button(contenedor, text='Acerca De',font = 'bold',width=20, command=video).grid(row= 4, column=2,pady=(0,15)) 
Salir = Button(contenedor, text='Salir',font = 'bold',width=20, command=Salir).grid(row= 5, column=2,pady=(0,15)) 
    
ventana.mainloop()