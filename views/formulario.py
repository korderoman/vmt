from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import ttk

class Formulario():
    def __init__(self,ventana):
        self.ventana=ventana
        self.mx=5
        self.my=2
        self.frame_principal=Frame(ventana)
        #administradores
        self.check_admin1=IntVar()
        self.check_admin2=IntVar()
        self.check_admin3=IntVar()
        #puesto
        self.radio_puesto=IntVar()
        #turno
        self.radio_turno=IntVar()
        """Operador"""
        self.operador=StringVar()
        self.camara=StringVar()
        self.incidencia=StringVar()
        self.descripcion=None
        """Fin de operador"""
        #inicializamos el método
        self.crear_interfaz(self.frame_principal)

    def crear_interfaz(self,frame):
        """Administradores"""
        administradores=LabelFrame(frame,text="Administradores",padx=self.mx,pady=self.my)
        Checkbutton(administradores,text="ENIT Nole",variable=self.check_admin1,onvalue=1,offvalue=0).grid(row=0,column=0, padx=self.mx,pady=self.my,sticky="w")
        Checkbutton(administradores,text="Pablo Chaupis",variable=self.check_admin2,onvalue=1,offvalue=0).grid(row=1,column=0, padx=self.mx,pady=self.my,sticky="w")
        Checkbutton(administradores,text="Jefe de Grupo",variable=self.check_admin3,onvalue=1,offvalue=0).grid(row=2,column=0, padx=self.mx,pady=self.my,sticky="w")
        administradores.grid(row=0,column=0,padx=self.mx,pady=self.my,sticky="wesn")
        """Puesto"""
        puestos=LabelFrame(frame,text="Puestos",padx=self.mx,pady=self.my)
        Radiobutton(puestos,text="OP1",variable=self.radio_puesto,value=1).grid(row=0, padx=self.mx,pady=self.my,column=0,sticky="we")
        Radiobutton(puestos,text="OP2",variable=self.radio_puesto,value=2).grid(row=0, padx=self.mx,pady=self.my,column=1,sticky="we")
        Radiobutton(puestos,text="OP3",variable=self.radio_puesto,value=3).grid(row=0, padx=self.mx,pady=self.my,column=2,sticky="we")
        Radiobutton(puestos,text="OP4",variable=self.radio_puesto,value=4).grid(row=1, padx=self.mx,pady=self.my,column=0,sticky="we")
        Radiobutton(puestos,text="OP5",variable=self.radio_puesto,value=5).grid(row=1, padx=self.mx,pady=self.my,column=1,sticky="we")
        puestos.grid(row=0,column=1,padx=self.mx,pady=self.my,sticky="wesn")
        """Turno"""
        turnos=LabelFrame(frame,text="Puestos",padx=self.mx,pady=self.my)
        Radiobutton(turnos,text="Mañana",variable=self.radio_turno,value=1).grid(row=0, padx=self.mx,pady=self.my,column=0,sticky="we")
        Radiobutton(turnos,text="Tarde",variable=self.radio_turno,value=2).grid(row=0, padx=self.mx,pady=self.my,column=1,sticky="we")
        Radiobutton(turnos,text="Noche",variable=self.radio_turno,value=3).grid(row=0, padx=self.mx,pady=self.my,column=2,sticky="we")
        turnos.grid(row=1,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky="we")
        """Operador"""
        datos=LabelFrame(frame,text="Reporte",padx=self.mx,pady=self.my)
        #operador
        Label(datos,text="Operador").grid(row=0,column=0,padx=self.mx,pady=self.my,sticky="w")
        Entry(datos,textvariable=self.operador).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky="we")
        #cámara
        Label(datos,text="Cámara").grid(row=1,column=0,padx=self.mx,pady=self.my,sticky="w")
        Entry(datos,textvariable=self.camara).grid(row=1,column=1,padx=self.mx,pady=self.my,sticky="we")
        #tipo
        Label(datos,text="Incidencia").grid(row=2,column=0,padx=self.mx,pady=self.my,sticky="w")
        tipo_incidencia=ttk.Combobox(datos,values=["N/A","V1","V2","V3"],state="readonly")
        tipo_incidencia.current(0)
        tipo_incidencia.grid(row=2,column=1,padx=self.mx,pady=self.my,sticky="we")
        #descripcion
        Label(datos,text="Descripción de la Incidencia").grid(row=3,column=0,padx=self.mx,pady=self.my,sticky="w")
        self.descripcion=tkst.ScrolledText(datos,wrap="word",height=5)
        self.descripcion.grid(row=4,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky="we")
        datos.grid(row=2,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky="we")
        """Botones de ejecución"""
        frame_botones=Frame(frame)
        Button(frame_botones,text="Guardar Reporte",command=self.guardar_registro).grid(row=0,column=0,padx=self.mx,pady=self.my,sticky="wens")
        Button(frame_botones,text="Mostrar Reportes",command=self.mostrar_reporte).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky="wens")
        frame_botones.grid(row=3,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky="wesn")
    """Funciones Auxiliares"""
    #guardar registro
    def guardar_registro(self):
        print("Guardo")
    #mostrar reporte
    def mostrar_reporte(self):
        print("Reporto")


