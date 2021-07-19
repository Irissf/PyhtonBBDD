import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor() #statement

miCursor.execute("select * from productos where seccion = 'alimentación'")
#cogemos los productos leidos
productos = miCursor.fetchall()
print(productos)

miConexion.commit()
miConexion.close()