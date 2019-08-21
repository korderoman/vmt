from tkinter import *
from tkinter import ttk

#importamos las demas vistas
from views.login import *
from views.formulario import *


class Index():
    def __init__(self,ventana):
        self.ventana=ventana
        #menu principal
        self.menu_principal=None
        #la vista por defecto deberá ser la de login
        login=Login(self.ventana)
        #login.frame_principal.pack(fill=BOTH)
        """Vistas adicionales"""
        formulario=Formulario(self.ventana)
        formulario.frame_principal.pack(fill=BOTH)
        #ejecutamos el menu principal
        self.crear_menu()
    
    def crear_menu(self):
        self.menu_principal=Menu(self.ventana)
        #creamos los elementos del submenu de incidencia
        subMenu_incidencia=Menu(self.menu_principal,tearoff=0)    
        subMenu_incidencia.add_command(label="Agregar Incidencia",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,0))
        #creamos los elementos del submenu de reportes
        subMenu_reportes=Menu(self.menu_principal,tearoff=0)
        subMenu_reportes.add_command(label="Reporte por fechas",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,0))
        subMenu_reportes.add_command(label="Reporte por OP",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,1))
        subMenu_reportes.add_command(label="Reporte por Turno",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,2))
        subMenu_reportes.add_command(label="Reportes Cruzados",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,3))

        #se agrega al menú principal los submenus
        self.menu_principal.add_command(label="Inicio", command=lambda:self.llamada_menus(self.menu_principal,1))
        self.menu_principal.add_cascade(label="Incidencias",menu=subMenu_incidencia)
        self.menu_principal.add_cascade(label="Reportes",menu=subMenu_reportes)
    def llamada_menus(self,submenu,posicion):
        pass
        