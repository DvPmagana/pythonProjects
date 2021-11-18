import sqlite3
from sqlite3.dbapi2 import Cursor

conexion=sqlite3.connect('agenda.db')
cursor=conexion.cursor()


def eliminar_tablaUsuario():
	cursor.execute("DROP TABLE usuario")
	conexion.commit()
	cursor.close()
	conexion.close()

def crear_tablaAgenda():
	cursor.execute("CREATE TABLE IF NOT EXISTS usuario(idContacto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idUsuario TEXT,Nombre TEXT,Telefono TEXT ,Direccion TEXT,Email TEXT)")
	conexion.commit()
	cursor.close()
	conexion.close()
 
def crear_tablaUsuario():
	cursor.execute("CREATE TABLE IF NOT EXISTS contactos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombre TEXT,Usuario TEXT,clave TEXT)")
	conexion.commit()
	cursor.close()
	conexion.close()
 

crear_tablaAgenda()
crear_tablaUsuario()

