from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from config import *
import config
import sqlite3


class login(Tk):


    def crearTablalogin(self):
        self.abrirBD()
        try:
            self.conexion.execute("CREATE TABLE usuario(idContacto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idUsuario TEXT,Nombre TEXT,Telefono TEXT ,Direccion TEXT,Email TEXT)")
            self.conexion.commit()
            print("Se ha creado la tabla de Login")
        except sqlite3.OperationalError:
            print('La tabla ya ha sido creada')
        finally:
            self.cursor.close()
            self.conexion.close()


    def __init__(self):
        super().__init__()
        self.geometry('340x100')
        self.resizable(0,0)
        self.title('Login')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=11)
        self.columnconfigure(2,weight=4)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.rowconfigure(4)
        self.rowconfigure(5,weight=1)
        self.crearTablalogin()
        self.abrirBD()
        self.componentes()
        self.inicio()
        
    def abrirBD(self):
        self.conexion=sqlite3.connect('agenda.db')		
        self.cursor=self.conexion.cursor()
        
        
    def componentes(self):
        self.usuario=StringVar()
        self.clave=StringVar()
       
        Label(self,text='Usuario',padx=10,pady=5, anchor='w').grid(column=0,row=0,sticky='we')
        Label(self,text='Clave',padx=10,pady=5, anchor='w').grid(column=0,row=1,sticky='we')

        Entry(self,textvariable=self.usuario).grid(column=1,row=0,sticky='we')
        Entry(self,textvariable=self.clave).grid(column=1,row=1,sticky='we')
        Button(self,text='Ingresar',bg='#A7A8A8',padx=20,pady=1,command=lambda:self.login()).grid(column=1,row=4,sticky='w')
        Button(self,text='Salir',padx=25,pady=1,command=lambda:self.salir()).grid(column=1,row=4,sticky='e')
        #Button(self,text='Registro',bg='#A7A8A8',padx=5,pady=5,command=lambda:self.vRegistro()).grid(column=1,row=4,sticky='w')

    def vAgenda(self):
        self.destroy()
        Agenda()
        
    def vRegistro(self):
        self.destroy()
        registro()

    def salir(self):
        self.destroy()

    def login(self):	
        if(self.idUser() == 2):
            self.destroy()
            registro()
        else:
            usuario=self.usuario.get()		
            clave=self.clave.get()
            self.cursor.execute('SELECT * FROM usuario WHERE Usuario = ? AND clave = ?',(usuario,clave))
            if self.cursor.fetchall():	
                config.idUser = self.idUser(),self.asigNombre(),self.destroy(),Agenda()
            else:
                mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")
        

    def asigNombre(self):
        config.idNombre = self.idNombre()

    def idUser(self):
        sqlite_select_query = """SELECT * from usuario"""
        self.cursor.execute(sqlite_select_query)
        records = self.cursor.fetchall()
        for row in records:
            if(self.usuario.get() == row[2]):
                config.idUser = (row[0])     
        return config.idUser

    def idNombre(self):
        sqlite_select_query = """SELECT * from usuario"""
        self.cursor.execute(sqlite_select_query)
        records = self.cursor.fetchall()
        for row in records:
            if(self.usuario.get() == row[2]):
                config.idNombre = (row[1])     
        return config.idNombre
                    
    
    def inicio(self):
        self.mainloop()

class registro(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('340x190')
        self.resizable(0,0)
        self.title('Registro')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=11)
        self.columnconfigure(2,weight=4)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.rowconfigure(4)
        self.rowconfigure(5,weight=1)
        self.rowconfigure(6,weight=1)
        self.abrirBD()
        self.componentes()
        self.inicio()
        
    def abrirBD(self):
        self.conexion=sqlite3.connect('agenda.db')		
        self.cursor=self.conexion.cursor()

    def cerrarBD(self):
        self.conexion.close
        
        
    def componentes(self):
        self.usuario=StringVar()
        self.clave=StringVar()
        self.cClave=StringVar()
        self.nombre=StringVar()
        
        Label(self,text='Usuario',padx=5,pady=5, anchor='w').grid(column=0,row=0,sticky='we')
        Label(self,text='Clave',padx=5,pady=5, anchor='w').grid(column=0,row=1,sticky='we')
        Label(self,text='Confirmar Clave',padx=5,pady=5, anchor='w').grid(column=0,row=2,sticky='we')
        Label(self,text='Nombre',padx=5,pady=5, anchor='w').grid(column=0,row=3,sticky='we')

        Entry(self,textvariable=self.usuario).grid(column=1,row=0,sticky='we')
        Entry(self,textvariable=self.clave).grid(column=1,row=1,sticky='we')
        Entry(self,textvariable=self.cClave).grid(column=1,row=2,sticky='we')
        Entry(self,textvariable=self.nombre).grid(column=1,row=3,sticky='we')
        Button(self,text='Registrar',bg='#A7A8A8',padx=10,pady=5,command=lambda:self.registrar()).grid(column=1,row=4,sticky='w')
        Button(self,text='Salir',padx=20,pady=5,command=lambda:self.salir()).grid(column=1,row=4,sticky='e')

    def vAgenda(self):
        self.destroy
        ag = Agenda()
    
    def salir(self):
        self.destroy()
        login()

    def registrar(self):			
        usuario = self.usuario.get()
        clave = self.clave.get()
        cClave = self.cClave.get()
        nombre = self.nombre.get()
        if(usuario == "" or clave=="" or cClave == "" or nombre == ""):
            mb.showerror(title="Campos vacios", message="Cuidado, no se aceptan registros de campos vacios")
        else:
            if(clave == cClave):
                self.cursor.execute('INSERT INTO usuario(nombre,usuario,clave) VALUES (?,?,?)',(nombre,usuario,clave))
                self.conexion.commit()
                mb.showinfo(title="Registro Correcto",message="Hola "+nombre+" \nSu registro fue exitoso.")
                self.cerrarBD()
            else:
                mb.showerror(title="Contraseña Incorrecta",message="Error \nLas contraseñas no coinciden.")


    def getAllRows(self):
        try:
            self.abrirBD()
            print("Connectado a Base de datos SQLite")

            sqlite_select_query = """SELECT * from usuario"""
            self.cursor.execute(sqlite_select_query)
            records = self.cursor.fetchall()
            print("Total de renglones:  ", len(records))
            print("Imprimiendo cada renglon")
            for row in records:
                print("Id: ", row[0])
                print("Nombre: ", row[1])
                print("Usuario: ", row[2])
                print("Clave: ", row[3])
                print("\n")

        except sqlite3.Error as error:
            print("Falla en la lectura", error)
        finally:
                self.cerrarBD()
                print("La conexion a Sqlite se ha cerrado")

            
    def inicio(self):
        self.mainloop()

class Agenda(Tk):
    listaTelefonos=[] # lista que almacena el contenido del archivo agenda.txt y se usa para llenar el treeview
    ids=[] # lista que almacena los ids asignados a los elementos del treeview


    def crearTablaAgenda(self):
        self.abrirBD()
        try:
            self.conexion.execute("CREATE TABLE contactos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombre TEXT,Usuario TEXT,clave TEXT)")
            self.conexion.commit()
            print("Se ha creado la tabla de Login")
        except sqlite3.OperationalError:
            print('La tabla ya ha sido creada')
        finally:
            self.cursor.close()
            self.conexion.close()


    def __init__(self):
        super().__init__()
        self.geometry('840x480')
        self.resizable(0,0)
        self.title('Agenda')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=4)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.crearTablaAgenda()
        self.componentes()
        self.cargarDatos()
        self.inicio()

    def abrirBD(self):
        self.conexion=sqlite3.connect('agenda.db')		
        self.cursor=self.conexion.cursor()

    def cerrarBD(self):
        self.conexion.close
    def componentes(self):
        self.idNombre = config.idNombre
        self.nombre=StringVar()
        self.aPaterno=StringVar()
        self.aMaterno=StringVar()
        self.telefono=StringVar()
        self.email=StringVar()
        self.direccion=StringVar()
        
        Label(self,text='Bienvenido!\n'+ str(config.idNombre),font=('Arial',20),padx=5,pady=5, anchor='n').grid(column=2,row=0,rowspan=3,sticky='we')
        Label(self,text='Nombre',padx=5,pady=5, anchor='w').grid(column=0,row=0,sticky='we')
        Label(self,text='Apellido Paterno',padx=5,pady=5, anchor='w').grid(column=0,row=1,sticky='we')
        Label(self,text='Apellido Materno',padx=5,pady=5, anchor='w').grid(column=0,row=2,sticky='we')
        Label(self,text='Telefono',padx=5,pady=5, anchor='w').grid(column=0,row=3,sticky='we')
        Label(self,text='Email',padx=5,pady=5, anchor='w').grid(column=0,row=4,sticky='we')
        Label(self,text='Direccion',padx=5,pady=5, anchor='w').grid(column=0,row=5,sticky='we')
        Button(self,text='Guardar',padx=25,bg='#A7A8A8',command=lambda:self.guardar()).grid(column=2,row=5,sticky='w')
        Button(self,text='Eliminar',bg='#A7A8A8',padx=40,pady=10,command=lambda:self.eliminar()).grid(column=1,row=8,sticky='w')
        Button(self,text='Salir',bg='#A7A8A8',padx=50,pady=10,command=lambda:self.salir()).grid(column=2,row=8,sticky='e')
        Entry(self,textvariable=self.nombre).grid(column=1,row=0)
        Entry(self,textvariable=self.aPaterno).grid(column=1,row=1)
        Entry(self,textvariable=self.aMaterno).grid(column=1,row=2)
        Entry(self,textvariable=self.telefono).grid(column=1,row=3)
        Entry(self,textvariable=self.email).grid(column=1,row=4)
        Entry(self,textvariable=self.direccion).grid(column=1,row=5)
        
        # DEFINIMOS LA ESTRUCTURA Y COMPOSICION DEL TREEVIEW
        self.listado=ttk.Treeview(self, show='headings')
        self.listado['columns']=("Id","Nombre","Telefono","Email","Direccion")
        self.listado.grid(column=0,row=7,columnspan=5,sticky='we',padx=5,pady=5)
        
        self.listado.column("Id", width=30,anchor=CENTER)
        self.listado.column("Nombre", width=30,anchor=CENTER)
        self.listado.column("Telefono", width=30,anchor=CENTER)
        self.listado.column("Email", width=60,anchor=CENTER)
        self.listado.column("Direccion", width=100,anchor=CENTER)
        
        self.listado.heading("Id", text="Id", anchor= CENTER)
        self.listado.heading("Nombre", text="Nombre", anchor= CENTER)
        self.listado.heading("Telefono", text="Telefono", anchor= CENTER)
        self.listado.heading("Email", text="Email", anchor= CENTER)
        self.listado.heading("Direccion", text="Direccion", anchor= CENTER)

    def salir(self):
        self.destroy()
        login()
    
    def guardar(self):
        nombre=self.nombre.get()
        aPaterno=self.aPaterno.get()
        aMaterno=self.aMaterno.get()
        telefono=self.telefono.get()
        email=self.email.get()
        direccion=self.direccion.get()
        if(nombre == "" or aPaterno=="" or aMaterno == "" or email == "" or direccion == ""):
            mb.showerror(title="Campos vacios", message="Cuidado, no se aceptan registros de campos vacios")
        else:
            try:
                self.abrirBD()
                print('Conexion a SQlite exitosa')
                self.cursor.execute('INSERT INTO contactos(idUsuario,Nombre,Telefono,Direccion,Email) VALUES(?,?,?,?,?)',(config.idUser,nombre+" "+aPaterno+" "+aMaterno,telefono,email,direccion))
                self.conexion.commit()
                mb.showinfo(title="Registro Correcto",message="Su registro fue exitoso.")
            except sqlite3.Error as error:
                print("Falla en la lectura", error)
            finally:
                self.eliminarListado()
                self.cargarDatos()
                self.cerrarBD()
                print("La conexion a Sqlite se ha cerrado")


    def cargarDatos(self):
        self.abrirBD()
        print("Connectado a Base de datos SQLite")
        sqlite_select_query = """SELECT * from contactos"""
        self.cursor.execute(sqlite_select_query)
        records = self.cursor.fetchall()
        i=0
        for row in records:
            idContacto = row[0]
            nombre = row[2]
            telefono = row[3]
            email = row[4]
            direccion = row[5]
            if(config.idUser == int(row[1])):
                self.listado.insert(parent='', index=i, iid=i, text='', values=(idContacto,nombre,telefono,email,direccion))
            i=i+1
                
    def eliminarListado(self):
        self.listado.delete(*self.listado.get_children())



    def eliminar(self):
        try:
            registro=self.listado.item(self.listado.focus(),"values")[0]
            print(registro)
            Respuesta=mb.askretrycancel(message='Estas seguro de eliminarlo??',title='CUIDADO!!!')
            if(Respuesta):
               #codigo para eliminar el registro de la BD
               self.abrirBD()
               self.cursor.execute('DELETE FROM contactos WHERE idContacto = ?',(registro,))
               self.conexion.commit()  
               print("Se elimino el contacto") 
               self.cerrarBD()
               self.eliminarListado()
               self.cargarDatos()
               pass

            else:
                print('No se elimino el contacto')
        except IndexError:
            mb.showinfo(message='Debes seleccionar un contacto',title='Aviso')

        


    def inicio(self):
        self.mainloop()


if(__name__=='__main__'):
    v=login()