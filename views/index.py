from tkinter import *
from tkinter import ttk

#importamos las demas vistas
#from views.login import *
from views.incidencia import *
from views.reporte_total import *


class Index():
    def __init__(self,ventana):
        self.ventana=ventana
        #menu principal
        self.menu_principal=None
        """Vistas"""
        self.inicio=Frame(self.ventana)
        self.inicio.pack(fill=BOTH) #vista por defecto del index
        self.reporte_total=Reporte_Total(self.ventana)
        self.incidencia=Incidencia(self.ventana)
        #ejecutamos el menu principal
        self.crear_menu()
        #submenus
        self.submenus_lista=[
            "Inicio",
            "Agregar Incidencia",
            "Reporte General"
        ]
        #subframes
        self.submenus_frames=[
            self.inicio,
            self.incidencia.frame_principal,
            self.reporte_total.frame_principal
        ]

    def crear_menu(self):
        self.menu_principal=Menu(self.ventana)
        #creamos los elementos del submenu de incidencia
        subMenu_incidencia=Menu(self.menu_principal,tearoff=0)    
        subMenu_incidencia.add_command(label="Agregar Incidencia",underline=0,command=lambda:self.llamada_menus(subMenu_incidencia,0))
        #creamos los elementos del submenu de reportes
        subMenu_reportes=Menu(self.menu_principal,tearoff=0)
        subMenu_reportes.add_command(label="Reporte por fechas",underline=0,command=lambda:self.llamada_menus(subMenu_reportes,0))
        subMenu_reportes.add_command(label="Reporte por OP",underline=0,command=lambda:self.llamada_menus(subMenu_reportes,1))
        subMenu_reportes.add_command(label="Reporte por Turno",underline=0,command=lambda:self.llamada_menus(subMenu_reportes,2))
        subMenu_reportes.add_command(label="Reportes Cruzados",underline=0,command=lambda:self.llamada_menus(subMenu_reportes,3))
        subMenu_reportes.add_command(label="Reporte General",underline=0,command=lambda:self.llamada_menus(subMenu_reportes,4))
        #se agrega al menú principal los submenus
        self.menu_principal.add_command(label="Inicio", command=lambda:self.llamada_menus(self.menu_principal,1))
        self.menu_principal.add_cascade(label="Incidencias",menu=subMenu_incidencia)
        self.menu_principal.add_cascade(label="Reportes",menu=subMenu_reportes)
    
    def llamada_menus(self,submenu,posicion):
        menu_seleccionado=submenu.entrycget(posicion,"label")
        for index,menu in enumerate(self.submenus_lista):
            if(menu==menu_seleccionado):
                self.submenus_frames[index].pack(fill=BOTH)
            else:
                self.submenus_frames[index].pack_forget()
        