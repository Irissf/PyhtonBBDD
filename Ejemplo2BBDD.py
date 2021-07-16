import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor() #statement

#creamos tabla, la triple comilla es para dividir la consulta en varios renglones
miCursor.execute('''
    create table productos(
        id integer primary key autoincrement,
        nombre_articulo varchar(50),
        precio integer,
        seccion varchar(20))
''')

#cubrimos los campos
productos = [
    ("fregona", 12,"limpieza"),
    ("jarrón", 145, "cerámica"),
    ("pan", 1,"alimentación"),
    ("carne cerdo", 2,"alimentación")
]

#los insertamos en la tabla, en el null meterá el id autoincremental
miCursor.executemany("insert into productos values (null,?,?,?)",productos)

miConexion.commit()
miConexion.close()