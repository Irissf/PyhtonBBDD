import sqlite3

#entre paréntesis el nombre de la base de datos
miConexion=sqlite3.connect("PrimeraBase")

#el puntero o cursor-> seria como el statement en Java
miCursor = miConexion.cursor()

#consulta, creamos una tabla con algunos campos
miCursor.execute("create table productos(nombre_articulo varchar(50),prcio integer, seccion varchar(20))")

#insertar datos, si el exteriro del string es con comillas dobles, usar simples en el interior, y a la inversa
miCursor.execute("insert into productos values('camiseta',15,'ropa')")

#meter un lote de registros
variosProductos=[
    ("pantalón",10,"ropa"),
    ("gusanitos",90,"comida"),
    ("jarrón",30,"cerámica")
]

miCursor.executemany("insert into productos values(?,?,?)",variosProductos)

#leer datos
miCursor.execute("select * from productos")

#fetchall->nos devuelve una lista con todos los registro del exexute
datosDelSelect = miCursor.fetchall()
print(datosDelSelect)
for producto in datosDelSelect:
    print("nombre: ",producto[0])

#confirmarmos los cambios que vamos a hacer en la tabla
miConexion.commit()

#Importante cerrarla
miConexion.close()