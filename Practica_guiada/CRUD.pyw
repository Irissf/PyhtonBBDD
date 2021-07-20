import sqlite3
from tkinter import *
from tkinter import messagebox
from sqlite3 import *

root = Tk()

#---------------------------FUNCIONES---------------------------

def conexionBBDD():
    miConexion = sqlite3.connect("Practica_guiada/Usuarios")
    miCursor = miConexion.cursor()

    try:
        #lo metemos en un tray ya que si ya está creada la base de datos
        # dará un error al hacerlo de nuevo
        miCursor.execute('''
            create table datosusuario(
            id integer primary key autoincrement,
            nombre_usuario varchar(50),
            password varchar(10),
            apellido varchar(50),
            direccion varchar(50),
            comentarios varchar(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    
    except:
        messagebox.showwarning("Atención", "La base de datos ya existe")
   
def salirAplicacion():
    #guardamos el valor de la respuesta del ususario del askquestion
    valor = messagebox.askquestion("Salir", "¿Desear cerrar la aplicación?")
    if valor == "yes":
        root.destroy()

def limpiarCmpos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    #que borre delsde el primer caracter hasta el último
    textoCOmentario.delete(1.0,END)

def crearRegistro():
    miConexion = sqlite3.connect("Practica_guiada/Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("insert into datosusuario values(NULL, '"+miNombre.get()+
        "','" +miPass.get() +
        "','" +miApellido.get() +
        "','" + miDireccion.get()+
        "','" + textoCOmentario.get("1.0", END) +"')")
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leerRegistro():
    miConexion = sqlite3.connect("Practica_guiada/Usuarios")
    miCursor = miConexion.cursor()
    
    miCursor.execute("select * from datosusuario where id="+miId.get())
    usuarioDatos = miCursor.fetchall()
    for usuario in usuarioDatos:
        #en 0 está el id, en 1 el nombre...
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoCOmentario.insert(1.0,usuario[5])

    miConexion.commit()

def modificarRegistro():
    miConexion = sqlite3.connect("Practica_guiada/Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("update datosusuario set nombre_usuario= '"+miNombre.get()+
        "', password='" +miPass.get() +
        "', apellido='" +miApellido.get() +
        "', direccion='" + miDireccion.get()+
        "', comentarios='" + textoCOmentario.get("1.0", END) +
        "' where id="+miId.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro modificado")

def borrarRegistro():
    miConexion = sqlite3.connect("Practica_guiada/Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("delete from datosusuario where id="+miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro eliminado")

#---------------------------MENU---------------------------------
barraMenu = Menu(root)
root.config(menu = barraMenu, width=300,height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCmpos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearRegistro)
crudMenu.add_command(label="Leer", command=leerRegistro)
crudMenu.add_command(label="Actualizar", command=modificarRegistro)
crudMenu.add_command(label="Borrar", command=borrarRegistro)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#---------------------------FORMULARIO----------------------------
miFrame = Frame(root)
miFrame.pack()

#variables para los valores del formulario
miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()


labelID = Label(miFrame, text="Id:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)
cuadroId = Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0,column=1,padx=10, pady=10)

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10, pady=10)

labelPass = Label(miFrame, text="Contraseña:")
labelPass.grid(row=2, column=0, sticky="e", padx=10, pady=10)
cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10, pady=10)
cuadroPass.config(show="❤")

labelApellido = Label(miFrame, text="Apellidos:")
labelApellido.grid(row=3, column=0, sticky="e", padx=10, pady=10)
cuadroApellido = Entry(miFrame, textvariable= miApellido)
cuadroApellido.grid(row=3,column=1,padx=10, pady=10)

labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)
cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10, pady=10)

labelComentario = Label(miFrame, text="Comentario:")
labelComentario.grid(row=5, column=0, sticky="e", padx=10, pady=10)
textoCOmentario = Text(miFrame, width=16, height=5)
textoCOmentario.grid(row=5,column=1,padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=textoCOmentario.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew")
textoCOmentario.config(yscrollcommand=scrollVertical)

#-----------------------------BOTONES-----------------------------

frameBotones = Frame(root)
frameBotones.pack()

botonCrear = Button(frameBotones, text="Crear", command=crearRegistro)
botonCrear.grid(row=0, column=0,sticky="e", padx=10, pady=10)

botonLeer = Button(frameBotones, text="Leer", command=leerRegistro)
botonLeer.grid(row=0, column=1,sticky="e", padx=10, pady=10)

botonActualizar = Button(frameBotones, text="Actualizar",command=modificarRegistro)
botonActualizar.grid(row=0, column=2,sticky="e", padx=10, pady=10)

botonBorrar = Button(frameBotones, text="Borrar", command=borrarRegistro)
botonBorrar.grid(row=0, column=3,sticky="e", padx=10, pady=10)


root.mainloop()